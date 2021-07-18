# https://www.acmicpc.net/problem/2931

from collections import deque

dx = [-1, 0, 1, 0] # 시계 방향 12 -> 3 -> 6 -> 9
dy = [0, 1, 0, -1]

def code2direction(ch):

    if ch == '.':
        return None
    elif ch == '|':
        return [0, 2]
    elif ch == '-':
        return [1, 3]
    elif ch == '+' or ch == 'M' or ch == 'Z':
        return [0, 1, 2, 3]
    elif ch == '1':
        return [1, 2]
    elif ch == '2':
        return [0, 1]
    elif ch == '3':
        return [0, 3]
    elif ch == '4':
        return [2, 3]

def direction2code(dir):
    dir.sort()
    if dir == [0, 2]:
        return '|'
    elif dir == [1, 3]:
        return '-'
    elif dir == [0, 1, 2, 3]:
        return '+'
    elif dir == [1, 2]:
        return '1'
    elif dir == [0, 1]:
        return '2'
    elif dir == [0, 3]:
        return '3'
    elif dir == [2, 3]:
        return '4'
    else:
        return f'what is {dir}'

def solution(table, R, C):

    def bfs(start, end):

        q = deque()
        mx, my = start
        zx, zy = end
        visit = [[False] * C for _ in range(R)]
        visit[mx][my] = visit[zx][zy] = True

        for i in range(4):
            nx = mx + dx[i]
            ny = my + dy[i]
            if nx < 0 or nx >= R or ny < 0 or ny >= C:
                continue
            if table[nx][ny] != '.':
                q.append((nx, ny, table[nx][ny]))
                visit[nx][ny] = True

        for i in range(4):
            nx = zx + dx[i]
            ny = zy + dy[i]
            if nx < 0 or nx >= R or ny < 0 or ny >= C:
                continue
            if table[nx][ny] != '.':
                q.append((nx, ny, table[nx][ny]))
                visit[nx][ny] = True
        target = [None, None, []]
        while q:
            x, y, ch = q.popleft()
            move = code2direction(ch)
            for i in move:
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx >= R or ny < 0 or ny >= C:
                    continue
                if table[nx][ny] == '.':
                    if table[x][y] == 'M' or table[x][y] == 'Z':
                        continue
                    if not target[0] and not target[1]:
                        target[0] = nx
                        target[1] = ny
                    target_dir = (i + 2) % 4
                    if not target_dir in target[2]:
                        target[2].append(target_dir)   # i == 0 -> 2, 1 -> 3, 2 -> 0, 3 -> 1
                elif not visit[nx][ny]:
                    q.append((nx, ny, table[nx][ny]))
                    visit[nx][ny] = True

        print(target[0] + 1, target[1] + 1, direction2code(target[2]))
    for row in range(R):
        m = table[row].find('M')
        z = table[row].find('Z')
        if m != -1:
            start = (row, m)
        if z != -1:
            end = (row, z)

    bfs(start, end)


if __name__ == "__main__":

    R, C = map(int, input().split())

    table = [input() for _ in range(R)]

    solution(table, R, C)