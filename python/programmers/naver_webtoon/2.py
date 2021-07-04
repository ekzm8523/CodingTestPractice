from collections import deque

INF = int(1e9)
def solution(grid):
    answer = 0
    h = len(grid)
    w = len(grid[0])
    move = [[1, 0], [0, 1]]  # move right, move left

    q = deque()
    q.append((0, 0))
    dp_table = [[INF] * w for _ in range(h)]
    dp_table[0][0] = grid[0][0]

    while q:
        x, y = q.popleft()
        for i in range(2):
            dx, dy = move[i]
            nx = x + dx
            ny = y + dy
            if nx < h and ny < w:
                if dp_table[nx][ny] > dp_table[x][y] + grid[nx][ny]:
                    dp_table[nx][ny] = dp_table[x][y] + grid[nx][ny]
                    q.append((nx, ny))

    return dp_table[-1][-1]


if __name__ == "__main__":
    grid = [[1, 2], [3, 4]]
    print(solution(grid))
    grid = [[1, 8, 3, 2], [7, 4, 6, 5]]
    print(solution(grid))
