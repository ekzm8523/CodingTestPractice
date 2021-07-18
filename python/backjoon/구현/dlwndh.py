import sys
from typing import List


def solution(row: int, col: int) -> None:
    def dfs(x: int, y: int, direction: int = -1):

        if graph[x][y] == '.':
            print(x + 1, y + 1, find_pipe(x, y))
        else:
            # 안끊겼을 때
            if direction != -1:
                nx = x + dx[direction]
                ny = y + dy[direction]
                if is_valid(nx, ny):
                    nd = find_direction(graph[nx][ny], direction)

                    dfs(nx, ny, nd)
            # 초기 방향 없을때(M일때)
            else:
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if not is_valid(nx, ny):
                        continue
                    if graph[nx][ny] != '.':
                        dfs(nx, ny, i)

    def find_pipe(x: int, y: int) -> str:
        ret = ''
        dir_check = [False] * 4
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not is_valid(nx, ny):
                continue
            adj_node = graph[nx][ny]
            if adj_node != ".":
                if i == 0 and adj_node in {'|', '+', '1', '4'}:
                    dir_check[i] = True
                elif i == 1 and adj_node in {'|', '+', '2', '3'}:
                    dir_check[i] = True
                elif i == 2 and adj_node in {'-', '+', '1', '2'}:
                    dir_check[i] = True
                elif i == 3 and adj_node in {'-', '+', '3', '4'}:
                    dir_check[i] = True
        if all(dir_check):
            ret = '+'
        elif dir_check[0] and dir_check[1]:
            ret = '|'
        elif dir_check[2] and dir_check[3]:
            ret = '-'
        elif dir_check[1] and dir_check[3]:
            ret = '1'
        elif dir_check[0] and dir_check[3]:
            ret = '2'
        elif dir_check[0] and dir_check[2]:
            ret = '3'
        elif dir_check[1] and dir_check[2]:
            ret = '4'
        return ret

    def find_direction(s: str, direction: int) -> int:
        # 상 하
        if s == '|' and (direction == 0 or direction == 1):
            return direction
        # 좌 우
        elif s == '-' and (direction == 2 or direction == 3):
            return direction
        # 상 하 좌 우
        elif s == '+':
            return direction
        # 하 우
        elif s == '1':
            if direction == 0:
                return 3
            elif direction == 2:
                return 1
        # 상 우
        elif s == '2':
            if direction == 2:
                return 0
            elif direction == 1:
                return 3
        # 상 좌
        elif s == '3':
            if direction == 3:
                return 0
            elif direction == 1:
                return 2
        # 하 좌
        elif s == '4':
            if direction == 3:
                return 1
            elif direction == 0:
                return 2
        return -1

    def is_valid(x: int, y: int) -> bool:
        return 0 <= x < row and 0 <= y < col

    graph = [list(input().rstrip()) for _ in range(row)]
    # print(graph)
    # 상 하 좌 우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    start_x, start_y = 0, 0
    for i in range(row):
        for j in range(col):
            if graph[i][j] == 'M':
                start_x, start_y = i, j
                break
    dfs(start_x, start_y)


input = sys.stdin.readline
row, col = map(int, input().split())
solution(row, col)