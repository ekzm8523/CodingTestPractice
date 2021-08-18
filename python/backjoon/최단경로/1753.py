# https://www.acmicpc.net/problem/1753
import sys
from collections import deque

INF = sys.maxsize

if __name__ == "__main__":
    v, e = map(int, sys.stdin.readline().split())

    start = int(sys.stdin.readline())

    graph = {i: {} for i in range(v + 1)}

    for _ in range(e):
        a, b, w = map(int, sys.stdin.readline().split())

        if b not in graph[a]:
            graph[a][b] = w
        elif graph[a][b] > w:
            graph[a][b] = w

    table = [None] + [INF] * v
    table[start] = 0
    remain_set = set(range(1, v+1))
    dq = deque()

    dq.append((start, 0))

    while dq:
        current_node, current_weight = dq.popleft()
        remain_set.remove(current_node)
        for adjacent_node in graph[current_node]:
            weight = graph[current_node][adjacent_node]
            if table[adjacent_node] > current_weight + weight:
                table[adjacent_node] = current_weight + weight
        next_node, weight = None, INF
        for remain_node in remain_set:
            if weight > table[remain_node]:
                next_node, weight = remain_node, table[remain_node]
        if next_node:
            dq.append((next_node, weight))

    for value in table[1:]:
        print("INF" if value == INF else value)
