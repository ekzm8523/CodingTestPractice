"""
1. 들어오는 간선이 하나도 없는 단 하나의 노드가 존재한다. 이를 루트(root) 노드라고 부른다.
-> in_node를 전부 모으고 전체 노드 - 1과 사이즈가 같은지 확인한다.
2. 루트 노드를 제외한 모든 노드는 반드시 단 하나의 들어오는 간선이 존재한다.
-> in_node를 set로 모으면서 다른 경로에서 들어오는 node가 있으면
3. 루트에서 다른 노드로 가는 경로는 반드시 가능하며, 유일하다. 이는 루트를 제외한 모든 노드에 성립해야 한다.
-> node의 개수 - 1 == edge의 개수
"""
import sys

if __name__ == "__main__":
    num = 0
    flag = True
    while flag:
        num += 1
        is_tree = True
        edges = []
        while True:
            line = list(map(int, sys.stdin.readline().split()))
            size = len(line)
            # if line[-1] == -1:
            #     flag = False
            #     break
            for i in range(0, size, 2):
                edges.append((line[i], line[i + 1]))

            if line[-1] == 0:
                edges = edges[:-1]
                next_line = list(map(int, sys.stdin.readline().split()))
                if next_line and next_line[0] == -1:
                    flag = False
                break
        parents = {}
        node_set = set()
        in_nodeset = set()
        for out_node, in_node in edges:
            node_set.add(out_node)
            node_set.add(in_node)
            if in_node in parents.keys():
                if out_node != parents[in_node]:
                    is_tree = False
            else:
                parents[in_node] = out_node

            if in_node in in_nodeset:
                is_tree = False
                break
            else:
                in_nodeset.add(in_node)
        node_cnt = len(node_set)
        if len(edges) != node_cnt - 1 or len(in_nodeset) != node_cnt - 1:     # 간선의 갯수 -> 노드의 갯수 -1 , 부모노드가 없는 루트는 하나만 존재
            is_tree = False



        # 트리가 한개인지 확인
        pass_node = set()
        root_node = None
        is_cycle = False

        for current_node in node_set:

            if current_node in pass_node:
                continue
            node = current_node

            while True:
                pass_node.add(current_node)
                if node not in parents.keys():
                    if root_node is None:
                        root_node = node
                    else:
                        if root_node != node:
                            is_cycle = True
                            break
                else:
                    node = parents[node]
                    pass_node.add(node)
                    if node == current_node:    # 사이클
                        is_cycle = True
                        break
            if is_cycle:
                is_tree = False
                break


        # 빈 트리도 트리
        if node_cnt == 0:
            is_tree = True

        print(f"Case {num} is {'not ' if not is_tree else ''}a tree.")