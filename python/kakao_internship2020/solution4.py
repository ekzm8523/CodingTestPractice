# https://programmers.co.kr/learn/courses/30/lessons/67259

from collections import deque
from pprint import pprint
move = [(-1, 0), (0, 1), (1, 0), (0, -1)]   # 0: up 1: right 2:down 3: left

# def isMove(board, point, dir):
#
#     size = len(board)
#     if 0 <= point[0] + move[dir][0] < size and 0 <= point[1] + move[dir][1] < size:
#         return True
#     return False
#
# def solution(board):
#
#     point1 = [0, 0, 1]
#     point2 = [0, 0, 2]
#     # 오른쪽 출발
#     def bfs(point):
#         q = deque()
#         q.append(point)
#         q.append(point2)
#         while q:
#             x, y, dir = q.popleft()
#             for i in range(4):
#                 # print(x,y,dir,q,i)
#                 if not isMove(board, [x,y], i): # out of range
#                     continue
#                 if abs(dir - i) == 2: # 반댓방향 고려 x
#                     continue
#                 nx = x + move[i][0]
#                 ny = y + move[i][1]
#
#                 if board[nx][ny] == 1: # 벽일경우
#                     continue
#
#                 if board[nx][ny] == 0:
#                     if dir == i:
#                         board[nx][ny] = board[x][y] + 100
#                         q.append([nx, ny, i])
#                     # elif abs(dir - i) == 1:
#                     else:
#                         board[nx][ny] = board[x][y] + 600
#                         q.append([nx, ny, i])
#                 else: # 0도 1도 아닌 이미 들렸던 길
#                     if dir == i and board[nx][ny] >= board[x][y] + 100:
#                         board[nx][ny] = board[x][y] + 100
#                         q.append([nx, ny, i])
#                     elif abs(dir - i) == 1 and board[nx][ny] >= board[x][y] + 600:
#                         board[nx][ny] = board[x][y] + 600
#                         q.append([nx, ny, i])
#
#         return board[-1][-1]
#     return min(bfs(point1), bfs(point2))

import math

def solution2(board):

    def bfs(start):
        table = [[math.inf for _ in range(len(board))] for _ in range(len(board))]
        queue = deque([start])

        table[0][0] = 0
        while queue:
            x, y, cost, head = queue.popleft()
            for idx, (dx, dy) in enumerate(move):
                nx, ny = x + dx, y + dy

                n_cost = cost + 600 if idx != head else cost + 100
                if 0 <= nx < len(board) and 0 <= ny < len(board) and board[nx][ny] == 0 and table[nx][ny] > n_cost:
                    table[nx][ny] = n_cost
                    queue.append((nx, ny, n_cost, idx))
        return table[-1][-1]
    return min(bfs((0,0,0,1)), bfs((0,0,0,2)))

if __name__ == "__main__":
    # pprint(solution([[0,0,0],
    #                 [0,0,0],
    #                 [0,0,0]]))
    # pprint(solution([[0,0,0,0,0,0,0,1],
    #                 [0,0,0,0,0,0,0,0],
    #                 [0,0,0,0,0,1,0,0],
    #                 [0,0,0,0,1,0,0,0],
    #                 [0,0,0,1,0,0,0,1],
    #                 [0,0,1,0,0,0,1,0],
    #                 [0,1,0,0,0,1,0,0],
    #                 [1,0,0,0,0,0,0,0]]))
    pprint(solution2([[0,0,1,0],
                    [0,0,0,0],
                    [0,1,0,1],
                    [1,0,0,0]]))
    # pprint(solution([[0,0,0,0,0,0],
    #                 [0,1,1,1,1,0],
    #                 [0,0,1,0,0,0],
    #                 [1,0,0,1,0,1],
    #                 [0,1,0,0,0,1],
    #                 [0,0,0,0,0,0]]))