# https://www.acmicpc.net/problem/2667

def dfs(i, j, group):
    visit[i][j] = True
    answer[group] += 1

    for dir in range(4):
        dx, dy = move[dir]
        nx = dx + i
        ny = dy + j
        if nx < 0 or nx >= N or ny < 0 or ny >= N: # out of index
            continue
        if not visit[nx][ny] and adj_list[nx][ny] == 1:
            dfs(nx, ny, group)


if __name__ == "__main__":
    N = int(input())
    adj_list = [list(map(int, input())) for _ in range(N)]
    answer = []
    visit = [[False] * N for _ in range(N)]
    move = [[0, -1], [1, 0], [0, 1], [-1, 0]]
    group = 0

    for i in range(N):
        for j in range(N):
            if not visit[i][j] and adj_list[i][j] == 1:
                answer.append(0)
                dfs(i, j, group)
                group += 1

    print(len(answer))

    for ans in sorted(answer):
        print(ans)

