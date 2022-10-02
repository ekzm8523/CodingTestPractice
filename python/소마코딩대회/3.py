import sys
from collections import deque
import math
from pprint import pprint
input = lambda: sys.stdin.readline().strip()

RIGHT, DOWN = 0, 1
move = ((0, 1), (1, 0))


def main():
    n, m = map(int, input().split())
    table = tuple(tuple(map(int, input().split())) for _ in range(n))
    dp = [[-math.inf] * m for _ in range(n)]
    wall = tuple(map(int, input().split()))

    cant_move = set()
    if wall[0] != wall[2] or wall[1] != wall[3]:
        if wall[0] == wall[2]:  # 가로 방향
            for col in range(wall[1], wall[3]):
                cant_move.add(((wall[0] - 1, col), DOWN))
                # cant_move.add(((wall[0], col), UP))
        elif wall[1] == wall[3]:  # 세로 방향
            for row in range(wall[0], wall[2]):
                cant_move.add(((row, wall[1] - 1), RIGHT))
                # cant_move.add(((row, wall[1]), LEFT))
        else:
            raise Exception("잘못된 설계")
    dp[0][0] = table[0][0]
    q = deque()
    q.append((0, 0, dp[0][0]))
    while q:
        x, y, w = q.popleft()
        if w < dp[x][y]:
            continue
        for direction, (dx, dy) in enumerate(move):
            if ((x, y), direction) not in cant_move:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m and w + table[nx][ny] > dp[nx][ny]:
                    dp[nx][ny] = w + table[nx][ny]
                    q.append((nx, ny, dp[nx][ny]))
    print(dp[-1][-1] if dp[-1][-1] != -math.inf else "Entity")


if __name__ == '__main__':
    main()

"""
4 4
1 2 8 7
3 2 1 4
7 8 2 1
2 6 2 1

0 3 3 3
"""