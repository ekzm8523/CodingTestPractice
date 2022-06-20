# https://www.acmicpc.net/problem/13913
import sys
from collections import deque

input = lambda: sys.stdin.readline().strip()
INF = 100001

if __name__ == '__main__':
    sys.setrecursionlimit(10000)
    distances = [INF] * INF
    move = [-1] * INF
    subin_pos, sister_pos = map(int, input().split())

    q = deque()
    q.append(subin_pos)
    distances[subin_pos] = 0

    while q:
        pos = q.popleft()
        dis = distances[pos]
        if pos == sister_pos:
            break
        for next_pos in (pos + 1, pos - 1, pos * 2):
            if 0 <= next_pos < INF and distances[next_pos] == INF:
                distances[next_pos] = dis + 1
                move[next_pos] = pos
                q.append(next_pos)

    print(dis)
    path = [pos]
    while pos != subin_pos:
        pos = move[pos]
        path.append(pos)
    path.reverse()

    print(*path)


