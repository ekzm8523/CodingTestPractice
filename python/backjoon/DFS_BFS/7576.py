# https://www.acmicpc.net/problem/7576
from collections import deque

move = ((-1, 0), (0, 1), (1, 0), (0, -1))


def bfs(board):

    q = deque()
    ripe_cnt = 0
    empty_cnt = 0
    for row in range(N):
        for col in range(M):
            if board[row][col] == 1:
                q.append((row, col, 0))
                ripe_cnt += 1
            if board[row][col] == -1:
                empty_cnt += 1

    while q:
        x, y, day = q.popleft()
        for dx, dy in move:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == 0:
                board[nx][ny] = 1
                q.append((nx, ny, day + 1))
                ripe_cnt += 1
    return day if ripe_cnt == (M * N) - empty_cnt else -1


if __name__ == '__main__':
    M, N = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    print(bfs(board))

