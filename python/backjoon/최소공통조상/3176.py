# https://www.acmicpc.net/problem/3176
"""
최소 공통 조상
가장 간단한 방법으로는 각각의 노드의 depth를 맞춰놓고 동시에 찾아 올라가는 방법이 있다.
하지만 이는 O(depth)라는 비효율적인 시간복잡도를 갖는다.
이를 이분 탐색을 통해 더 빠르게 구할 수 있다.
parent[x][k] = "x번 정점의 2^k번째 조상 노드의 번호"
라고 정의하면 parent[x][k] = parent[parent[x][k-1]][k-1]이 성립한다.

우린 로직을 두 가지로 나눠야 한다.
1. parent 배열을 만들어준다.
2. 두 노드 사이의 depth를 갖게 해준다.
3. parent 배열을 이분탐색으로 가장 작은 공통 부모를 찾는다.
- 2^n을 높여 봤을때 부모가 같다면 더 낮은 공통 부모는 없을까? 하고 낮추는 것

"""
import sys
from typing import Optional, List, Tuple
from math import log2
from collections import deque

input = lambda: sys.stdin.readline().strip()

class Node:
    def __init__(self, num):
        self.num: int = num
        self.depth: Optional[int] = None
        self.parents: List[int] = []
        self.parents_min_weight: List[int] = []
        self.parents_max_weight: List[int] = []
        self.neighborhood: List[Tuple] = []

    def __str__(self) -> str:
        return f"num : {self.num}"\
               f" parents : {self.parents}"\
               f" depth : {self.depth}"

    def __repr__(self) -> str:
        return f"num : {self.num}," \
               f" parents : {self.parents}"\
               f" depth : {self.depth}"


def set_depth():
    q = deque([(1, 0)])
    graph[1].depth = 0

    while q:
        current_node, depth = q.popleft()
        for next_node, weight in graph[current_node].neighborhood:
            if graph[next_node].depth is None:
                graph[next_node].depth = depth + 1
                graph[next_node].parents.append(current_node)
                graph[next_node].parents_min_weight.append(weight)
                graph[next_node].parents_max_weight.append(weight)
                q.append((next_node, depth + 1))

    for node in graph:
        if node and node.depth:
            for _ in range(int(log2(node.depth))):  # 4 -> 0, 1, 2
                node.parents.append(0)
                node.parents_min_weight.append(0)
                node.parents_max_weight.append(0)


def set_parents():

    for j in range(1, max_parents_size):
        for i in range(1, node_count + 1):
            if len(graph[i].parents) - 1 >= j:
                graph[i].parents[j] = graph[graph[i].parents[j - 1]].parents[j - 1]
                graph[i].parents_min_weight[j] = min(
                    graph[graph[i].parents[j - 1]].parents_min_weight[j - 1],
                    graph[i].parents_min_weight[j - 1]
                )
                graph[i].parents_max_weight[j] = max(
                    graph[graph[i].parents[j - 1]].parents_max_weight[j - 1],
                    graph[i].parents_max_weight[j - 1]
                )


def lca(a: int, b: int):
    _min, _max = sys.maxsize, 0
    if graph[a].depth > graph[b].depth:  # 무조건 b가 더 깊거나 같도록
        a, b = b, a
    # 깊이를 같도록 만들어주는 로직, 깊이 맞춰주면서 weight 기억해줘야함
    depth_gap = graph[b].depth - graph[a].depth
    while depth_gap > 0:
        exponent = int(log2(depth_gap))  # 가장 큰 비트 gap : 5 -> 2^2 + 2^0 -> exp : 2
        _min, _max = min(_min, graph[b].parents_min_weight[exponent]), max(_max, graph[b].parents_max_weight[exponent])
        b = graph[b].parents[exponent]
        depth_gap -= 2**exponent


    # print(graph[a].depth == graph[b].depth)
    # 최소공통조상까지 찾아가면서 최소, 최대 weight 기억하기
    run = a != b
    while run:
        flag = True
        for i, (parents_a, parents_b) in enumerate(zip(graph[a].parents, graph[b].parents)):
            if parents_a == parents_b:
                if i == 0:
                    run = False
                    _min = min(_min, graph[a].parents_min_weight[i], graph[b].parents_min_weight[i])
                    _max = max(_max, graph[a].parents_max_weight[i], graph[b].parents_max_weight[i])
                    a, b = parents_a, parents_b
                    break
                _min = min(_min, graph[a].parents_min_weight[i - 1], graph[b].parents_min_weight[i - 1])
                _max = max(_max, graph[a].parents_max_weight[i - 1], graph[b].parents_max_weight[i - 1])
                a, b = graph[a].parents[i - 1], graph[b].parents[i - 1]
                flag = False
                break
        if not graph[a].parents:  # 루트일때
            run = False
        if not run:
            break
        if flag:
            _min = min(_min, graph[a].parents_min_weight[-1], graph[b].parents_min_weight[-1])
            _max = max(_max, graph[a].parents_max_weight[-1], graph[b].parents_max_weight[-1])
            a, b = graph[a].parents[-1], graph[b].parents[-1]

    print(_min, _max)


if __name__ == '__main__':
    node_count: int = int(input())
    max_parents_size = int(log2(node_count)) + 1
    graph: List[Node] = [None] + [Node(num) for num in range(1, node_count + 1)]
    visit: List[bool] = [False] * (node_count + 1)
    for _ in range(node_count - 1):
        a, b, weight = map(int, input().split())
        graph[a].neighborhood.append((b, weight))
        graph[b].neighborhood.append((a, weight))

    set_depth()
    set_parents()

    query_count = int(input())
    for _ in range(query_count):
        a, b = map(int, input().split())
        lca(a, b)

"""
Input
7
3 6 4
1 7 1
1 3 2
1 2 6
2 5 4
2 4 4
5
6 4
7 6
1 2
1 3
3 5

Output
2 6
1 4
6 6
2 2
2 6
"""
