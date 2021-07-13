# https://www.acmicpc.net/problem/2206

# import sys
#
# move = [[-1, 0], [0, 1], [1, 0], [0, -1]]

# def dfs(x, y, depth, flag):
#     global answer, cnt
#
#     if table[x][y] > depth:
#         table[x][y] = depth
#     elif not flag:
#         return
#
#     if x == N-1 and y == M-1:
#         if answer > depth:
#             answer = depth
#         return
#
#
#     for i in range(4):
#         dx, dy = move[i]
#         nx = x + dx
#         ny = y + dy
#         if nx < 0 or nx >= N or ny < 0 or ny >= M:
#             continue
#         if matrix[nx][ny] == '1':
#             if flag:
#                 visit[nx][ny] = True
#                 dfs(nx, ny, depth + 1, False)
#                 visit[nx][ny] = False
#                 continue
#         elif not visit[nx][ny]:
#             visit[nx][ny] = True
#             dfs(nx, ny, depth + 1, flag)
#             visit[nx][ny] = False


from collections import deque
import sys

move = [[-1, 0], [0, 1], [1, 0], [0, -1]]

if __name__ == "__main__":

    N, M = map(int, sys.stdin.readline().split())
    matrix = [sys.stdin.readline().strip() for _ in range(N)]

    def bfs():
        q = deque()
        q.append((0, 0, 1)) # x, y, use_skill
        visit = [[[0, 0] for _ in range(M)] for _ in range(N)]
        visit[0][0][1] = 1

        while q:
            x, y, skill = q.popleft()

            if x == N-1 and y == M-1:
                return visit[x][y][skill]

            for i in range(4):
                nx, ny = x + move[i][0], y + move[i][1]

                if 0 > nx or N <= nx or 0 > ny or M <= ny:
                    continue

                if matrix[nx][ny] == "1":
                    if skill == 1:
                        visit[nx][ny][0] = visit[x][y][1] + 1
                        q.append((nx, ny, 0))
                elif visit[nx][ny][skill] == 0:   # 벽이 아닐때 여기서 중복 방문 안막으면 메모리 초과 뜬다
                    visit[nx][ny][skill] = visit[x][y][skill] + 1
                    q.append((nx, ny, skill))

        return -1
    print(bfs())
    # sys.setrecursionlimit(int(1e9))
    # dfs(0, 0, 0, True)
    # if table[-1][-1] == sys.maxsize:
    #     print(-1)
    # else:
    #     print(table[-1][-1] + 1)
