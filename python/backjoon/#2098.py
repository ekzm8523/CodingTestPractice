# https://www.acmicpc.net/problem/2098
"""
외판원 문제 (Traveling Salesman problem)
완탐문제, 단순하게 풀면 N!으로 시간초과
동적계획법 + 비트마스크
dp[current][visited] = min(dp[current][visited], tsp(next, visited + next) + w[current][next]
종료조건
1. 이미 구한 DP가 있을떄
2. 모든 노드를 방문했을때

w[0]
"""
import sys

if __name__ == "__main__":
    N = int(input())
    INF = sys.maxsize

    DP = [[INF] * (1 << N) for _ in range(N)]

    W = []
    for i in range(N):
        W.append(list(map(int, input().split())))

    def TSP(current, visited):
        if visited == (1 << N) - 1:
            return W[current][0] or INF

        if DP[current][visited] != INF:
            return DP[current][visited]

        for city in range(N):
            if visited & (1 << city) == 0 and W[current][city] != 0:
                DP[current][visited] = min(DP[current][visited],
                                           TSP(city, visited | (1 << city)) + W[current][city])
        return DP[current][visited]

    print(TSP(0, 1 << 0))

"""
4
0 10 15 20
5 0 9 10
6 13 0 12
8 8 9 0

35
"""