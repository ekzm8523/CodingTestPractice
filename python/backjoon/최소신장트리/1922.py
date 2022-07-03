"""
https://www.acmicpc.net/problem/1922
최소신장트리 : Minimum Spanning Tree
N개의 노드를 N-1개의 노드로 연결하도록 만드면서 가중치의 합이 최소가 되게 만드는 트리
MST의 두 가지 방법
1. 크루스칼 알고리즘
2. 프림 알고리즘

크루스칼 알고리즘은 정렬시키는데 nlogn 이고 사이클 확인을 위한 union find는 무시해도 되기 때문에 결과론적으로 시간복잡도는 nlogn
프림 알고리즘은 n개의 노드를 선택해야하고 연결된 노드들중에서 가장 weight가 작은 노드를 연결해야 한다.
가장 작은 노드를 찾는걸 heap으로 사용한다고 치면 이 또한 nlogn

보통 크루스칼은 희소 그래프의 MST를 찾는데 적합하고 프림은 밀집 그래프의 MST를 찾는데 적합하다.

둘 다 구현해봤을때 크루스칼이 확실히 빨랐다.
아무래도 매번 heapq에 넣고 빼는 것 보다는 처음에 sorting을 하고 select하는게 좀 더 효율적이기 때문인 것 같다.
"""

import sys
from heapq import heappop as pop, heappush as push
input = lambda: sys.stdin.readline().strip()


def union(parents: list, a: int, b: int) -> None:
    a, b = find_parent(parents, a), find_parent(parents, b)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b


def find_parent(parents: list, num: int) -> int:
    if num != parents[num]:
        parents[num] = find_parent(parents, parents[num])
    return parents[num]


def is_cycle(parents: list, a: int, b: int) -> bool:
    return find_parent(parents, a) == find_parent(parents, b)


def kruskal(edges: list):
    edges = sorted(edges, key=lambda edge: edge[2])
    parents = [i for i in range(node_count + 1)]
    total_weight = 0
    size = 0

    for a, b, w in edges:
        if is_cycle(parents, a, b):
            continue

        union(parents, a, b)
        total_weight += w
        size += 1
        if size == node_count - 1:
            break

    return total_weight


def prim(edges: list):

    hq = []
    node_set = set()
    node_set.add(1)
    total_weight = 0
    graph = [[] for _ in range(node_count + 1)]

    for a, b, w in edges:
        graph[a].append((b, w))
        graph[b].append((a, w))

    for b, w in graph[1]:
        push(hq, (w, b))

    while hq:
        weight, next_node = pop(hq)
        if next_node not in node_set:
            node_set.add(next_node)
            total_weight += weight
            for b, w in graph[next_node]:
                push(hq, (w, b))
        if len(node_set) == node_count:
            break
    return total_weight


if __name__ == '__main__':
    node_count = int(input())
    edge_count = int(input())
    edges = []
    for _ in range(edge_count):
        u, v, w = map(int, input().split())  # u와 v는 같을 수 있다.
        if u == v:
            continue
        edges.append((u, v, w))

    print(kruskal(edges))
    print(prim(edges))


