# https://www.acmicpc.net/problem/2178

from collections import deque

if __name__ == "__main__":
    N, M = list(map(int, input().split()))
    miro = [list(map(int, input())) for _ in range(N)]

    # row, col 시계방향
    direction = [[-1, 0], [0, 1], [1, 0], [0, -1]]

    queue = deque()
    queue.append((0, 0))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + direction[i][0]
            ny = y + direction[i][1]

            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if miro[nx][ny] == 0:
                continue
            if miro[nx][ny] == 1:
                miro[nx][ny] = miro[x][y] + 1
                queue.append((nx, ny))

    print(miro[-1][-1])
