# https://www.acmicpc.net/problem/1103
"""
dfs 사용
memoization 사용

"""
import sys

if __name__ == "__main__":
    sys.setrecursionlimit(int(1e9))
    n, m = map(int, input().split())

    table = [input() for _ in range(n)]

    memoization = [[0] * m for _ in range(n)]
    visit = [[False] * m for _ in range(n)]
    move = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    def dfs(x, y, depth):
        visit[x][y] = True
        weight = int(table[x][y])

        for dx, dy in move:
            nx, ny = x + (dx * weight), y + (dy * weight)

            if 0 <= nx < n and 0 <= ny < m and table[nx][ny] != 'H' and memoization[nx][ny] < depth + 1:
                if visit[nx][ny]:
                    memoization[0][0] = -1
                    return
                memoization[nx][ny] = depth + 1
                dfs(nx, ny, depth + 1)
        visit[x][y] = False

    memoization[0][0] = 1
    dfs(0, 0, 1)
    answer = -1
    if memoization[0][0] != -1:
        for row in range(n):
            for col in range(m):
                answer = max(answer, memoization[row][col])
    print(answer)
