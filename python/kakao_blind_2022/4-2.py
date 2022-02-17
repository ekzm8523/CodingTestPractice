# https://programmers.co.kr/learn/courses/30/lessons/92342
# 라이언이 가장 큰 점수 차이로 우승할 수 있는 방법이 여러 가지 일 경우, 가장 낮은 점수를 더 많이 맞힌 경우를 return 해주세요.
# from itertools import combinations_with_replacement
# from collections import Counter
#
#
# def calculate_score(lion: list[int], apeach: list[int]) -> int:
#     final_score = 0
#     for score, (l, a) in enumerate(zip(lion, apeach)):
#         if l == a == 0:
#             continue
#         if l > a:
#             final_score += score
#         else:
#             final_score -= score
#
#     return final_score
#
#
# def is_change(answer: list[int], new_answer: list[int]) -> bool:
#     for a, b in zip(answer, new_answer):
#         if a < b:
#             return True
#         elif a > b:
#             return False
#     return False  # 이 경우는 없음
#
#
# def solution(n, info):
#     answer = []
#     apeach = list(reversed(info))
#     max_score = 0
#     for comb in combinations_with_replacement(range(11), n):
#         lion = [0 for _ in range(11)]
#         for key, value in Counter(comb).items():
#             lion[key] = value
#
#         score = calculate_score(lion, apeach)
#         if score > max_score:
#             max_score, answer = score, lion.copy()
#         elif score == max_score and is_change(answer, lion):
#             max_score, answer = score, lion.copy()
#     answer.reverse()
#     return answer if answer else [-1]

answer = []
max_score = 0
def solution2(n, info):
    apeach = list(reversed(info))
    print()
    # answer = []
    # max_score = 0
    lion = [0 for _ in range(11)]

    def dfs(lion, idx, remain_arrow_cnt, score):
        global max_score, answer

        if idx == 11 or remain_arrow_cnt == 0:
            for i in range(idx, 11):
                if apeach[i] != 0:
                    score -= i
            if max_score < score:
                max_score = score
                answer = lion.copy()
            return

        assert remain_arrow_cnt > 0, "예외발생"

        # lion이 이겼을때
        if apeach[idx] < remain_arrow_cnt:
            lion[idx] = apeach[idx] + 1
            dfs(lion, idx + 1, remain_arrow_cnt - lion[idx], score + idx)
            lion[idx] = 0
        else:
            for i in range(idx, 11):
                if apeach[i] != 0:
                    score -= i
            if max_score < score:
                max_score = score
                answer = lion.copy()

        # lion이 졌을때
        dfs(lion, idx + 1, remain_arrow_cnt, score - idx)


    dfs(lion, 0, n, 0)
    print(answer)
    print(apeach)
    print(max_score)
    # print(answer, max_score)

if __name__ == '__main__':
    n = 5
    info = [2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]
    # print(solution(n, info))
    print(solution2(n, info))
    # assert solution(n, info) == [0,2,2,0,1,0,0,0,0,0,0]

    n = 1
    info = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    # print(solution(n, info))
    print(solution2(n, info))
    # assert solution(n, info) == [-1]

    n = 9
    info = [0, 0, 1, 2, 0, 1, 1, 1, 1, 1, 1]
    # print(solution(n, info))
    print(solution2(n, info))
    # assert solution(n, info) == [1,1,2,0,1,2,2,0,0,0,0]

    n = 10
    info = [0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 3]
    # print(solution(n, info))
    print(solution2(n, info))
    # assert solution(n, info) == [1,1,1,1,1,1,1,1,0,0,2]
