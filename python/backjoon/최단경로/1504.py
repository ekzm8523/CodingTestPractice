# https://www.acmicpc.net/problem/1504

"""
1번 정점에서 N번 정점으로 이동할 때 주어진 두 정점을 반드시 거치면서 최단 경로로 이동하는 프로그램을 작성하라
한번 이동했던 정점, 간점도 다시 이동할 수 있다.
하지만 최단경로여야 함
다익스트라를 3번 하면 된다.
"""

import sys, heapq
from collections import deque


if __name__ == "__main__":
    N, E = map(int, sys.stdin.readline().split())
    edges = [[] for _ in range(N + 1)]
    for _ in range(E):
        a, b, c = map(int, sys.stdin.readline().split())
        edges[a].append((b, c))
        edges[b].append((a, c))

    def bfs(start, end):
        table = [sys.maxsize for _ in range(N + 1)]
        hq = []
        table[start] = 0
        heapq.heappush(hq, (table[start], start))

        while hq:
            step_dis, current_node = heapq.heappop(hq)
            if table[current_node] < step_dis:  # 이미 방문했던 노드면 패스
                continue

            for node, dis in edges[current_node]:
                if table[node] > step_dis + dis:
                    table[node] = step_dis + dis
                    heapq.heappush(hq, (table[node], node))

        return table[end]

    v1, v2 = map(int, sys.stdin.readline().split())
    answer = []
    answer.append(bfs(1, v1) + bfs(v1, v2) + bfs(v2, N))
    answer.append(bfs(1, v2) + bfs(v2, v1) + bfs(v1, N))

    if max(answer) > sys.maxsize:
        print(-1)
    else:
        print(min(answer))

