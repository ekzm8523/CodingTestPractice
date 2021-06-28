# https://www.acmicpc.net/problem/1707

from collections import deque

def bfs(start):
    colouring[start] = 1
    q = deque()
    q.append(start)

    while q:
        current = q.popleft()

        for node in edges[current]:
            if colouring[node] == 0:
                colouring[node] = -colouring[current]
                q.append(node)
            else:
                if colouring[node] == colouring[current]:
                    return False
    return True

if __name__ == "__main__":
    num_test = int(input())

    for test in range(num_test):
        isTrue = True
        V, E = map(int, input().split())
        edges = [[] for _ in range(V + 1)]
        colouring = [0] * (V + 1)
        for i in range(E):
            edge = list(map(int, input().split()))
            edges[edge[0]].append(edge[1])
            edges[edge[1]].append(edge[0])


        for node in range(1, V+1):
            if colouring[node] == 0:
                if not bfs(node):
                    isTrue = False
                    break

        print("YES" if isTrue else "NO")