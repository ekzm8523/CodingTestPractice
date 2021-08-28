
from collections import deque
import sys

if __name__ == "__main__":
    input = sys.stdin.readline

    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]

    r, c = map(int, input().split())
    s = []
    w, q = deque(), deque()

    visit = [[0] * c for _ in range(r)]

    def bfs():
        while q or w:
            temp1 = []
            temp2 = []
            while q:
                x, y = q.popleft()
                if s[x][y] != '*':
                    for i in range(4):
                        nx = x + dx[i]
                        ny = y + dy[i]
                        if 0 <= nx < r and 0 <= ny < c and visit[nx][ny] == 0 and s[nx][ny] != "X" and s[nx][ny] != "*":
                            s[nx][ny] = s[x][y] + 1
                            visit[nx][ny] = 1
                            temp1.append([nx, ny])
            while w:
                x, y = w.popleft()
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if nx == d[0] and ny == d[1]:
                        continue
                    if 0 <= nx < r and 0 <= ny < c and s[nx][ny] != "*" and s[nx][ny] != "X":
                        s[nx][ny] = "*"
                        temp2.append([nx, ny])

            for i in temp1:
                q.append(i)
            for i in temp2:
                w.append(i)


    for i in range(r):
        a = list(input().strip())
        s.append(a)
        for j in range(c):

            if a[j] == "S":
                q.append([i, j])
                visit[i][j] = 1
                s[i][j] = 0
            elif a[j] == "*":
                w.append([i, j])
            elif a[j] == "D":
                d = [i, j]

    bfs()
    result = s[d[0]][d[1]]
    print(result if result != "D" else "KAKTUS")