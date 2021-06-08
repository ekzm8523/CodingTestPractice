
from collections import deque

def bfs(graph, start, visited):

    dq = deque([start])
    visited[start] = True
    while dq:
        next = dq.popleft()
        (next, end=' ')
        for i in graph[next]:
            if not visited[i]:
                dq.append(i)
                visited[i] = True

graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,5],
    [7],
    [2,6,8],
    [1,7]
]

visited = [False] * 9

bfs(graph, 1, visited)

