# https://www.acmicpc.net/problem/3055
"""
'.' : 비어있음
'*' : 물이 차있음
'X' : 돌
'D' : 비버의 굴
'S' : 고슴도치의 위치

"""

from collections import deque

def move_water(wq):
    cycle = len(wq)
    for _ in range(cycle):
        x, y = wq.popleft()
        for dx, dy in move:
            nx, ny = x + dx, y + dy
            if 0 <= nx < R and 0 <= ny < C:
                if table[nx][ny] == ".":
                    table[nx][ny] = '*'
                    wq.append((nx, ny))

def move_hedgehog(q, depth):
    cycle = len(q)
    for _ in range(cycle):
        x, y = q.popleft()

        for dx, dy in move:
            nx, ny = x + dx, y + dy
            if 0 <= nx < R and 0 <= ny < C:
                if visit[nx][ny] or table[nx][ny] == 'X' or table[nx][ny] == '*':
                    continue
                if table[nx][ny] == 'D':
                    return depth
                q.append((nx, ny))
                visit[nx][ny] = True
    return 0


if __name__ == "__main__":
    R, C = map(int, input().split())
    move = [[-1, 0], [0, 1], [1, 0], [0, -1]] # 시계방향 moving
    table = [list(map(str, input())) for _ in range(R)]
    s_pos = []
    w_pos = []
    for i in range(R):
        for j in range(C):
            if table[i][j] == 'S':
                s_pos = [i, j]
            elif table[i][j] == '*':
                w_pos = [i, j]

    visit = [[False] * C for _ in range(R)]

    def bfs(hedgehog_pos, water_pos):
        x, y = hedgehog_pos
        visit[x][y] = True
        q, wq = deque(), deque()
        q.append((x, y))
        wq.append(water_pos)
        depth = 0
        while q:
            depth += 1
            move_water(wq)
            result = move_hedgehog(q, depth)

            if result != 0:
                print(result)
                return
        print("KAKTUS")
    bfs(s_pos, w_pos)

