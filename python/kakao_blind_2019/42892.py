# https://school.programmers.co.kr/learn/courses/30/lessons/42892
"""
1. 좌표로 주어진 노드들을 트리구조로 변경
    - 같은 level에 있는 노드는 같은 y값을 가진다.
    - 오른쪽 자식은 부모보다 x값이 크고 왼쪽 자식은 부모보다 x값이 작음
    - 최소 공통 조상이 필요함

2. 전위 순회, 후위 순회를 각각 출력
"""


class Node:
    def __init__(self, num: int):
        self.num = num
        self.parent = None
        self.children = []

    def __str__(self):
        return f"num : {self.num}, parent: {self.parent}, children: {self.children}"


    def __repr__(self):
        return f"num : {self.num}, parent: {self.parent}, children: {self.children}"


def solution(nodes):
    answer = [[]]

    sorted_levels = sorted(set([y for _, y in nodes]), reverse=True)
    node_dict = {i + 1: pos for i, pos in enumerate(nodes)}
    graph = {num: Node(num)for num in node_dict}
    level_dict = {}
    for key in node_dict:
        level = node_dict[key][1]

        if level not in level_dict:
            level_dict[level] = [key]
        else:
            level_dict[level].append(key)

    iter_order = sorted(node_dict, key=lambda x: (-node_dict[x][1], node_dict[x][0]))
    root_node = graph[level_dict[sorted_levels[0]][0]]
    root_node.children = level_dict[sorted_levels[1]].copy()
    for node in root_node.children:
        graph[node].parent = root_node.num

    for i, level in enumerate(sorted_levels):
        if i == 0:
            continue
        for node_num in level_dict[level]:
            x, y = node_dict[node_num]
            for upper_node_num in level_dict[sorted_levels[i - 1]]:
                upper_x, upper_y = node_dict[upper_node_num]







    # for i, node_num in enumerate(iter_order):
    #     if i == 0:  # 루트 설정





    # root =
    nodes.sort(key=lambda x: x[1])

    return answer


if __name__ == '__main__':
    print(solution([[5, 3], [11, 5], [13, 3], [3, 5], [6, 1], [1, 3], [8, 6], [7, 2], [2, 2]]))