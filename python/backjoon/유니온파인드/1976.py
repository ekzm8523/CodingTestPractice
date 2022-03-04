# https://www.acmicpc.net/problem/1976

def find(parent, A):
    if parent[A] != A:
        parent[A] = find(parent, parent[A])
    return parent[A]


def union(parent, A, B):
    A = find(parent, A)
    B = find(parent, B)

    if A <= B:
        parent[B] = A
    else:
        parent[A] = B


if __name__ == '__main__':
    city_cnt = int(input())
    travel_len = int(input())
    table = [tuple(map(int, input().split())) for _ in range(city_cnt)]
    parent = list(range(city_cnt))

    travel_flan = list(map(int, input().split()))
    for i, nodes in enumerate(table):
        for j, flag in enumerate(nodes):
            if flag:
                union(parent, i, j)

    answer = True
    p = find(parent, travel_flan[0] - 1)
    for _, node in enumerate(travel_flan):
        if find(parent, node-1) != p:
            answer = False
            break
    print("YES" if answer else "NO")