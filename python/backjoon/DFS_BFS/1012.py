# https://www.acmicpc.net/problem/1012
from collections import deque


def bfs(cabbage_field: list, start: tuple, visit: set):
    q = deque()
    q.append(start)
    visit.add(start)

    while q:
        x, y = q.popleft()  # x : vertical, y : width

        for dx, dy in move:
            nx, ny = dx + x, dy + y
            if 0 <= nx < vertical_size and 0 <= ny < width_size and cabbage_field[nx][ny] and not (nx, ny) in visit:
                q.append((nx, ny))
                visit.add((nx, ny))


if __name__ == '__main__':
    test_count = int(input())
    move = ((-1, 0), (0, 1), (1, 0), (0, -1))  # 시계방향

    for _ in range(test_count):
        width_size, vertical_size, cabbage_count = map(int, input().split())
        cabbage_field = [[0 for _ in range(width_size)] for _ in range(vertical_size)]
        cabbage_pos = []
        for _ in range(cabbage_count):
            width, vertical = map(int, input().split())
            cabbage_field[vertical][width] = 1
            cabbage_pos.append((vertical, width))

        worm_count = 0
        visit = set()
        for start in cabbage_pos:

            if start not in visit:
                bfs(cabbage_field, start, visit)
                worm_count += 1
        print(worm_count)

