# https://www.acmicpc.net/problem/13305

import sys

if __name__ == "__main__":
    N = int(input())
    distance_list = list(map(int, input().split()))
    oil_list = list(map(int, input().split()))

    oil_min = oil_list[0]
    answer = 0

    for i in range(N-1):
        if oil_min > oil_list[i]:
            oil_min = oil_list[i]
        answer += (oil_min * distance_list[i])

    print(answer)