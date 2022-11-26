import argparse
from pprint import pprint

from private_request import http_method
from heapq import heappop as pop, heappush as push
problem_info = {1: {"num_days": 200, "high": 3, "width": 20, "avg_req_a_day": 1},
                2: {"num_days": 1000, "high": 10, "width": 200, "avg_req_a_day": 4}}

TOKEN = ""
get_method = lambda url: http_method(method="GET", base_url=args.base_url, sub_url=url, token=TOKEN)
post_method = lambda url, data: http_method(method="POST", base_url=args.base_url, sub_url=url, token=TOKEN, data=data)
put_method = lambda url, data: http_method(method="PUT", base_url=args.base_url, sub_url=url, token=TOKEN, data=data)
tracking = {
        "fail_cnt": 0,  # P
        "reject_req_room_cnt": 0,  # A
        "every_req_room_cnt": 0,  # T2
        "reject_req_cnt": 0,  # R
        "every_req_cnt": 0,  # T3
    }

def start_api(problem, init_token) -> str:
    assert 1 <= problem <= 2
    resp = http_method("POST", args.base_url, "/start", data={'problem': problem}, token=init_token, init=True)
    if type(resp) is dict:
        return resp.get('auth_key', "")
    return ""


def new_requests_api() -> list:
    res_data = get_method("/new_requests").get("reservations_info")
    return [(data["id"], data["amount"], data['check_in_date'], data['check_out_date']) for data in res_data]


def reply_api(replies: list) -> None:
    req_data = [{"id": reply[0], "reply": reply[1]} for reply in replies]
    res_data = put_method("/reply", data={"replies": req_data})
    # print(f"{res_data} : {req_data} 적용 완료")


def simulate_api(room_assigns: list) -> None:
    global tracking
    req_data = [{"id": room_assign[0], "room_number": room_assign[1]} for room_assign in room_assigns]
    res_data = put_method("/simulate", data={"room_assign": req_data})
    tracking['fail_cnt'] += res_data.get("fail_count")
    # print(res_data)


def score_api():
    res_data = get_method("/score")
    print(res_data)


def reservation(table, amount, check_in, check_out) -> int | None:
    for start_floor in range(len(table)):
        for start_room in range(len(table[0]) - amount + 1):
            available = True
            for day in range(check_in, check_out):
                if available and any((day in room for room in table[start_floor][start_room:start_room + amount])):
                    available = False
                    break
            if available:
                for day in range(check_in, check_out):
                    for i in range(amount):
                        table[start_floor][start_room + i].add(day)
                return (start_floor + 1) * 1000 + start_room + 1
    return None


def solve(args) -> None:
    """
    정확성 -> 객실 이용률
    효율성 -> 요청해서 얼마나 빨리 예약이 되었는지
    패널티 -> 예약 했는데 객실 배정에 실패했을 때

    호텔의 객실 이용률이 목표치 이상이 되도록 예약을 관리하거나 객실을 배정하면서, 객실 수가 많은 예약은 최대한 거절하지 않아야 합니다.
    접근 방법
    weight = (checkout - checkin) * amount
    하루 평균량 만큼만 뽑자

    인원수 * 예약일수 -> weight로 두고 우선순위를 최상으로 주자
    최대한 미뤄가면서 마지막에 판단하기 -> 더 좋은 우선순위의 예약이 있을수도 있으니까?
    성수기 시즌임을 감지하는 코드가 하나 있어야함 -> 갑자기 요청수가 늘어난다던가 그런거를 확인하는 코드 -> flag로
    """
    global TOKEN
    TOKEN = start_api(args.problem, args.init_token)
    table = [[set() for _ in range(problem_info[args.problem]['width'])] for _ in range(problem_info[args.problem]['high'])]

    reservation_dict = {i: [] for i in range(1, problem_info[args.problem]['num_days'] + 1)}
    request_dict = {}
    requests_with_weight = []

    # parameter
    for now in range(1, problem_info[args.problem]['num_days'] + 1):
        pprint(tracking)
        new_requests = new_requests_api()
        pprint(new_requests)
        for req_id, amount, check_in, check_out in new_requests:
            tracking['every_req_cnt'] += 1
            request_dict[req_id] = (amount, check_in, check_out)
            weight = amount * (check_out - check_in)
            tracking['every_req_room_cnt'] += weight
            deadline = min(check_in - 1, now + 14)
            push(requests_with_weight, (-weight, deadline, req_id))

        process_cnt = 0
        accept_request = []
        remain_request = []
        while requests_with_weight:
            print(requests_with_weight)
            weight, deadline, req_id = pop(requests_with_weight)

            if deadline < now:
                tracking['reject_req_room_cnt'] -= weight
                tracking['reject_req_cnt'] += 1
                continue
            # remain_day = deadline - now
            # if 1 < remain_day < 5:
            #     remain_request.append((weight, deadline, req_id))
            # else:
            amount, check_in, check_out = request_dict[req_id]
            response = reservation(table, amount, check_in, check_out)
            if response is not None:
                accept_request.append((req_id, "accepted"))
                reservation_dict[check_in].append((req_id, response))
                process_cnt += 1
            else:
                tracking['reject_req_room_cnt'] -= weight
                tracking['reject_req_cnt'] += 1
        for req in remain_request:
            push(requests_with_weight, req)
        reply_api(accept_request)
        simulate_api(reservation_dict[now])
    score_api()
    print()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--problem", type=int, default=1)
    parser.add_argument("--init-token", type=str, default="9e9bc6368b5689c6138d143d41111706")
    parser.add_argument("--base-url", type=str, default="https://68ecj67379.execute-api.ap-northeast-2.amazonaws.com/api")
    args = parser.parse_args()
    solve(args)

"""
p1
{'accuracy_score': 80.0, 'efficiency_score': 9.243027888446214, 'penalty_score': 196.58796119984765, 'score': 392.6550666885986}

p2
{'accuracy_score': 80.0, 'efficiency_score': 9.006995393277599, 'penalty_score': 119.56221156571709, 'score': 469.4447838275605}

"""