# https://www.acmicpc.net/problem/2252

import sys
from collections import deque

if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().split())

    in_degree = [0] * (N + 1)
    graph = [[] for _ in range(N + 1)]
    for _ in range(M):
        A, B = map(int, sys.stdin.readline().split())
        in_degree[B] += 1
        graph[A].append(B)

    q = deque()

    for i in range(1, N+1):
        if in_degree[i] == 0:
            q.append(i)
    answer = []
    while q:
        current_node = q.popleft()
        print(current_node, end=" ")
        for node in graph[current_node]:
            in_degree[node] -= 1
            if in_degree[node] == 0:
                q.append(node)
