# https://www.acmicpc.net/problem/20040
"""
Union find 알고리즘에서 Cycle 판별법
1. A 집합과 B 집합의 루트 노드를 확인한다.
2. 루트 노드가 같다면 이미 같은 집합인데 연결하려고 하므로 cycle 발생
3. 없다면 union find 알고리즘 적용

Union find 알고리즘은 Union 과 find 의 합성어로 찾으면서 합친다는 말이다.
Union을 할때 부모만 연결시켜준다면 편향 트리가 만들어질 수 있기 때문에 find를 할때 cost가 너무 커진다.
그러므로 find 를 진행하면서 부모노드를 한칸씩 땡겨준다고 보면 된다.

"""
import sys


def union(parents, A, B):
    # A set | B set
    A = find(parents, A)
    B = find(parents, B)
    if A <= B:
        parents[B] = A
    else:
        parents[A] = B


def find(parents, node):
    # 루트 노드 find
    if parents[node] == node:
        return node
    parents[node] = find(parents, parents[node])
    return parents[node]


def is_cycle(parents, A, B):
    # A set의 루트노드와 B set의 루트노드를 비교
    a_parent, b_parent = find(parents, A), find(parents, B)
    return a_parent == b_parent


if __name__ == '__main__':
    node_count, edge_count = map(int, sys.stdin.readline().split())
    edges = [tuple(map(int, sys.stdin.readline().split())) for _ in range(edge_count)]
    parents = [i for i in range(node_count)]

    for i, edge in enumerate(edges):
        if is_cycle(parents, *edge):
            print(i+1)
            sys.exit()
        else:
            union(parents, *edge)
    print(0)
