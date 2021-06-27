# https://www.acmicpc.net/problem/1463

if __name__ == "__main__":
    N = int(input())

    dp = [1000001 for i in range(0, N+1)]
    dp[1] = 0
    for i in range(1, N):
        if i * 3 <= N:
            dp[i * 3] = min(dp[i] + 1, dp[i * 3])
        if i * 2 <= N:
            dp[i * 2] = min(dp[i] + 1, dp[i * 2])
        dp[i + 1] = min(dp[i] + 1, dp[i + 1])

    print(dp[-1])