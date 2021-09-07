# https://www.acmicpc.net/problem/1167
"""
트리의 지름을 구하는 방법
임의의 x를 루트노드로 지정
x에서 가장 먼 노드인 y를 구하고
y에서 가장 먼 노드인 z를 구하고
z와 y의 거리를 구하면 지름이다.
https://blog.myungwoo.kr/112 참고
"""
import sys

if __name__ == "__main__":
    v = int(sys.stdin.readline())
    sys.setrecursionlimit(int(1e6))
    graph = {}
    for i in range(v):
        lists = list(map(int, sys.stdin.readline().split()))[:-1]
        ptr_node = lists[0]
        graph[ptr_node] = []
        for i in range(1, len(lists), 2):
            graph[ptr_node].append(tuple(lists[i:i+2]))


    def find_farthest_node(current_node, diameter):
        global max_diameter, farthest_node
        visit[current_node] = True
        is_leaf = True
        for next_node, weight in graph[current_node]:
            if not visit[next_node]:
                is_leaf = False
                find_farthest_node(next_node, diameter + weight)
        visit[current_node] = False
        if is_leaf and max_diameter < diameter:
            max_diameter = diameter
            farthest_node = current_node

    visit = [False] * (v + 1)
    max_diameter = 0
    farthest_node = None
    find_farthest_node(1, 0)

    max_diameter = 0
    find_farthest_node(farthest_node, 0)
    print(max_diameter)



