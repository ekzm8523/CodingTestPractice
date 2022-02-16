# https://programmers.co.kr/learn/courses/30/lessons/92342
# 라이언이 가장 큰 점수 차이로 우승할 수 있는 방법이 여러 가지 일 경우, 가장 낮은 점수를 더 많이 맞힌 경우를 return 해주세요.
from itertools import combinations_with_replacement
from collections import Counter

def solution(n, info):
    answer = []
    # Todo : 중복조합을 활용해서 문제풀기
    # Todo : DFS를 통해 문제 풀기
    # print()
    # for comb in combinations_with_replacement(range(11), n):
    #     lion = [0 for _ in range(11)]
    #     for k, v in Counter
    #     for obj in comb:
    #         lion[obj] += 1



    return answer


if __name__ == '__main__':
    n = 5
    info = [2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]
    print(solution(n, info))
    # assert solution(n, info) == [0,2,2,0,1,0,0,0,0,0,0]

    n = 1
    info = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    print(solution(n, info))
    # assert solution(n, info) == [-1]

    n = 9
    info = [0, 0, 1, 2, 0, 1, 1, 1, 1, 1, 1]
    print(solution(n, info))
    # assert solution(n, info) == [1,1,2,0,1,2,2,0,0,0,0]

    n = 10
    info = [0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 3]
    print(solution(n, info))
    # assert solution(n, info) == [1,1,1,1,1,1,1,1,0,0,2]
