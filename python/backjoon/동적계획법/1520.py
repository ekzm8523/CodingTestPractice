# https://www.acmicpc.net/problem/1520
import sys
move = [[0, -1], [1, 0], [0, 1], [-1, 0]]

def dfs(x, y):
    if x == M-1 and y == N-1:
        return 1

    if dp[x][y] != -1:
        return dp[x][y]

    dp[x][y] = 0
    for i in range(4):
        nx = x + move[i][0]
        ny = y + move[i][1]
        if 0 <= nx < M and 0 <= ny < N:
            if matrix[nx][ny] < matrix[x][y]:
                dp[x][y] += dfs(nx, ny)
    
    return dp[x][y]


if __name__ == "__main__":
    sys.setrecursionlimit(1000000)

    M, N = map(int, input().split())

    matrix = [list(map(int, input().split())) for _ in range(M)]
    dp = [[-1] * N for _ in range(M)]

    print(dfs(0,0))