# https://www.acmicpc.net/problem/12865

if __name__ == "__main__":
    N, K = list(map(int, input().split()))
    WV_list = [list(map(int, input().split())) for _ in range(N)]

    dp = [[0] * (K + 1) for _ in range(N + 1)]
    answer = 0

    for i in range(1, N + 1):
        W, V = WV_list[i-1]

        for j in range(1, K + 1):
            if j >= W:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-W] + V)
            else:
                dp[i][j] = dp[i-1][j]


    print(dp[-1][-1])