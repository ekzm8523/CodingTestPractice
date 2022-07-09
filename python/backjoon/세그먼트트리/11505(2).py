"""
https://www.acmicpc.net/problem/11505
세그먼트 트리
특정 구간의 합을 가장 빠르게 구할 수 있는 트리
만약 데이터가 잘 변하지 않으면 prefix sum을 쓰면 되는데 값이 변한다면 segment tree를 이용
1. 세그먼트 트리를 만든다
2. 합을 구하는 메서드를 만든다.
3. 값을 수정하는 메서드를 만든다.
overflow를 방지하기 위해 1_000_000_007로 나눈 나머지를 저장하고 출력한다.
"""
import sys
from math import log2, ceil

input = lambda: sys.stdin.readline().strip()
COMPLEMENT = 1_000_000_007


def tree_init(start, end, idx):
    if start == end:
        tree[idx] = nodes[start - 1]
        return tree[idx]

    mid = (start + end) // 2
    tree[idx] = (tree_init(start, mid, idx * 2) * tree_init(mid + 1, end, idx * 2 + 1)) % COMPLEMENT
    return tree[idx]


def tree_multiple(start, end, left, right, idx):
    if right < start or end < left:
        return 1
    if left <= start and end <= right:
        return tree[idx]

    mid = (start + end) // 2
    return (tree_multiple(start, mid, left, right, idx * 2) * tree_multiple(mid + 1, end, left, right, idx * 2 + 1)) % COMPLEMENT


def tree_update(start, end, num, dif, idx):
    if start <= num <= end:
        if start == end:
            tree[idx] = dif
        else:
            mid = (start + end) // 2
            if num <= mid:
                tree_update(start, mid, num, dif, idx * 2)
            else:
                tree_update(mid + 1, end, num, dif, idx * 2 + 1)
            tree[idx] = tree[2 * idx] * tree[2 * idx + 1] % COMPLEMENT


if __name__ == '__main__':
    node_count, change_count, multiple_count = map(int, input().split())
    nodes = list(int(input()) for _ in range(node_count))

    # tree init
    tree_depth = ceil(log2(node_count)) + 1
    tree = [1] * (2 ** tree_depth)
    tree_init(1, node_count, 1)
    for _ in range(change_count + multiple_count):
        query, a, b = map(int, input().split())

        if query == 1:
            tree_update(1, node_count, a, b, 1)
        else:
            print(tree_multiple(1, node_count, a, b, 1))





