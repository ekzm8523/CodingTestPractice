# https://www.acmicpc.net/problem/11779
import sys
import math
from heapq import heappush as push, heappop as pop

input = lambda: sys.stdin.readline().rstrip()


def dijkstra():
    global graph, node_cnt, start, end

    dp = [math.inf] * (node_cnt + 1)
    path = [0] * (node_cnt + 1)
    dp[start] = 0
    visit = [False] * (node_cnt + 1)

    hq = [(0, start)]

    while hq:
        weight, node = pop(hq)
        if visit[node]:
            continue

        visit[node] = True

        if node not in graph:
            continue

        for key in graph[node]:
            new_weight = weight + graph[node][key]
            if new_weight < dp[key]:
                path[key] = node
                dp[key] = new_weight
                push(hq, (new_weight, key))
    print(dp[end])
    idx = end
    min_path = []
    while idx != 0:
        min_path.append(idx)
        idx = path[idx]

    print(len(min_path))
    print(*reversed(min_path))


if __name__ == "__main__":
    node_cnt = int(input())
    edge_cnt = int(input())

    graph = {}
    for _ in range(edge_cnt):
        u, v, w = map(int, input().split())

        if u not in graph:
            graph[u] = {}

        if v not in graph[u]:
            graph[u][v] = {}
        else:
            w = min(w, graph[u][v])

        graph[u][v] = w
    start, end = map(int, input().split())
    dijkstra()

