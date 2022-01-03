# https://www.acmicpc.net/problem/1260
from collections import deque


def dfs(graph, remain_node, current_node):
    print(current_node, end=' ')
    remain_node.remove(current_node)
    if not remain_node or current_node not in graph:
        return

    for next_node in graph[current_node]:
        if next_node in remain_node:
            dfs(graph, remain_node, next_node)


def bfs(graph, remain_node, start_node):
    q = deque()
    q.append(start_node)
    remain_node.remove(start_node)
    while q:
        current_node = q.popleft()
        print(current_node, end=' ')
        if current_node in graph:
            for next_node in graph[current_node]:
                if next_node in remain_node:
                    q.append(next_node)
                    remain_node.remove(next_node)



if __name__ == '__main__':
    node_count, edge_count, start_node = map(int, input().split())  # node count, edge count, start node number
    edges = [tuple(map(int, input().split()))for _ in range(edge_count)]
    graph = {}
    for x, y in edges:
        if x not in graph:
            graph[x] = []
        if y not in graph:
            graph[y] = []
        graph[x].append(y)
        graph[y].append(x)

    for key in graph:
        graph[key].sort()
    remain_node = set(range(1, node_count+1))
    dfs(graph, remain_node, start_node)
    print()
    remain_node = set(range(1, node_count+1))
    bfs(graph, remain_node, start_node)
