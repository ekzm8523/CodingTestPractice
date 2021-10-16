"""
사이클 X
위상정렬 -> 큐 or 스택으로 가능
일반적으로 큐 사용

"""
from collections import deque

def solution(n, path, order):
    answer = True

    undirected_graph = {i: [] for i in range(n)}
    for a, b in path:
        undirected_graph[a].append(b)
        undirected_graph[b].append(a)



    injection_node = {i: [] for i in range(n)}
    directed_graph = {i: [] for i in range(n)}
    visit_set = set()
    q = deque((0,))

    while q:
        node = q.popleft()
        visit_set.add(node)

        for next_node in undirected_graph[node]:
            if next_node not in visit_set:
                q.append(next_node)
                injection_node[next_node].append(node)
                directed_graph[node].append(next_node)
    del undirected_graph

    for a, b in order:
        injection_node[b].append(a)
        if b not in directed_graph[a]:
            directed_graph[a].append(b)

    for k, v in injection_node.items():
        if v:
            injection_node[k] = set(v)

    print(directed_graph)
    print(injection_node)
    q2 = deque((0,))
    visit_set = set()
    while q2:
        node = q2.popleft()

        # print(f"remove {node}")
        for next_node in directed_graph[node]:
            if next_node in visit_set:
                return False
            injection_node[next_node].remove(node)
            if len(injection_node[next_node]) == 0:
                del(injection_node[next_node])
                q2.append(next_node)
        visit_set.add(node)

    return len(visit_set) == n


if __name__ == '__main__':
    # n = 9
    # path = [[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]]
    # order = [[8,5],[6,7],[4,1]]
    # print(solution(n, path, order))
    #
    # n = 9
    # path = [[8,1],[0,1],[1,2],[0,7],[4,7],[0,3],[7,5],[3,6]]
    # order = [[4,1],[5,2]]
    # print(solution(n, path, order))
    #
    # n = 9
    # path = [[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]]
    # order = [[4,1],[8,7],[6,5]]
    # print(solution(n, path, order))

    n = 3
    path = [[0, 1], [1, 2]]
    order = [[2, 1]]
    print(solution(n, path, order))