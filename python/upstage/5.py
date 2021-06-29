
from collections import deque

class ProblemPy:

    @staticmethod
    def solve(n, e, companies, subway_map):
        # IMPLEMENT HERE
        visited = [False] * n
        q = deque()

        # graph = [[] for _ in range(n+1)]

        # for i in range(n):
        #     for j in range(n):
        #         if subway_map[i][j] > 0:
        #             graph[i+1].append(j+1)

        q.append((0, 0, [0]))
        answer_list = []
        while q:
            current_node, cnt, visit_list = q.popleft()
            if current_node == e-1:
                answer_list.append(visit_list)
                break
            for i in range(n):
                if not visited[i]:
                    visited[i] = True
                    visit_list.append(i)
                    q.append((i, cnt+1, visit_list))

        print(q)



        transfer = 0
        dist = 0
        return transfer, dist


if __name__ == "__main__":
    # DO NOT MODIFY FROM HERE
    n = 6
    e = 3
    companies = [0, 1, 1, 0, 1, 0]
    subway_map = [[0, 3, 1, 0, 10, 0],
                  [3, 0, 0, 15, 0, 0],
                  [1, 0, 0, 0, 0, 1],
                  [0, 15, 0, 0, 10, 0],
                  [10, 0, 0, 10, 0, 1],
                  [0, 0, 1, 0, 1, 0]]
    print(ProblemPy.solve(n, e, companies, subway_map))