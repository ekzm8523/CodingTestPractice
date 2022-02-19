# # https://programmers.co.kr/learn/courses/30/lessons/92343
# from collections import deque
# # DFS(현재 노드 번호, 양의 수, 늑대의 수, 다음으로 방문할 수 있는 노드의 집합)
#
#
#
#
# def solution(info, edges):
#     size = len(info)
#     answer = -1
#     graph = [[] for _ in range(size)]
#     for a, b in edges:
#         graph[a].append(b)
#
#     def dfs(current_node, sheep_cnt, wolf_cnt, remain_node_set):
#
#         if info[current_node] == 0:  # 양일때
#             remain_node_set.remove(current_node)
#             sheep_cnt += 1ㅅ
#         else:  # 늑대일때
#             if wolf_cnt < sheep_cnt - 1:
#                 wolf_cnt += 1
#                 remain_node_set.remove(current_node)
#
#         for child_node in graph[current_node]:
#             if info[child_node] == 0:
#                 remain_node_set.remove(child_node)
#                 dfs(child_node, )
#
#         # for child_node in graph[current_node]:
#         #     if info[child_node] == 0: # 양일때
#         #         remain_node_set.remove(child_node)
#         #         dfs(child_node, )
#         #     else:  # 늑대일때
#         #         ...
#
#     dfs(0, 0, 0, set(range(len(info))))
#
#
#
# if __name__ == '__main__':
#     input_info = [0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1]
#     input_edges = [[0, 1], [1, 2], [1, 4], [0, 8], [8, 7], [9, 10], [9, 11], [4, 3], [6, 5], [4, 6], [8, 9]]
#     print(solution(input_info, input_edges))
#
#     input_info = [0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0]
#     input_edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 8], [6, 9], [9, 10]]
#     print(solution(input_info, input_edges))
