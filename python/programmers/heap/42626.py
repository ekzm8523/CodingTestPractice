# https://programmers.co.kr/learn/courses/30/lessons/42626?language=python3

from heapq import heappop, heappush


def solution(scoville, K):
    answer = 0

    hq = []
    for score in scoville:
        heappush(hq, score)

    while hq and hq[0] < K and len(hq) > 1:
        first_min = heappop(hq)
        second_min = heappop(hq)
        heappush(hq, first_min + second_min * 2)
        answer += 1

    if hq and hq[0] < K:
        answer = -1

    return answer


if __name__ == '__main__':
    scoville = [1, 2, 3, 9, 10, 12]
    k = 7
    print(solution(scoville, k))
