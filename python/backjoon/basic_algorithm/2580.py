# https://www.acmicpc.net/problem/2580
from collections import deque
import sys

def find_candidate(x, y):
    candidate = set(range(1, 10))

    for i in range(9):
        if table[x][i] in candidate:
            candidate.remove(table[x][i])
        if table[i][y] in candidate:
            candidate.remove(table[i][y])

    x_grid = x // 3
    y_grid = y // 3

    for i in range(3):
        for j in range(3):
            nx = x_grid * 3 + i
            ny = y_grid * 3 + j
            if table[nx][ny] in candidate:
                candidate.remove(table[nx][ny])

    return tuple(candidate)

if __name__ == "__main__":
    table = [list(map(int, input().split())) for _ in range(9)]

    # 찾아야 하는 빈칸의 위치 미리 저장
    blanks = []
    for i in range(9):
        for j in range(9):
            if table[i][j] == 0:
                blanks.append((i, j))


    blanks_size = len(blanks)

    def dfs(depth):
        if depth == blanks_size:
            for row in table:
                print(*row)
            sys.exit(0)

        x, y = blanks[depth]
        candidate = find_candidate(x, y)
        for cand in candidate:
            table[x][y] = cand
            dfs(depth + 1)
            table[x][y] = 0

    dfs(0)





