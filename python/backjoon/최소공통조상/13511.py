'''
https://www.acmicpc.net/problem/13511
6 -> node count
1 2 1  -> a, b, w
2 4 1
2 5 2
1 3 1
3 6 2
2 -> query count
1 4 6  -> q, a, b
2 4 6 4  -> q, a, b, c
if query is 1
-> a에서 b까지의 weight 계산해서 출력
if query is 2
-> a에서 b까지의 경로중 c번째 노드 출력
-> c를 1 빼줌 : c번째 노드라는건 c - 1칸만큼 움직이라는 뜻으로 이해하기 위해 c를 1만큼 빼준다
-> a, b의 LCA(Lowest Common Ancestor)을 구한다.
-> a에서 LCA까지의 거리를 a_depth라고 정의
-> if a_depth <= c
    -> a에서 c번째 노드 출력
-> else
    -> c를 a_depth 만큼 빼줌 그리고 그 값을 b의 높이에서 빼면 된다.
    -> b의 (b_depth - (c - a_depth)) 번째 높이의 노드를 출력해주면 된다.

'''
import sys
from collections import deque
from math import log2
from typing import Tuple
input = lambda: sys.stdin.readline().strip()


class Node:
    def __init__(self):
        self.parents = []
        self.weights = []
        self.neighborhood = []
        self.children = []
        self.depth = None


def move_depth(node_num, up_depth) -> Tuple[int, int]:
    move_node_num, remain_depth, _weight = node_num, up_depth, 0
    while remain_depth:
        move = int(log2(remain_depth))
        remain_depth -= 2**move
        _weight += graph[move_node_num].weights[move]
        move_node_num = graph[move_node_num].parents[move]


    return move_node_num, _weight


def find_lca(u, v) -> Tuple[int, int]:
    _weight = 0
    if u == v:
        return u, 0

    while graph[u].parents[0] != graph[v].parents[0]:
        for u_p, v_p, u_w, v_w in zip(
                graph[u].parents[::-1], graph[v].parents[::-1], graph[u].weights[::-1], graph[v].weights[::-1]
        ):
            if u_p != v_p:
                u, v = u_p, v_p
                _weight += (u_w + v_w)
                break
    _weight += (graph[u].weights[0] + graph[v].weights[0])
    return graph[u].parents[0], _weight


def calculate_path_weight(u, v) -> None:
    weight = 0
    if graph[u].depth > graph[v].depth:
        u, v = v, u
    depth_dif = graph[v].depth - graph[u].depth
    if depth_dif:
        v, w = move_depth(v, depth_dif)
        weight += w
    lca, w = find_lca(u, v)
    weight += w
    print(weight)


def find_nth_node_in_path(u, v, n) -> None:
    n -= 1
    u_copy, v_copy = u, v
    if graph[u].depth > graph[v].depth:
        u, v = v, u
    depth_dif = graph[v].depth - graph[u].depth
    if depth_dif:
        v, _ = move_depth(v, depth_dif)
    lca, _ = find_lca(u, v)

    u, v = u_copy, v_copy
    u_gap = graph[u].depth - graph[lca].depth
    v_gap = graph[v].depth - graph[lca].depth
    if u_gap >= n:
        v, _ = move_depth(u, n)
        print(v)
    else:
        v, _ = move_depth(v, v_gap - (n - u_gap))
        print(v)


if __name__ == '__main__':
    node_count = int(input())
    graph = [Node() for _ in range(node_count + 1)]
    for _ in range(node_count - 1):
        a, b, w = map(int, input().split())
        graph[a].neighborhood.append((b, w))
        graph[b].neighborhood.append((a, w))

    q = deque([(1, 0)])  # (node number, depth)
    graph[1].depth = 0

    # depth init
    while q:
        node, depth = q.popleft()
        for next_node, weight in graph[node].neighborhood:
            if graph[next_node].depth is None:
                # graph[next_node].parents = [0] * int(log2(depth + 1))
                graph[next_node].parents.append(node)
                graph[next_node].weights.append(weight)
                graph[next_node].depth = depth + 1
                graph[node].children.append(next_node)
                q.append((next_node, depth + 1))

    # parents setting
    q.append(1)
    while q:
        node = q.popleft()
        for next_node in graph[node].children:
            for i in range(1, int(log2(graph[next_node].depth)) + 1):
                i_parent = graph[graph[next_node].parents[i-1]].parents[i-1]
                graph[next_node].parents.append(i_parent)
                i_weight = graph[graph[next_node].parents[i-1]].weights[i-1] + graph[next_node].weights[i-1]
                graph[next_node].weights.append(i_weight)
            q.append(next_node)

    query_count = int(input())
    for _ in range(query_count):
        row_input = tuple(map(int, input().split()))
        if row_input[0] == 1:
            calculate_path_weight(*row_input[1:])
        elif row_input[0] == 2:
            find_nth_node_in_path(*row_input[1:])


    # for node in graph:
    #     print(node.depth, node.parents, node.weights)

"""
6
1 2 1
2 4 1
2 5 2
1 3 1
3 6 2
2
1 4 3
2 4 6 4
"""