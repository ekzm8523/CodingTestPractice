# https://www.acmicpc.net/problem/1197
"""

"""
import sys

def find(node):
    if parents[node] != node:
        parents[node] = find(parents[node])
    return parents[node]

def union(A, B):
    A = find(A)
    B = find(B)
    if A > B:
        parents[A] = B
    else:
        parents[B] = A

if __name__ == "__main__":

    V, E = map(int, sys.stdin.readline().split())

    edges = sorted([list(map(int, sys.stdin.readline().split())) for _ in range(E)], key=lambda x:x[2])
    parents = [i for i in range(V+1)]
    answer = 0
    cnt = 0

    for a, b, d in edges:
        p_a = find(a)
        p_b = find(b)
        if p_a == p_b:
            continue
        union(a, b)
        answer += d
        cnt += 1
        if cnt == V-1:
            break
    print(answer)
