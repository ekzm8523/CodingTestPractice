"""
https://www.acmicpc.net/problem/11438
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
from math import log2

input = lambda: sys.stdin.readline().strip()
sys.setrecursionlimit(int(2e6))

class Node:
    def __init__(self, parents=None, depth=None, children=None):
        self.parents = parents if parents else []
        self.children = children if children else []
        self.depth = depth


if __name__ == '__main__':
    node_count = int(input())
    graph = {num: Node() for num in range(1, node_count + 1)}  # [parent, children, depth]

    # init
    for _ in range(node_count - 1):
        parent, child = map(int, input().split())
        if parent > child:  # 무조건 작은 노드가 부모로 정의
            parent, child = child, parent
        graph[parent].children.append(child)
        graph[child].parents.append(parent)

    # find depth
    def find_depth(cur, depth):
        graph[cur].depth = depth
        for child in graph[cur].children:
            find_depth(child, depth + 1)

    find_depth(1, 0)

    # parents
    def find_parents(cur):
        parents_size = int(log2(graph[cur].depth)) if graph[cur].depth != 0 else 0
        for i in range(1, parents_size + 1):
            half_parent = graph[cur].parents[i-1]
            graph[cur].parents.append(graph[half_parent].parents[i-1])

        for child in graph[cur].children:
            find_parents(child)

    find_parents(1)

    query_count = int(input())
    for _ in range(query_count):
        node1, node2 = map(int, input().split())
        if graph[node1].depth >= graph[node2].depth:  # 오른쪽의 depth가 더 깊도록 설정
            node1, node2 = node2, node1
        # 높이를 같게 만들어주기
        depth_gab = graph[node2].depth - graph[node1].depth
        while depth_gab > 0:
            idx = int(log2(depth_gab))
            node2 = graph[node2].parents[idx]
            depth_gab -= 2 ** idx

        # 최소 공통 조상 찾기
        while node1 != node2:
            flag = True
            for i, (p1, p2) in enumerate(zip(graph[node1].parents, graph[node2].parents)):
                if p1 == p2:
                    flag = False
                    if i == 0:
                        node1, node2 = p1, p2
                        break
                    node1, node2 = graph[node1].parents[i-1], graph[node2].parents[i-1]
            if flag:
                node1, node2 = graph[node1].parents[-1], graph[node2].parents[-1]
        print(node1)

# 15
# 1 2
# 1 3
# 2 4
# 3 7
# 6 2
# 3 8
# 4 9
# 2 5
# 5 11
# 7 13
# 10 4
# 11 15
# 12 5
# 14 7
# 6
# 6 11
# 10 9
# 2 6
# 7 6
# 8 13
# 3 15
# """
