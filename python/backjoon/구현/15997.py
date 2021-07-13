# https://www.acmicpc.net/problem/15997

"""
4개의 팀이 조별리그를 진행
한 팀은 자신을 제외한 모든 상대방과 한 번씩 총 3번의 경기를 치른다.
승리 : 3점 , 비김 : 1점, 패배 : 0점
승점이 같을 시에는 추첨으로 순위를 정함, 추첨은 공평하게 진행, 순위를 정한 후 상위 2팀은 다음 라운드로 진
"""
# import sys
#
#
# if __name__ == "__main__":
#
#     participate_list = sys.stdin.readline().split()
#     participate_dic = {}
#     answer = {}
#     for participate in participate_list:
#         participate_dic[participate] = 0
#         answer[participate] = 0.0
#
#
#     for _ in range(6):
#         A, B, W, D, L = sys.stdin.readline().split()
#         W, D, L = float(W), float(D), float(L)
#         participate_dic[A] += (3 * W + D)
#         participate_dic[B] += (3 * L + D)
#     result = sorted(participate_dic.items(), key=lambda x: x[1], reverse=True)
#
#     # 1등이 확실히 갈릴때
#     first, second, third, fourth = result[0][0], result[1][0], result[2][0], result[3][0]
#     if result[0][1] != result[1][1]:
#         answer[first] = 1.0
#         if result[1][1] != result[2][1]: # 2등도 확실히 갈릴 때
#             answer[second] = 1.0
#         elif result[1][1] == result[2][1]: # 2등 3등 같을 때
#             if result[2][1] == result[3][1]: # 3등 4등까지도 같을 때
#                 answer[second] = answer[third] = answer[fourth] = 1 / 3
#             else: # 3등 4등은 갈릴 때
#                 answer[second] = answer[third] = 1 / 2
#     else: # 1등하고 2등하고 같을 때
#         if result[1][1] != result[2][1]: # 2등 3등은 갈릴 때
#             answer[first] = answer[second] = 1
#         elif result[1][1] == result[2][1]: # 1, 2, 3등 같을 때
#             if result[2][1] == result[3][1]: # 1, 2, 3, 4등 전부 동점
#                 answer[first] = answer[second] = answer[third] = answer[fourth] = 1 / 2
#             else: # 1, 2, 3등은 같고 4등은 다를 때
#                 answer[first] = answer[second] = answer[third] = 2 / 3
#
#     for participate in participate_list:
#         print(answer[participate])

import sys
from collections import defaultdict

if __name__ == "__main__":
    nations = sys.stdin.readline().split()
    percentage = defaultdict(int)
    expected_score = defaultdict(int)
    schedule = []
    for _ in range(3):
        temp = []
        for _ in range(2):
            temp.append(sys.stdin.readline().split())
        schedule.append(temp)

    def battle(match_day, idx, expected_score, rate):
        global total, final_score

        if match_day == 3:
            winner = sorted(expected_score.items(), key=lambda x: x[1], reverse=True)

            # 전원 동점인 경우
            if len(set([i[1] for i in winner])) == 1:
                for nation in winner:
                    percentage[nation[0]] += rate * (2 / len(winner))
                return

            # 2위에서 동점자 존재
            elif winner[0][1] != winner[1][1] and winner[1][1] == winner[2][1]:
                percentage[winner[0][0]] += rate
                equal_value = winner[1][1]
                scores = [i for i in winner if i[1] == equal_value]

                for nation in scores:
                    percentage[nation[0]] += rate * (1 / len(scores))
                return

            # 1위에서 동점자 존재
            elif winner[0][1] == winner[1][1]:
                equal_value = winner[0][1]
                scores = [i for i in winner if i[1] == equal_value]
                for nation in scores:
                    percentage[nation[0]] += rate * (2 / len(scores))
                return
            else:
                for nation in winner[:2]:
                    percentage[nation[0]] += rate
                return

        if idx == 2:
            battle(match_day + 1, 0, expected_score, rate)
            return
        n1, n2, win, draw, lose = schedule[match_day][idx]
        win, draw, lose = map(float, [win, draw, lose])

        # n1이 n2를 이길 경우
        expected_score[n1] += 3
        battle(match_day, idx + 1, expected_score, rate * win)
        expected_score[n1] -= 3

        # 비길 경우
        expected_score[n1] += 1
        expected_score[n2] += 1
        battle(match_day, idx + 1, expected_score, rate * draw)
        expected_score[n2] -= 1
        expected_score[n1] -= 1

        # n2가 n1 이길 경우
        expected_score[n2] += 3
        battle(match_day, idx + 1, expected_score, rate * lose)
        expected_score[n2] -= 3

    battle(0, 0, expected_score, 1)
    for nation in nations:
        print(percentage[nation])
































