# https://www.acmicpc.net/problem/2606

from collections import deque

if __name__ == "__main__":
    node_cnt = int(input())
    edge_cnt = int(input())
    edges = [[] for _ in range(node_cnt + 1)]

    for i in range(edge_cnt):
        a, b = list(map(int, input().split()))
        edges[a].append(b)
        edges[b].append(a)

    # bfs
    queue = deque()
    visit = [False] * (node_cnt + 1)
    cnt = 0
    queue.append(1)
    visit[1] = True
    while queue:
        visit_node = queue.popleft()

        for node in edges[visit_node]:
            if not visit[node]:
                visit[node] = True
                queue.append(node)
                cnt += 1

    print(cnt)