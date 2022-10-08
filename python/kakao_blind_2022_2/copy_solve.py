

import argparse

from python.kakao_blind_2022_2.private_request import http_method

TOKEN = ""

get_method = lambda url: http_method(method="GET", base_url=args.base_url, sub_url=url, token=TOKEN)
post_method = lambda url, data: http_method(method="POST", base_url=args.base_url, sub_url=url, token=TOKEN, data=data)
put_method = lambda url, data: http_method(method="PUT", base_url=args.base_url, sub_url=url, token=TOKEN, data=data)


def start_api() -> str:
    data = {"problem": args.problem}
    auth_key = http_method(
        method="POST", base_url=args.base_url, sub_url="/start", init=True, token=args.init_token, data=data
    )
    return auth_key.get("auth_key")


def waiting_line_api() -> list:
    res_data = get_method("/waiting_line").get("waiting_line", [])
    return [(data['id'], data['from']) for data in res_data]


def game_result_api() -> list:
    res_data = get_method("/game_result").get("game_result", [])
    return [(data['win'], data['lose'], data['taken']) for data in res_data]


def user_info_api() -> list:
    res_data = get_method("/user_info").get("user_info")
    return [(data['id'], data['grade']) for data in res_data]


def match_api(match_data: list) -> None:
    data = {"pairs": match_data}
    res_data = put_method("/match", data)
    print(res_data)


def change_grade_api(skills) -> None:
    commands = []

    for key in skills:
        commands.append({"id": key, "grade": (skills[key] - 1) // 10})
    put_method("/change_grade", data={"commands": commands})


def score_api() -> None:
    res_data = get_method("/score")
    print(res_data)


def get_real_diff(taken) -> float:
    # taken = 40 - (diff / 99000 * 35)
    return (40 - taken) * 99000 / 35


def get_reliability(win_skill, lose_skill, real_diff) -> float:
    prob_with_lose = (lose_skill + real_diff) / (2 * lose_skill + real_diff)
    if 2 * win_skill - real_diff > 0:
        prob_with_win = win_skill / (2 * win_skill - real_diff)
        return (prob_with_win + prob_with_lose) / 2
    return prob_with_lose


def solve(args) -> dict:
    """
    - 초기에 모든 유저는 고유한 실력을 갖고 있으며, 실력은 1,000 이상 100,000 이하의 정수로 표현할 수 있다.
    - 모든 유저의 실력 분포는 평균이 40,000 표준편차가 20,000인 정규분포를 따른다.
    - 걸리는 시간은 40분 - (두 유저 간 고유 실력 차 / 99000 * 35) + e 으로 계산
    - 게임의 승부는 두 유저의 실력이 가중치로 쓰이며, 실력이 높은 유저가 이길 확률이 높다.
        유저 A와 유저 B가 게임을 했을 때, 유저 A가 이길 확률은 (유저 A의 고유 실력) / (유저 A의 고유 실력 + 유저 B의 고유 실력)과 같다.
    - 게임 한 판에 걸리는 시간은 최소 3분, 최대 40분이다.

    """
    global TOKEN
    TOKEN = start_api()
    skills = {user[0]: 40000 for user in user_info_api()}

    for now in range(595):
        game_result = game_result_api()
        for win, lose, taken in game_result:
            estimated_diff = abs(skills[win] - skills[lose])
            real_diff = get_real_diff(taken)
            error_diff = estimated_diff - real_diff
            prob = get_reliability(skills[win], skills[lose], real_diff)
            update_value = abs(error_diff * prob / 2)

            if update_value > 0:   # diff를 줄여야 하는 경우
                skills[win] = min(100_000, skills[win]+update_value)
                skills[lose] = max(1000, skills[lose]-update_value)
            # elif update_value < 0:  # diff를 늘려야 하는 경우
            #     skills[win] = max(MIN_SKILL, skills[win]+update_value)
            #     skills[lose] = min(MAX_SKILL, skills[lose]-update_value)

        waiting_line = waiting_line_api()
        waiting_line = sorted(waiting_line, key=lambda w: skills[w[0]], reverse=True)

        match_list = []
        i = 0
        while i + 1 < len(waiting_line):
            cur_user_id, next_user_id = waiting_line[i][0], waiting_line[i + 1][0]
            diff = (skills[cur_user_id] - skills[next_user_id]) / (waiting_line[i+1][1] // args.wait_weight + 1)
            if diff <= args.match_skill:
                match_list.append((cur_user_id, next_user_id))
                i += 2
            else:
                i += 1
        match_api(match_list)
    change_grade_api(skills)
    match_api([])
    score_api()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--problem", type=int, default=1)
    parser.add_argument("--init-token", type=str, default="81c6d4ed9812b5152fa85b783a682cfb")
    parser.add_argument("--base-url", type=str, default="https://huqeyhi95c.execute-api.ap-northeast-2.amazonaws.com/prod")
    parser.add_argument("--match-skill", type=int, default=20000)  # 매칭 가능한 능력의 최대 차이
    parser.add_argument("--wait-weight", type=int, default=3)  # 매칭 대기 시간에 가중치 부여
    args = parser.parse_args()
    solve(args)
