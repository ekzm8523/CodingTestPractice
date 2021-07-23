from math import log2, ceil
import sys

def update_tree(value):
    idx = value + size - 1
    while idx > 0:
        tree[idx] += 1
        idx //= 2


def delete_tree(rank):
    idx = 1
    while idx < size:
        tree[idx] -= 1
        if tree[idx * 2] >= rank:
            idx *= 2
        else:
            rank -= tree[idx * 2]
            idx = idx * 2 + 1
    tree[idx] -= 1
    return idx - size + 1


if __name__ == "__main__":
    p = 2000000
    h = ceil(log2(p))   # 실제 트리 높이는 h + 1
    size = 2 ** h   # 1(value)을 넣으면 size - 1 + 1(value)
    tree = [0] * size * 2

    n = int(sys.stdin.readline())

    for _ in range(n):
        query, value = map(int, sys.stdin.readline().split())

        if query == 1:
            update_tree(value)
        else:
            print(delete_tree(value))


