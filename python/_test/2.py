import functools
import sys
from collections import deque

move = ((0, -1), (1, 0), (0, 1), (-1, 0))  # 시계방향


# def in_cache(func):
#     cache = {}
#     def wrapper(pos: tuple, num: str) -> int:
#         key = f"{pos[0]} {pos[1]} " + num
#         if key in cache:
#             return cache[key]
#         else:
#             cache[key] = func(pos, num)
#             return cache[key]
#     return wrapper





if __name__ == '__main__':

    W, H = map(int, sys.stdin.readline().split())
    keypad = []
    for i in range(H):
        keypad.append(sys.stdin.readline().strip())


    def bfs(pos: tuple, num: str, cache: dict) -> int:
        if keypad[pos[1]][pos[0]] == num:
            return 0
        key = f'{pos[0]} {pos[1]} ' + num
        if key in cache:
            return cache[key]

        q = deque()
        q.append((*pos, 0))
        visit = set()
        visit.add(pos)

        min_distance = sys.maxsize
        end = False
        while q:
            x, y, distance = q.popleft()
            current_key = f'{pos[0]} {pos[1]} ' + keypad[y][x]
            if current_key not in cache:
                cache[current_key] = distance

            answer_key = f'{x} {y} ' + num
            if answer_key in cache:
                min_distance = min(min_distance, distance + cache[answer_key])
                continue
            for dx, dy in move:
                nx, ny = dx + x, dy + y
                if 0 <= nx < W and 0 <= ny < H and (nx, ny) not in visit:
                    if keypad[ny][nx] == num:
                        min_distance, end = distance + 1, True
                        break
                    visit.add((nx, ny))
                    q.append((nx, ny, distance + 1))

            if end:
                break
        return min_distance

    T = int(sys.stdin.readline())
    cache = {}
    for _ in range(T):
        answer = []
        line = sys.stdin.readline().split()
        x = int(line[0])
        y = int(line[1])
        _ = int(line[2])
        nums = line[3]

        for num in nums:
            answer.append(bfs((x-1, y-1), num, cache))

        print(*answer)