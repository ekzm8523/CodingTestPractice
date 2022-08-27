# https://www.acmicpc.net/status?user_id=ekzm8523&problem_id=12865&from_mine=1
import sys

input = lambda: sys.stdin.readline().strip()

if __name__ == '__main__':
    stuff_count, max_weight = map(int, input().split())

    weights, values = [], []
    for _ in range(stuff_count):
        w, v = map(int, input().split())
        weights.append(w)
        values.append(v)
    # dp[i][j] : j weight까지 담을 수 있고 i번째 물건까지 담을 수 있을 때 최대 value
    dp = [[0] * (max_weight + 1) for _ in range(stuff_count)]

    # init
    for weight_idx in range(weights[0], max_weight + 1):
        dp[0][weight_idx] = values[0]

    for weight_idx in range(1, max_weight + 1):
        for stuff_idx in range(1, stuff_count):
            dp[stuff_idx][weight_idx] = max(
                dp[stuff_idx - 1][weight_idx],
                dp[stuff_idx - 1][weight_idx - weights[stuff_idx]] + values[stuff_idx] if weight_idx - weights[stuff_idx] >= 0 else 0
            )
    print(max(max(dp)))

'''
4 7
6 13
4 8
3 6
5 12
'''