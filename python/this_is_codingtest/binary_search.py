
# from bisect import bisect_left, bisect_right
#
# def count_by_range(array, left_value, right_value):
#     right_index = bisect_right(array, right_value)
#     left_index = bisect_left(array, left_value)
#     return right_index - left_index
#
# print(count_by_range([1,2,3,3,4],1,4))

# n, m = map(int,input().split())
# d_list = list(map(int,input().split()))
# d_list.sort(reverse=True)
#
# size = len(d_list)
#
# low = 0
# high = d_list[0]
# sum = 0
# while low < high:
#     sum = 0
#     mid = (low + high) // 2
#
#     for i in range(size):
#         if d_list[i] > mid:
#             sum += d_list[i]-mid
#         else:
#             break
#
#     if sum == m:
#         break
#     elif sum > m:
#         low = mid+1
#     else:
#         high = mid-1
# print(mid)
#





