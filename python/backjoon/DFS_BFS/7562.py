# https://www.acmicpc.net/problem/7562

from collections import deque

def bfs(length, current, destination):
    if current == destination:
        return 0

    move = [
        [1, -2], [2, -1], [2, 1], [1, 2],
        [-1, 2], [-2, 1], [-2, -1], [-1, -2],
    ]

    visited = [[False] * length for _ in range(length)]
    visited[current[0]][current[1]] = True
    cnt = 1
    q = deque()
    q.append((current[0], current[1], cnt))
    while q:
        x, y, cnt = q.popleft()

        for i in range(8):
            dx, dy = move[i]
            nx = x + dx
            ny = y + dy
            if nx < 0 or nx >= length or ny < 0 or ny >= length:
                continue

            if nx == destination[0] and ny == destination[1]:
                return cnt

            if not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny, cnt + 1))

if __name__ == "__main__":
    num_test = int(input())

    for test in range(num_test):
        length = int(input())
        current = list(map(int, input().split()))
        destination = list(map(int, input().split()))

        print(bfs(length, current, destination))
