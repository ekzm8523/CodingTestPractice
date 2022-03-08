import sys
from heapq import heappop as pop, heappush as push

if __name__ == "__main__":

    node_count, edge_count = map(int, input().split())
    start_node = int(input())
    graph = {i: {} for i in range(1, node_count + 1)}

    for _ in range(edge_count):
        u, v, w = map(int, input().split())
        if v in graph[u]:
            graph[u][v] = min(graph[u][v], w)
        else:
            graph[u][v] = w

    table = [sys.maxsize] * (node_count + 1)
    table[start_node] = 0
    visit = [False] * (node_count + 1)

    hq = [(0, start_node)]

    while hq:
        current_distance, current_node = pop(hq)
        if visit[current_node]:
            continue
        visit[current_node] = True

        # if current_node in graph:
        for next_node, distance in graph[current_node].items():
            if visit[next_node] is False:
                table[next_node] = min(table[next_node], current_distance + distance)
                push(hq, (table[next_node], next_node))

    for distance in table[1:]:
        print(distance if distance < sys.maxsize else "INF")


"""
5 6
2
5 1 1
5 1 2
1 3 3
2 3 4
2 4 5
3 4 1
"""