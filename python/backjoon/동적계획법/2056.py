# https://www.acmicpc.net/problem/2056

"""
N개의 작업 (3 <= N <= 10000)
시간 (1 <= time <= 100)

"""

if __name__ == "__main__":
    N = int(input())

    # 예쁜 input
    work = [[None, []] for _ in range(N+1)]
    for i in range(1, N+1):
        read_line = list(map(int, input().split()))
        work[i][0] = read_line[0]
        if read_line[1] > 0:
            work[i][1] = read_line[2:]

    dp = [0] * (N + 1)
    for i in range(1, N+1):
        max_prev_time = 0
        for prev_work in work[i][1]:
            max_prev_time = max(dp[prev_work], max_prev_time)
        dp[i] = max_prev_time + work[i][0]
    print(max(dp))


