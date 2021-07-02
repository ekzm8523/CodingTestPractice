# https://www.acmicpc.net/problem/1563

"""
지각 두번 이상 or 결석을 세번 연속으로 한 사람
"""
import sys

def dfs(day, late, absent):
    if late == 2 or absent == 3:
        return 0

    if day == N:
        return 1

    if dp[day][late][absent] == 0:
        dp[day][late][absent] = dfs(day + 1, late, 0) + dfs(day + 1, late + 1, 0) + dfs(day + 1, late, absent + 1)

    return dp[day][late][absent]



if __name__ == "__main__":
    sys.setrecursionlimit(1000000)
    N = int(input())

    # dp = [[[0] * 3] * 2] * N
    dp = [[[0 for absent in range(3)] for late in range(2)] for day in range(N)]
    print(dfs(0, 0, 0) % 1000000)


