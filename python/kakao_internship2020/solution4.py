# https://programmers.co.kr/learn/courses/30/lessons/67259

from collections import deque
from pprint import pprint
import math

move = [(-1, 0), (0, 1), (1, 0), (0, -1)]   # 0: up 1: right 2:down 3: left

def solution(board):

    point1 = [0, 0, 0, 1]
    point2 = [0, 0, 0, 2]

    def bfs(start):
        size = len(board)
        table = [[math.inf for _ in range(size)] for _ in range(size)]
        q = deque([start])
        table[0][0] = 0

        while q:
            x, y, cost, dir = q.popleft()
            for i, (dx, dy) in enumerate(move):
                nx, ny = x + dx, y + dy

                n_cost = cost + 600 if i != dir else cost + 100
                if 0 <= nx < size and 0 <= ny < size and board[nx][ny] == 0 and table[nx][ny] > n_cost:
                    table[nx][ny] = n_cost
                    q.append([nx, ny, n_cost, i])

        return table[-1][-1]


    return min(bfs(point1), bfs(point2))

if __name__ == "__main__":
    pprint(solution([[0,0,0],
                    [0,0,0],
                    [0,0,0]]))
    pprint(solution([[0,0,0,0,0,0,0,1],
                    [0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,1,0,0],
                    [0,0,0,0,1,0,0,0],
                    [0,0,0,1,0,0,0,1],
                    [0,0,1,0,0,0,1,0],
                    [0,1,0,0,0,1,0,0],
                    [1,0,0,0,0,0,0,0]]))
    pprint(solution([[0,0,1,0],
                    [0,0,0,0],
                    [0,1,0,1],
                    [1,0,0,0]]))
    pprint(solution([[0,0,0,0,0,0],
                    [0,1,1,1,1,0],
                    [0,0,1,0,0,0],
                    [1,0,0,1,0,1],
                    [0,1,0,0,0,1],
                    [0,0,0,0,0,0]]))


