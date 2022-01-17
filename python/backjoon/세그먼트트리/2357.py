# https://www.acmicpc.net/problem/2357
"""
세그먼트 트리 최소값, 최대값 구하기
[input]
10 4
75
30
100
38
50
51
52
20
81
5
1 10
3 5
6 9
8 10
"""

import sys
from math import ceil, log2

INF = sys.maxsize

def init_min_tree(node: int, start: int, end: int) -> int:
    global min_tree, nums

    if start == end:
        min_tree[node] = nums[end]
    else:
        mid = (start + end) // 2
        min_tree[node] = min(init_min_tree(node * 2, start, mid), init_min_tree(node * 2 + 1, mid + 1, end))
    return min_tree[node]


def get_min_interval(node: int, start: int, end: int, t_start: int, t_end: int) -> int:
    global min_tree

    if start > t_end or end < t_start:
        return INF

    if t_start <= start <= end <= t_end:
        return min_tree[node]

    mid = (start + end) // 2

    return min(
        get_min_interval(node * 2, start, mid, t_start, t_end),
        get_min_interval(node * 2 + 1, mid + 1, end, t_start, t_end)
    )


def get_max_interval(node: int, start: int, end: int, t_start: int, t_end: int) -> int:
    global max_tree

    if start > t_end or end < t_start:
        return 0

    if t_start <= start <= end <= t_end:
        return max_tree[node]

    mid = (start + end) // 2

    return max(
        get_max_interval(node * 2, start, mid, t_start, t_end),
        get_max_interval(node * 2 + 1, mid + 1, end, t_start, t_end)
    )


def init_max_tree(node, start, end):
    global max_tree, nums

    if start == end:
        max_tree[node] = nums[end]
    else:
        mid = (start + end) // 2
        max_tree[node] = max(init_max_tree(node * 2, start, mid), init_max_tree(node * 2 + 1, mid + 1, end))
    return max_tree[node]


if __name__ == '__main__':
    num_cnt, query_cnt = map(int, sys.stdin.readline().split())

    nums = [0] + [int(sys.stdin.readline()) for _ in range(num_cnt)]

    # segment tree initialization
    tree_height = ceil(log2(num_cnt))  # if num_cnt is 7 height is 3
    tree_size = 2 ** (tree_height + 1)
    min_tree = [0] * (tree_size + 1)  # index는 1부터 시작
    max_tree = [0] * (tree_size + 1)

    init_min_tree(1, 1, num_cnt)
    init_max_tree(1, 1, num_cnt)

    for _ in range(query_cnt):
        a, b = map(int, sys.stdin.readline().split())
        print(get_min_interval(1, 1, num_cnt, a, b), get_max_interval(1, 1, num_cnt, a, b))
