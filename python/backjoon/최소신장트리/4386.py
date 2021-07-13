# https://www.acmicpc.net/problem/4386
"""
전체 별들을 잇는다면 밀집 그래프가 되기 때문에 Prim MST 알고리즘을 사
"""
import math
import sys
import heapq

def calc_distance(A, B):
    x = A[0] - B[0]
    y = A[1] - B[1]
    return round(math.sqrt(x * x + y * y), 2)

# if __name__ == "__main__":
#     n = int(input())
#
#     node_positions = [list(map(float, input().split())) for _ in range(n)]
#
#     remain_node = set(range(1, n))
#     sum_distance = current_node = 0
#
#     for i in range(n - 1):
#         min_node, min_distance = -1, sys.maxsize
#         for node in remain_node:
#             dist = calc_distance(node_positions[current_node], node_positions[node])
#             if min_distance > dist:
#                 min_node = node
#                 min_distance = dist
#
#             print(f"{current_node} to {node} distance -> {dist}")
#         print(f"select min_node {min_node}")
#         current_node = min_node
#         remain_node.remove(min_node)
#         sum_distance += min_distance
#     print(sum_distance)


if __name__ == "__main__":
    n = int(input())
    node_positions = [list(map(float, input().split())) for _ in range(n)]
    graph = [[] for _ in range(n)]

    for i in range(n - 1):
        for j in range(i + 1, n):
            dis = calc_distance(node_positions[i], node_positions[j])
            graph[i].append([dis, j])
            graph[j].append([dis, i])

    hq = []
    heapq.heappush(hq, [0, 0])

    sum_distance = 0
    check = [False] * n
    while hq:
        dis, end = heapq.heappop(hq)
        if check[end]:
            continue
        sum_distance += dis
        check[end] = True
        for dis, end in graph[end]:
            heapq.heappush(hq, [dis, end])

    print(sum_distance)