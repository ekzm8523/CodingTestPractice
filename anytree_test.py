import sys

from anytree import Node, RenderTree
from anytree.exporter import DotExporter

input = lambda: sys.stdin.readline().strip()


if __name__ == '__main__':
    node_count = int(input())
    graph = {}
    graph[1] = Node(1)  # root
    for _ in range(node_count - 1):
        parent, child = map(int, input().split())
        if parent > child:  # 무조건 작은 노드가 부모로 정의
            parent, child = child, parent
        if child not in graph:
            graph[child] = Node(child, parent=graph[parent])
    print()
    for pre, fill, node in RenderTree(graph[1]):
        print(f"{pre}{node.name}")


    # DotExporter(graph[1]).to_picture("tree.png")