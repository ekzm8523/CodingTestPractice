from collections import deque

if __name__ == "__main__":
    N, M = map(int, input().split())

    graph = [[] for _ in range(N+1)]
    for i in range(M):
        A, B, W = map(int, input().split())
        graph[A].append((B, W))
        graph[B].append((A, W))

    start, end = map(int, input().split())

    def bfs(product_weight):

        visit = set([start])
        q = deque([start])

        while q:
            current_node = q.popleft()
            for next_node, weight in graph[current_node]:
                if next_node not in visit and weight >= product_weight:
                    q.append(next_node)
                    visit.add(next_node)
                    if next_node == end:
                        return True
        return False

    left = 0
    right = 1e9
    max_weight = 0

    while left <= right:
        mid = (left + right) // 2

        if bfs(mid):
            max_weight = max(max_weight, mid)
            left = mid + 1
        else:
            right = mid - 1

    print(int(max_weight))