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

    graph = {}
    for i in range(v):
        lists = list(map(int, sys.stdin.readline().split()))[:-1]
        ptr_node = lists[0]
        graph[ptr_node] = []

        ptr_node


    print(graph)


