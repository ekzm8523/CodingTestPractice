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
input = lambda: sys.stdin.readline().strip()


class Node:
    def __init__(self, num):
        self.num: int = num
        self.parent: Optional[int] = None
        self.children: List[int] = []
        self.depth: Optional[int] = None
        self.parents: List[int] = []
        self.weights: List[int] = []
        self.parents_weight: List[Tuple] = []

    def __str__(self) -> str:
        return f"num : {self.num}," \
               f" parent : {self.parent}," \
               f" children : {self.children}," \
               f" parents : {self.parents}," \
               f" parents_weight : {self.parents_weight}" \
               f" depth : {self.depth}" \
               f" weights : {self.weights}"

    def __repr__(self) -> str:
        return f"num : {self.num}," \
               f" parent : {self.parent}," \
               f" children : {self.children}," \
               f" parents : {self.parents}," \
               f" parents_weight : {self.parents_weight}"\
               f" depth : {self.depth}" \
               f" weights : {self.weights}"



def set_depth(graph: List[Node], depth: int, num: int):
    graph[num].depth = depth
    if depth > 0:
        for _ in range(int(log2(depth))):  # parents의 사이즈 공식
            graph[num].parents.append(0)
            graph[num].parents_weight.append(0)
    for child in graph[num].children:
        set_depth(graph, depth + 1, child)



def set_parents(graph: List[Node], num: int):
    parents_size = 0
    if graph[num].depth:
        parents_size = int(log2(graph[num].depth)) + 1  # 0은 log에 태울 수 없음 -> root node

    for i in range(1, parents_size):
        graph[num].parents[i] = graph[graph[num].parents[i-1]].parents[i-1]
        graph[num].parents_weight[i] = (
            min(graph[num].parents_weight[i - 1][0], graph[graph[num].parents[i - 1]].parents_weight[i - 1][0]),
            max(graph[num].parents_weight[i - 1][1], graph[graph[num].parents[i - 1]].parents_weight[i - 1][1]),
        )  # min, max

    for child in graph[num].children:
        set_parents(graph, child)

if __name__ == '__main__':
    node_count: int = int(input())
    graph: List[Node] = [None] + [Node(num) for num in range(1, node_count + 1)]

    for _ in range(node_count - 1):
        a, b, weight = map(int, input().split())
        if a > b:
            a, b = b, a
        graph[a].children.append(b)
        graph[a].weights.append(weight)
        graph[b].parent = a
        graph[b].parents.append(a)
        graph[b].parents_weight.append((weight, weight))
    set_depth(graph, 0, 1)
    set_parents(graph, 1)
    for node in graph:
        print(node)
