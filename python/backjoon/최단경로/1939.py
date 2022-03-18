# https://www.acmicpc.net/problem/1939
import sys
import math
from collections import deque


input = lambda: sys.stdin.readline().rstrip()


def bfs(weight):
    global graph, node_cnt, start, end

    q = deque()
    q.append(start)
    visit = [False] * (node_cnt + 1)
    visit[start] = True
    while q:
        node = q.popleft()

        if node not in graph:
            continue

        for key in graph[node]:
            if graph[node][key] >= weight and visit[key] is False:
                visit[key] = True
                q.append(key)

    return visit[end]



if __name__ == "__main__":
    node_cnt, edge_cnt = map(int, input().split())

    graph = {}
    max_weight = 0
    for _ in range(edge_cnt):
        u, v, w = map(int, input().split())

        if u not in graph:
            graph[u] = {}

        if v not in graph:
            graph[v] = {}

        if v not in graph[u]:
            graph[u][v] = {}
        else:
            w = max(w, graph[u][v])

        if u not in graph[v]:
            graph[v][u] = {}
        else:
            w = max(w, graph[v][u])
        max_weight = max(w, max_weight)
        graph[u][v] = graph[v][u] = w

    start, end = map(int, input().split())
    l, r = 1, max_weight
    answer = 0
    while l <= r:
        mid = (l + r) // 2

        if bfs(mid):
            l = mid + 1
            answer = mid
        else:
            r = mid - 1

    print(answer)
