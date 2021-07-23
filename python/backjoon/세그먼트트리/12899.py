# https://www.acmicpc.net/problem/12899
import sys
from math import ceil, log2

def update(i):
    while i >= 1:
        tree[i] += 1
        i //= 2


def delete(node, b):
    while node < size:
        if tree[node*2] < b:
            b -= tree[node * 2]
            node = node * 2 + 1
        else:
            node = node * 2

    tmp = node
    while tmp >= 1:
        tree[tmp] -= 1
        tmp //= 2

    return node - size + 1



if __name__ == "__main__":
    p = 2000000
    h = ceil(log2(p))   # 실제로는 트리의 높이 - 1
    size = 2**h     # index가 나오기 전까지의 size

    tree = [0] * size * 2

    n = int(sys.stdin.readline())

    for i in range(n):
        q, value = map(int, sys.stdin.readline().split())
        if q == 1:
            update(size + value - 1)
        else:
            print(delete(1, value))
