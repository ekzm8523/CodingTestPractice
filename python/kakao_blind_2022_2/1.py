"""
실력은 1000 <= 실력 <= 100000
평균 40000, 표준편차 20000
모든 실력 중복 X

매칭시간 maximum 15분

무승부 X
시나리오 1은 어뷰저 X
시나리오 2는 어뷰저 O

게임이 오래 걸릴수록 가중치가 높아짐 (실력 차이가 없다는 것)
실력 차이가 작을수록 오래 걸리고 실력차이가 클수록 짧게 걸림
- 게임 한 판에 걸리는 시간은 3분~40분
- 걸리는 시간은 40분 - (두 유저 간 실력 차 / 99000 * 35) + e로 계산되고 소수점 이하는 버림
- e는 -5이상 5이하인 정수 중 무작위로 선택된 값
- 걸리는 시간이 3분보다 작으면 3, 40보다 크면 40

게임의 승부는 두 유저의 실력이 가중치로 쓰이며 실력이 높은 유저가 이길 확률이 높다.
- 유저 A와 유저 B가 게임을 했을 때, 유저 A가 이길 확률은 (유저 A의 고유 실력) / (유저 A의 고유 실력 + 유저 B의 고유 실력) 과 같다.

시나리오 1
- 매칭을 1번 이상 신청하는 유저의 수 : 30명
- 매칭 신청 빈도 : 분당 신청 수 평균 1건

시나리오 2
- 매칭을 1번 이상 신청하는 유저의 수 : 900명
- 매칭 신청 빈도 : 분당 신청 수 평균 45건
- 어뷰저 존재
  - 자신보다 낮은 실력을 가진 상대에게만 80% 확률로 진다.
  - 게임에 걸리는 시간은 10분 이하
  - 20%는 어뷰저가 승리함, 이때는 일반 게임과 같은 조건이므로 10분이 초과될수도
  - 전체 유저 중 어뷰저는 5%, 게임에 걸리는 시간은 3~10 랜덤값
  - 자신보다 높은 실력을 가진 유저한테는 어뷰징 안함
  - 만약 어뷰저 둘이 붙으면 둘 중 높은 실력을 가진 어뷰저가 80% 확률로 진다.


점수

정확성 점수 1
- 원래 고유 실력 순서와 내가 정의한 실력 순서를 비교해서 정확도

정확성 점수 2
- 두 유저가 얼마나 비슷한 실력끼리 매칭되었는가

"""

import requests
import json
import random

API_HOST = 'https://huqeyhi95c.execute-api.ap-northeast-2.amazonaws.com/prod'
headers = {
    'X-Auth-Token': '3afb1780dc2ca85c8486ca0f307187a6',
    'Content-Type': 'application/json'
}


def request(path, method, data: dict | None = None):
    url = API_HOST + path

    if method == 'GET':
        return requests.get(url, headers=headers)
    elif method == 'POST':
        return requests.post(url, headers=headers, data=json.dumps(data))
    elif method == 'PUT':
        return requests.put(url, headers=headers, data=json.dumps(data))


def get(path: str):
    response = request(f'/{path}', 'GET')
    return response.json()[path]


def match(data: list[list]):
    response = request(f"/match", "PUT", {"pairs": data})
    if response.status_code != 200:
        print()
        return None
    else:
        response = response.json()
        status, time = response['status'], response['time']
        return status, time


import math


# Function to calculate the Probability
def Probability(rating1, rating2):
    return 1.0 * 1.0 / (1 + 1.0 * math.pow(10, 1.0 * (rating1 - rating2) / 400))


# Function to calculate Elo rating
# K is a constant.
# d determines whether
# Player A wins or Player B.
def EloRating(Ra, Rb, K, d):
    # To calculate the Winning
    # Probability of Player B
    Pb = Probability(Ra, Rb)

    # To calculate the Winning
    # Probability of Player A
    Pa = Probability(Rb, Ra)

    # Case -1 When Player A wins
    # Updating the Elo Ratings
    if (d == 1):
        Ra = Ra + K * (1 - Pa)
        Rb = Rb + K * (0 - Pb)


    # Case -2 When Player B wins
    # Updating the Elo Ratings
    else:
        Ra = Ra + K * (0 - Pa)
        Rb = Rb + K * (1 - Pb)
    return Ra, Rb


# Driver code

# Ra and Rb are current ELO ratings
# Ra = 1200
# Rb = 1000
# K = 30
# d = 1
# EloRating(Ra, Rb, K, d)

if __name__ == '__main__':
    # auth_key를 발급 받고, 문제 풀이 시작
    response = request('/start', 'POST', {"problem": 1})
    auth_key = response.json()['auth_key']
    headers['Authorization'] = auth_key
    # match_weight = 20
    turn = 1
    match([])
    user_info_list = get("user_info")
    user_info = {info['id']: 1500 for info in user_info_list}
    while turn < 596:

        waiting_line = get("waiting_line")
        user_ids = []
        for row in waiting_line:
            user_id, waiting_time = row['id'], turn - row['from']
            user_ids.append(user_id)
        user_ids.sort(key=lambda x: user_info[x])
        matching_order = [[user_ids[i], user_ids[i+1]] for i in range(len(user_ids) // 2)]
        response = match(matching_order)
        turn += 1

        game_result = get("game_result")
        for result in game_result:
            win, lose, taken = result['win'], result['lose'], result['taken']
            user_info[win], user_info[lose] = EloRating(user_info[win], user_info[lose], 40 - taken, 1)
            # user_info[win] += match_weight
            #  -= match_weight

    commands = [{"id": key, "grade": user_info[key]} for key in user_info]
    response = request("/change_grade", "PUT", {"commands": commands})
    response = request("/score", "GET")
    print(response.json())
    print()

