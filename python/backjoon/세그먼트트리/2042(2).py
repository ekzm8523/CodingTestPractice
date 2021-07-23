def update(idx, value):
    while idx <= n:
        tree[idx] += value
        idx += (idx & -idx)


def prefix_sum(idx):
    sum_value = 0
    while 0 < idx:
        sum_value += tree[idx]
        idx -= (idx & -idx)
    return sum_value


def interval_sum(start, end):
    return prefix_sum(end) - prefix_sum(start - 1)


if __name__ == "__main__":
    n, m, k = map(int, input().split())
    tree = [0] * (n + 1)
    arr = [0] * (n + 1)

    for i in range(1, n + 1):
        x = int(input())
        arr[i] = x
        update(i, x)

    for _ in range(m + k):
        a, b, c = map(int, input().split())
        if a == 1:
            update(b, c - arr[b])
            arr[b] = c
        else:
            print(interval_sum(b, c))

