# https://www.acmicpc.net/problem/2042

import sys

def update(i, dif):
    while i <= n:
        tree[i] += dif
        i += (i & -i)


def prefix_sum(i):
    result = 0
    while i > 0:
        result += tree[i]
        i -= (i & -i)
    return result


def interval_sum(start, end):
    return prefix_sum(end) - prefix_sum(start - 1)


if __name__ == "__main__":

    n, m, k = map(int, sys.stdin.readline().split())

    arr = [0] * (n + 1)
    tree = [0] * (n + 1)

    for i in range(1, n + 1):
        x = int(sys.stdin.readline())
        arr[i] = x
        update(i, x)

    for i in range(m + k):
        a, b, c = map(int, sys.stdin.readline().split())
        if a == 1:
            update(b, c - arr[b])
            arr[b] = c
        else:
            print(interval_sum(b, c))