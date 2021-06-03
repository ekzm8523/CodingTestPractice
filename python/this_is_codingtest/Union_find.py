

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


# def find_parent(parent, x):
#     if parent[x] != x:
#         return find_parent(parent, parent[x])
#     return x


if __name__ == "__main__":
    v, e = map(int, input().split())
    parent = [0] * (v + 1)

    for i in range(1, v + 1):
        parent[i] = i

    cycle = False

    for edge in range(e):
        a, b = map(int, input().split())
        if find_parent(parent, a) == find_parent(parent, b):
            cycle = True
            break
        else:
            union_parent(parent, a, b)

    if cycle:
        print("사이클이 발생")
    else:
        print("사이클이 안발생 ㅋ")


    print('각 원소가 속한 집합: ', end='')
    for i in range(1, v + 1):
        print(find_parent(parent, i), end=' ')

    print()

    print('부모 테이블:', end=' ')
    for i in range(1, v + 1):
        print(parent[i], end=' ')