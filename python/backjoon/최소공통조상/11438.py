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
input = lambda: sys.stdin.readline().strip()

if __name__ == '__main__':
    node_count = int(input())
    graph = {node_num: [-1, [], -1] for node_num in range(1, node_count + 1)}  # [parent, children, depth]
    for _ in range(node_count - 1):
        parent, child = map(int, input().split())
        if parent > child:  # 무조건 작은 노드가 부모로 정의
            parent, child = child, parent

        graph[parent][1].append(child)
        graph[child][0] = parent

    # depth 구하기
    graph[1][2] = 0

    # parents 배열 구하기
    parents = []

# import sys
# from dataclasses import dataclass, field
# import math
# from typing import List
# input = lambda: sys.stdin.readline().strip()
#
#
# @dataclass
# class Node:
#     num: int  # 구현 후 삭제
#     depth: int = None
#     parents: List[int] = field(default_factory=list)
#     children: List[int] = field(default_factory=list)
#
#
# def find_same_parent(tree: List[Node], left_node, right_node):
#     if left_node == right_node:
#         return left_node
#
#     while tree[left_node].parents[0] != tree[right_node].parents[0]:
#         for i in range(1, len(tree[left_node].parents)):
#             if tree[left_node].parents[i] == tree[right_node].parents[i]:
#                 left_node, right_node = tree[left_node].parents[i - 1], tree[right_node].parents[i - 1]
#                 return tree[left_node].parents[0]
#         left_node, right_node = tree[left_node].parents[-1], tree[right_node].parents[-1]
#
#     return tree[left_node].parents[0]
#
# def find_same_depth_node(tree: List[Node], move_node: int, target_depth: int):
#     current_node = move_node
#     while tree[current_node].depth != target_depth:
#         log_depth = math.log2(tree[current_node].depth - target_depth)
#         current_node = tree[current_node].parents[int(log_depth)]
#
#     return current_node
#
#
# def dfs_init(tree: List[Node], node_num: int, depth: int):
#     for child in tree[node_num].children:
#         tree[child].depth = depth
#         step = 0
#         parent_node = tree[child].parents[0]
#         while parent_node != -1 and tree[parent_node].depth - 2 ** step >= 0:
#             parent_node = tree[parent_node].parents[step]
#             tree[child].parents.append(parent_node)
#             step += 1
#
#         dfs_init(tree, child, depth + 1)
#
#
# if __name__ == '__main__':
#     node_cnt = int(input())
#     tree = [None] + [Node(num=i) for i in range(1, node_cnt + 1)]
#     tree[1].parents.append(-1)
#     for _ in range(node_cnt - 1):
#         parent, child = map(int, input().split())
#         if parent > child:
#             parent, child = child, parent
#         tree[child].parents.append(parent)
#         tree[parent].children.append(child)
#
#
#     tree[1].depth = 0
#     dfs_init(tree, 1, 1)
#     query_cnt = int(input())
#
#     for _ in range(query_cnt):
#         left_node, right_node = map(int, input().split())
#         if tree[left_node].depth < tree[right_node].depth:  # 왼쪽이 더 아래에 있는 노드가 되도록
#             left_node, right_node = right_node, left_node
#         left_node = find_same_depth_node(tree, left_node, tree[right_node].depth)
#
#         print(find_same_parent(tree, left_node, right_node))
#
# """
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
