"""
직선 - 100원
코너 - 500원
bfs 로 풀되 각 위치에 memorization 을 한다.
"""
from pprint import pprint
import math
from collections import deque

def is_move(size, row, col):
    return 0 <= row < size and 0 <= col < size

def solution(board: list):
    size = len(board)

    memorization = [[math.inf] * size for _ in range(size)]
    memorization[0][0] = 0
    move = ((-1, 0), (0, 1), (1, 0), (0, -1))   # 방향 convention -> 0: 위 , 1: 오른쪽, 2: 아래, 3: 왼쪽

    def bfs():
        q = deque([(0, 0, 1), (0, 0, 2)])  # position(x, y), direction

        while q:
            x, y, head = q.popleft()
            for next_head, (dx, dy) in enumerate(move):
                nx, ny = x + dx, y + dy

                if is_move(size, nx, ny) and board[nx][ny] == 0 and (next_head + 2) % 4 != head:
                    cost = memorization[x][y] + 100
                    if head != next_head:
                        cost += 500
                    if memorization[nx][ny] >= cost:
                        memorization[nx][ny] = cost
                        q.append((nx, ny, next_head))
                        pprint(memorization)
    bfs()

    return memorization[-1][-1]


if __name__ == '__main__':
    # board = [[0,0,0],[0,0,0],[0,0,0]]
    # print(solution(board))
    # board = [[0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0],
    #  [0, 0, 0, 1, 0, 0, 0, 1], [0, 0, 1, 0, 0, 0, 1, 0], [0, 1, 0, 0, 0, 1, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0]]
    # print(solution(board))
    board = [[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]]
    print(solution(board))
    # board = [[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]]
    # print(solution(board))