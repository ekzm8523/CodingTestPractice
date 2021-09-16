# https://www.acmicpc.net/problem/2096
import sys

if __name__ == "__main__":

    n = int(sys.stdin.readline())
    INF = sys.maxsize
    # min_dp = [[INF] * 3 for _ in range(n)]
    # max_dp = [[0] * 3 for _ in range(n)]
    min_dp = [INF] * 3
    max_dp = [0] * 3
    for i in range(n):
        a, b, c = map(int, sys.stdin.readline().split())
        if i == 0:
            min_dp[0] = max_dp[0] = a
            min_dp[1] = max_dp[1] = b
            min_dp[2] = max_dp[2] = c
        else:
            next_0 = min(min_dp[0], min_dp[1]) + a
            next_1 = min(min_dp[0], min_dp[1], min_dp[2]) + b
            next_2 = min(min_dp[1], min_dp[2]) + c
            min_dp = [next_0, next_1, next_2]
            next_0 = max(max_dp[0], max_dp[1]) + a
            next_1 = max(max_dp[0], max_dp[1], max_dp[2]) + b
            next_2 = max(max_dp[1], max_dp[2]) + c
            max_dp = [next_0, next_1, next_2]
    print(max(max_dp))
    print(min(min_dp))
