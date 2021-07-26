# https://www.acmicpc.net/problem/3584
import sys

def find_depth(current_node, depth):
    depths[current_node] = depth
    for child in childs[current_node]:
        find_depth(child, depth + 1)


def LCA(node1, node2):

    while depths[node1] != depths[node2]:
        if depths[node1] > depths[node2]:
            node1 = parents[node1]
        else:
            node2 = parents[node2]

    while node1 != node2:
        node1, node2 = parents[node1], parents[node2]

    return node1

if __name__ == "__main__":

    T = int(sys.stdin.readline())
    for _ in range(T):
        n = int(sys.stdin.readline())
        parents = [None] * (n + 1)
        childs = [None] + [[] for _ in range(n)]
        for _ in range(n - 1):
            a, b = map(int, sys.stdin.readline().split())
            parents[b] = a
            childs[a].append(b)
        depths = [None] + [0] * n

        root_node = None
        for i, parent in enumerate(parents):
            if parent == None:
                root_node = i


        find_depth(root_node, 1)

        node1, node2 = map(int, sys.stdin.readline().split())
        print(LCA(node1, node2))



