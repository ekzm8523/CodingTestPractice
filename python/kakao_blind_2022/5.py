"""

"""

from collections import deque
class Node:

    def __init__(self, node_num, is_sheep):
        self.num = node_num
        self.is_sheep = None
        self.parent = None
        self.childs = []
        self.is_sheep = (is_sheep == 0)
        self.wolf_cnt = 0
        self.is_leaf = True
    def __repr__(self):
        if self.is_sheep:
            return f"{self.num}(sheep)"
        else:
            return f"{self.num}(wolf)"

    def __str__(self):
        return f"Node {self.num}  is_sheep : {self.is_sheep}   parent : {self.parent}   childs : {self.childs} " \
               f"following wolf num is {self.wolf_cnt}"

def solution(info, edges):
    answer = 0
    tree = []
    for node_num, is_sheep in enumerate(info):
        tree.append(Node(node_num, is_sheep))

    for edge in edges:
        a, b = edge
        tree[a].childs.append(b)
        tree[b].parent = a
        tree[a].is_leaf = True

    q = deque()
    q.append(0)



    while q:
        current_node = tree[q.popleft()]
        childs = current_node.childs
        for child in childs:
            if current_node.is_sheep:
                tree[child].wolf_cnt = current_node.wolf_cnt
            else:
                tree[child].wolf_cnt = current_node.wolf_cnt + 1
            q.append(child)

    sheep = []
    for node in tree:
        if node.is_sheep:
            sheep.append(node)

    sorted_sheep = sorted(sheep, key=lambda x: x.wolf_cnt)
    print(sorted_sheep)

    # def dfs(num):


    sheep_set = set()
    wolf_set = set()
    for sheep in sorted_sheep:
        dfs(sheep.num)

    print()
    return answer

if __name__ == "__main__":

    info = [0,0,1,1,1,0,1,0,1,0,1,1]
    edges = [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]
    print(solution(info, edges))
    info = [0,1,0,1,1,0,1,0,0,1,0]
    edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]]
    print(solution(info, edges))
