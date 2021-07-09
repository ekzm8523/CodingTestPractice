# https://www.acmicpc.net/problem/14621

"""
1. 사심 경로는 사용자들의 사심을 만족시키기 위해 남초 대학교와 여초 대학교들을 연결하는 도로로만 이루어져 있다.
2. 사용자들이 다양한 사람과 미팅할 수 있도록 어떤 대학교에서든 모든 대학교로 이동이 가능한 경로이다. (Spanning Tree)
3. 시간을 낭비하지 않고 미팅할 수 있도록 이 경로의 길이는 최단 거리가 되어야 한다. (MST)
"""
import sys

def find(node):
    if parents[node] != node:
        parents[node] = find(parents[node])

    return parents[node]

def union(A, B):
    A_parent = find(A)
    B_parent = find(B)

    if A_parent > B_parent:
        parents[A_parent] = B_parent
    else:
        parents[B_parent] = A_parent

if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().split())   # N: 학교의 수, M: 도로의 개수
    gender_list = [None] + list(sys.stdin.readline().split())
    edges = [tuple(map(int, sys.stdin.readline().split())) for _ in range(M)]

    # print(edges)
    edges.sort(key=lambda x: x[2])
    # print(edges)
    parents = [i for i in range(N + 1)]
    answer = 0
    node_cnt = 1
    for u, v, d in edges:
        # print(u,v,d)
        u_parent = find(u)  # u가 MST에 포함되어 있는지 확인하는 함수
        v_parent = find(v)
        if u_parent == v_parent:
            # print(f"{u}랑 {v} 이미 둘다 집어넣었슈")
            continue
        if gender_list[u] == gender_list[v]:
            # print("같은 성끼리는 못이어유")
            continue
        union(u, v)
        node_cnt += 1
        answer += d
        # print(f"union of the {u} and {v} answer {answer}")
        # print(parents)

        if node_cnt == N:
            # print("완성~")
            break
    if node_cnt < N:
        answer = -1

    print(answer)


