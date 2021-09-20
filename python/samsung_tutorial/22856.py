import sys

class Node:

    def __init__(self):
        self.lc = None
        self.rc = None
        self.parent = None
        self.is_visit = False

    def set_child(self, lc, rc):
        self.lc = lc
        self.rc = rc

    def set_parent(self, p):
        self.parent = p


if __name__ == "__main__":
    n = int(sys.stdin.readline())

    tree = [None] + [Node() for _ in range(n)]

    for _ in range(n):
        p, lc, rc = map(int, sys.stdin.readline().split())
        tree[p].set_child(lc, rc)
        tree[lc].set_parent(p)
        tree[rc].set_parent(p)


    def travel():
        current = 1
        # visit = set()
        visit_cnt = 1   # 방문처리용 카운터 , len(visit)을 매번 호출하면 cost가 크기 때문에 만든 변수
        record = 0
        while True:
            record += 1
            # 현재 위치한 노드의 왼쪽 자식 노드가 존재하고 아직 방문하지 않았다면, 왼쪽 자식 노드로 이동한다.
            if tree[current].lc != -1 and not tree[tree[current].lc].is_visit:
                # visit.add(tree[current].lc)
                visit_cnt += 1
                current = tree[current].lc
                tree[current].is_visit = True
            # 그렇지 않고 현재 위치한 노드의 오른쪽 자식 노드가 존재하고 아직 방문하지 않았다면, 오른쪽 자식 노드로 이동한다.
            elif tree[current].rc != -1 and not tree[tree[current].rc].is_visit:
                # visit.add(tree[current].rc)
                visit_cnt += 1
                current = tree[current].rc
                tree[current].is_visit = True
            # 그렇지 않고 현재 노드가 유사 중위 순회의 끝이라면, 유사 중위 순회를 종료한다.
            elif visit_cnt == n:
                break
            # 그렇지 않고 부모 노드가 존재한다면, 부모 노드로 이동한다.
            else:
                current = tree[current].parent
        return record - 1

    print(travel())

# import sys
#
# if __name__ == "__main__":
#     n = int(sys.stdin.readline())
#
#     childs = [0] * (n + 1)
#     parents = [0] * (n + 1)
#     for _ in range(n):
#         p, lc, rc = map(int, sys.stdin.readline().split())
#         childs[p] = (lc, rc)
#         parents[lc] = parents[rc] = p
#
#
#     def travel():
#         current = 1
#         visit = set()
#         visit_cnt = 1  # 방문처리용 카운터 , len(visit)을 매번 호출하면 cost가 크기 때문에 만든 변수
#         record = []
#         while True:
#             record.append(current)
#
#             if childs[current][0] != -1 and childs[current][0] not in visit:
#                 visit.add(childs[current][0])
#                 visit_cnt += 1
#                 current = childs[current][0]
#             elif childs[current][1] != -1 and childs[current][1] not in visit:
#                 visit.add(childs[current][1])
#                 visit_cnt += 1
#                 current = childs[current][1]
#             elif visit_cnt == n:
#                 break
#             else:
#                 current = parents[current]
#         return len(record) - 1
#
#
#     print(travel())
