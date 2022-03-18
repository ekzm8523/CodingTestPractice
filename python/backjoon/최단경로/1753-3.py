# https://www.acmicpc.net/problem/1753
import sys
import math
from heapq import heappush as push, heappop as pop

input = lambda: sys.stdin.readline().rstrip()


def dijkstra():
    global graph, start_node, node_cnt

    dp = [math.inf] * (node_cnt + 1)  # 1번부터 시작
    dp[start_node] = 0
    hq = []
    visit = [False] * (node_cnt + 1)
    push(hq, (0, start_node))

    while hq:
        weight, node = pop(hq)
        if visit[node]:
            continue
        visit[node] = True
        if node not in graph:
            continue
        for key in graph[node]:
            new_weight = weight + graph[node][key]

            if dp[key] > new_weight:
                dp[key] = new_weight
                push(hq, (new_weight, key))

    for value in dp[1:]:
        print(value if value != math.inf else "INF", end=" ")


if __name__ == "__main__":
    node_cnt, edge_cnt = map(int, input().split())

    start_node = int(input())

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


    dijkstra()

