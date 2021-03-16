#
# def main():
#     nodes = input().split()
#     n = int(input())
#     edges = []
#     for i in range(n):
#         new_edge = input().split()
#         for edge in edges:
#             for j in range(len(edge)):
#                 if new_edge[j] == edge:
#                     new_edge = edge[0:j] + new_edge[j:]
#         edges.append(new_edge)
#         print(edges)
#
#
#     print(nodes)
#
#     skill = [edges[0]]
#
#
#
#
#
#
#
#
#
#
#
#
#
# # if __name__=="__main__":
# #     main()
# #
# # """
# # h g f w r
# # 4
# # h g
# # h f
# # g r
# # g w
# # """
#
# # def main():
# #     p, n, h = map(int,input().split())
# #     reser_list = []
# #     for _ in range(n):
# #         pc, time = map(int,input().split())
# #         reser_list.append([pc,time])
# #     answer = {}
# #     for i in range(n):
# #         if reser_list[i][1] <= h:
# #             if reser_list[i][0] not in answer:
# #                 answer[reser_list[i][0]] = reser_list[i][1]
# #             else:
# #                 answer[reser_list[i][0]] += reser_list[i][1]
# #
# #     for i in range(1,p+1):
# #         if i in answer:
# #             print(i, answer[i]*1000)
# #         else:
# #             print(i,0)
# # INF = 10001
# # def binary_search(target, data):
# #     data.sort()
# #     start = 0
# #     end = len(data) - 1
# #
# #     while start <= end:
# #         mid = (start + end) // 2
# #
# #         if data[mid] == target:
# #             return mid # 함수를 끝내버린다.
# #         elif data[mid] < target:
# #             start = mid + 1
# #         else:
# #             end = mid -1
# #     return None
# #
# # def main():
# #     n, m, e = map(int, input().split())
# #     pinut_pos = list(map(int, input().split()))
# #     left_idx, right_idx = 0,n
# #     eat_cnt = 0
# #     for i in range()
# #     while eat_cnt < m:
# #         for i in range(n):
# #             if pinut_pos[i] < left:
#
# # answer = 0
# #
# # def dfs(array, idx, visited,n,cnt):
# #     if visited[idx]:
# #         global answer
# #         answer = max(answer,cnt)
# #         return
# #
# #     visited[idx] = True
# #     next = idx + array[idx]
# #     if next < 0 or next >= n: return # out of index
# #     dfs(array, next, visited,n,cnt+1)
# #
# # def main():
# #     n = int(input())
# #     array = list(map(int,input().split()))
# #     check = [False] * n
# #     dfs(array,0,check,n,1)
# #     check = [False] * n
# #     dfs(array,1,check,n,1)
# #     check = [False] * n
# #     dfs(array,2,check,n,1)
# #     print(answer)
#
# if __name__=="__main__":
#     main()
#
# """
# 2 7 4
# 1 10
# 1 5
# 1 7
# 2 10
# 2 1
# 2 3
# 2 7
#
# """
cnt = 0
for i in range(0,12):
    for j in range(0,60):
        if i - j == 15 or i - j == -15:
            cnt+=1
print(cnt)
