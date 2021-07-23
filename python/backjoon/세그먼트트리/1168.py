# https://www.acmicpc.net/problem/1168
# update, prev_sum

from math import log2, ceil

def update_tree(i, dif=1):
    while i > 0:
        tree[i] += dif
        i //= 2

def delete_tree(node, k):
    while node < size:  # 왼쪽
        if tree[node * 2] < k:
            k -= tree[node * 2]
            node = node * 2 + 1
        else:   # 오른쪽
            node = node * 2
    tmp = node
    update_tree(tmp, -1)

    return node - size + 1

if __name__ == "__main__":

    n, k = map(int, input().split())

    h = ceil(log2(n))
    size = 2**h
    tree = [0] * size * 2

    for i in range(n):
        update_tree(size + i)

    answer = []
    delete_idx = 1
    for i in range(n):
        delete_idx = (delete_idx + k - 1) % tree[1]
        if delete_idx == 0:
            delete_idx = tree[1]
        answer.append(delete_tree(1, delete_idx))

    print(f"<", end="")
    for ans in answer[:-1]:
        print(ans, end=", ")
    print(f"{answer[-1]}>")
