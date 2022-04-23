# https://www.acmicpc.net/problem/11438
import sys
from dataclasses import dataclass, field
input = lambda: sys.stdin.readline().strip()


@dataclass
class Node:
    num: int  # 구현 후 삭제
    depth: int = None
    parents: list[int] = field(default_factory=list)
    children: list[int] = field(default_factory=list)


# def find_parent(tree, num):
#     while num != -1:
#         print(tree[num])
#         num = tree[num].parents[0]

def dfs_init(tree: list[Node], node_num: int, depth: int):

    if not tree[node_num].children:
        return

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
    for t in tree:
        print(t)

    query_cnt = int(input())

    for _ in range(query_cnt):
        node1, node2 = map(int, input().split())
