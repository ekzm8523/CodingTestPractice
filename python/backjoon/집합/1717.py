def find(a):
    if parent[a] == a:
        return a
    parent[a] = find(parent[a])
    return parent[a]


def union(a, b):
    a = find(a)
    b = find(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


if __name__ == "__main__":
    n, m = map(int, input().split())

    parent = [i for i in range(n+1)]

    for i in range(m):
        query, a, b = map(int, input().split())

        if query == 0:
            union(a, b)
        elif query == 1:
            print("YES") if find(a) == find(b) else print("No")

