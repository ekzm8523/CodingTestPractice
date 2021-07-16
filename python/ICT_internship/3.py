
from collections import deque

def reachTheEnd(grid, maxTime):
    col_size = len(grid[0])
    row_size = len(grid)
    dx = [-1, 0, 1 ,0]
    dy = [0, 1, 0, -1] # 동 서 남 북
    table = [[0] * col_size for _ in range(row_size)]

    q = deque()
    q.append((0, 0, 0))
    table[0][0] = 1
    while q:
        x, y, time = q.popleft()
        if x == row_size and y == col_size:
            break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= row_size or ny < 0 or ny >= col_size:
                continue

            if table[nx][ny] == 0 and grid[nx][ny] == '.':
                table[nx][ny] = time + 1
                q.append((nx, ny, time + 1))

    if maxTime < table[-1][-1] or table[-1][-1] == 0:
        return "No"
    return "Yes"





if __name__ == "__main__":
    grid = ['.']
    max_time = 5
    print(reachTheEnd(grid, max_time))