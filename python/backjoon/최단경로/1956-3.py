import sys
import math


input = lambda: sys.stdin.readline()


if __name__ == "__main__":
    node_cnt, edge_cnt = map(int, input().split())

    dp = [[math.inf] * node_cnt for _ in range(node_cnt)]

    for _ in range(edge_cnt):
        u, v, w = map(int, input().split())
        dp[u-1][v-1] = w

    for i in range(node_cnt):
        for j in range(node_cnt):
            for k in range(node_cnt):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

    answer = math.inf
    for i in range(node_cnt):
        answer = min(answer, dp[i][i])

    print(answer if answer != math.inf else -1)
