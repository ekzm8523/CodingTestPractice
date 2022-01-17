"""
쿼리가 일단 30만개라서 쿼리의 중복을 없애는게 관건
그리고 W*H가 20만갠데 쿼리가 30만개라는건 중복명령이 무조건 있다는거 -> using cache
전체 m의 합도 30만개이다. -> maximum bfs를 30만번 실행 시킬 수 있다.

12번에서 시간초과 나는건 분명 20만개의 Cell과 30만개의 Query에서 Timeout이 뜰것 이다.

bfs의 퍼저나가는 습성때문에 왼쪽상단과 오른쪽 하단으로 찾으면 전체 탐색을 해야한다. -> bidirection search
하지만 bidirection search는 정확한 목표 위치가 있어야 하고 길을 찾는 문제에서 활용이 되는 것 같은데 목표 위치를 어떻게 알지?

DP를 이용한다면?
DP[x][y][num]으로 만들면?

"""

import sys
from collections import deque

move = ((0, -1), (1, 0), (0, 1), (-1, 0))  # 시계방향

#
# def in_cache(func):
#     cache = {}
#
#     def wrapper(pos: tuple, num: str) -> int:
#         key = f"{pos[0]} {pos[1]} " + num
#         if key in cache:
#             return cache[key]
#         else:
#             cache[key] = func(pos, num)
#             return cache[key]
#
#     return wrapper


def bfs(pos: tuple, num: str, dp: list) -> int:
    global keypad, W, H
    if keypad[pos[1]][pos[0]] == num:
        return 0
    q = deque()
    q.append((*pos, 0))
    visit = set()
    visit.add(pos)
    min_distance = sys.maxsize
    while q:
        x, y, distance = q.popleft()
        dp[x][y][int(num)] = min()
        for dx, dy in move:
            nx, ny = dx + x, dy + y
            if 0 <= nx < W and 0 <= ny < H and (nx, ny) not in visit:
                if keypad[ny][nx] == num:
                    return distance + 1
                visit.add((nx, ny))
                q.append((nx, ny, distance + 1))
    return min_distance


if __name__ == '__main__':

    W, H = map(int, sys.stdin.readline().split())
    cache = cached_bfs.__closure__[0].cell_contents
    keypad = []
    for i in range(H):
        keypad.append(sys.stdin.readline().strip())

    dp = [[[0] * 9 for _ in range(H)] for _ in range(W)]

    T = int(sys.stdin.readline())
    for _ in range(T):
        answer = []
        line = sys.stdin.readline().split()
        x = int(line[0])
        y = int(line[1])
        _ = int(line[2])
        nums = line[3]
        for num in nums:
            distance = bfs((x - 1, y - 1), dp)

            answer.append(distance)
        print(*answer)