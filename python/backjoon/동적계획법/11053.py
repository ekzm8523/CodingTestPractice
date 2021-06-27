# https://www.acmicpc.net/problem/11053

if __name__ == "__main__":
    N = int(input())
    seq = list(map(int, input().split()))

    dp = [0 for _ in range(N)]

    for i in range(N):
        for j in range(i):
            if seq[i] > seq[j] and dp[i] < dp[j]:
                dp[i] = dp[j]

        dp[i] += 1
    print(max(dp))