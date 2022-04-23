# https://www.acmicpc.net/problem/11438
import sys
from dataclasses import dataclass, field
import math
from typing import List
input = lambda: sys.stdin.readline().strip()


@dataclass
class Node:
    num: int  # 구현 후 삭제
    depth: int = None
    parents: List[int] = field(default_factory=list)
    children: List[int] = field(default_factory=list)


def find_same_parent(tree: List[Node], left_node, right_node):
    if left_node == right_node:
        return left_node

    while tree[left_node].parents[0] != tree[right_node].parents[0]:
        for i in range(1, len(tree[left_node].parents)):
            if tree[left_node].parents[i] == tree[right_node].parents[i]:
                left_node, right_node = tree[left_node].parents[i - 1], tree[right_node].parents[i - 1]
                return tree[left_node].parents[0]
        left_node, right_node = tree[left_node].parents[-1], tree[right_node].parents[-1]

    return tree[left_node].parents[0]

def find_same_depth_node(tree: List[Node], move_node: int, target_depth: int):
    current_node = move_node
    while tree[current_node].depth != target_depth:
        log_depth = math.log2(tree[current_node].depth - target_depth)
        current_node = tree[current_node].parents[int(log_depth)]

    return current_node


def dfs_init(tree: List[Node], node_num: int, depth: int):
    for child in tree[node_num].children:
        tree[child].depth = depth
        step = 0
        parent_node = tree[child].parents[0]
        while parent_node != -1 and tree[parent_node].depth - 2 ** step >= 0:
            parent_node = tree[parent_node].parents[step]
            tree[child].parents.append(parent_node)
            step += 1

        dfs_init(tree, child, depth + 1)


if __name__ == '__main__':
    node_cnt = int(input())
    tree = [None] + [Node(num=i) for i in range(1, node_cnt + 1)]
    tree[1].parents.append(-1)
    for _ in range(node_cnt - 1):
        parent, child = map(int, input().split())
        if parent > child:
            parent, child = child, parent
        tree[child].parents.append(parent)
        tree[parent].children.append(child)


    tree[1].depth = 0
    dfs_init(tree, 1, 1)
    query_cnt = int(input())

    for _ in range(query_cnt):
        left_node, right_node = map(int, input().split())
        if tree[left_node].depth < tree[right_node].depth:  # 왼쪽이 더 아래에 있는 노드가 되도록
            left_node, right_node = right_node, left_node
        left_node = find_same_depth_node(tree, left_node, tree[right_node].depth)

        print(find_same_parent(tree, left_node, right_node))

"""
15
1 2
1 3
2 4
3 7
6 2
3 8
4 9
2 5
5 11
7 13
10 4
11 15
12 5
14 7
6
6 11
10 9
2 6
7 6
8 13
3 15
"""