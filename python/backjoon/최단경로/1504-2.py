import math
import sys
from heapq import heappop as pop, heappush as push
input = lambda: sys.stdin.readline()


def dijkstra(start, end):
    global graph, node_cnt

    dp = [math.inf] * (node_cnt + 1)
    dp[start] = 0

    hq = []
    visit = [False] * (node_cnt + 1)
    push(hq, (0, start))

    while hq:
        weight, node = pop(hq)

        if visit[node]:
            continue
        visit[node] = True
        if node not in graph:
            continue

        for key in graph[node]:
            new_weight = dp[node] + graph[node][key]
            if dp[key] > new_weight:
                dp[key] = new_weight
                push(hq, (new_weight, key))

    return dp[end]

if __name__ == "__main__":
    node_cnt, edge_cnt = map(int, input().split())

    graph = {}
    for _ in range(edge_cnt):
        u, v, w = map(int, input().split())

        if u not in graph:
            graph[u] = {}

        if v not in graph:
            graph[v] = {}

        if v not in graph[u]:
            graph[u][v] = {}
        else:
            w = min(graph[u][v], w)

        if u not in graph[v]:
            graph[v][u] = {}
        else:
            w = min(graph[u][v], w)
        graph[u][v] = graph[v][u] = w

    a, b = map(int, input().split())

    path_1 = dijkstra(1, a) + dijkstra(a, b) + dijkstra(b, node_cnt)
    path_2 = dijkstra(1, b) + dijkstra(b, a) + dijkstra(a, node_cnt)
    answer = min(path_1, path_2)
    print(answer if answer != math.inf else -1)