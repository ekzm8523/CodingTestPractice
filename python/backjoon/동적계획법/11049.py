# https://www.acmicpc.net/problem/11049

# dp[i][j] -> i부터 j까지 곱셈량의 최솟값
# dp[i][j] -> dp[i][k] + dp[k+1][j] + matrix_list[i][0] * matrix_list[k][1] * matrix_list[j][1]
import sys

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    matrix_list = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]

    dp = [[0] * n for _ in range(n)]

    for interval_size in range(1, n):
        for i in range(n - interval_size):
            j = i + interval_size
            dp[i][j] = sys.maxsize
            for k in range(i, j):
                weight = matrix_list[i][0] * matrix_list[k][1] * matrix_list[j][1]
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j] + weight)

    print(dp[0][n-1])
