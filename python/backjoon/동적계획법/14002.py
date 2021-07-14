# https://www.acmicpc.net/problem/14002

from bisect import bisect_left

"""
bisect_left의 특징
같은 값이 있으면 그 index를 return
같은 값이 여러개면 가장 왼쪽의 index를 return
같은 값이 없으면 그 값보다 한단계 큰 value의 index를 return
마지막 값보다 찾는 값이 크면 Len을 return 해주기 때문에 예외처리 해주어야 out of index가 안뜸
"""
if __name__ == "__main__":
    # n = int(input())
    #
    # l = list(map(int, input().split()))
    l = [3, 5, 7, 9, 2, 1, 4, 8]
    n = len(l)
    dp1 = [0] * n   # list의 값까지의 최대 부분 수열 DP
    dp2 = [0]    # 최대 부분 수열을 찾기 위해 탐색할 DP dp2[1] -> dp1의 값이 1인 list value의 최솟값

    size = 0
    for i in range(n):
        # if dp2[-1] < l[i]: # 가장 마지막에 나온 값보다 증가하는 수열이면
        #     dp2.append(l[i]) # dp2[size + 1] = l[i]
        #     dp1[i] = size + 1 # size = len(dp2)와 같음
        #     size += 1 # append 해주었으니 size 하나 늘려주기
        #
        # else:
        idx = bisect_left(dp2, l[i]) - 1 # dp2[idx] == l[i]인 경우와 dp2[idx] > l[i]인 경우로 나뉨
        # 하지만 더 작은 경우만 생각해야 하므로 같든 작든 둘다 idx - 1로 찾아야함
        dp1[i] = size + 1
        size += 1
        dp2.append(l[idx])
        if dp2[idx] > l[i]: # 최솟값으로 업데이트
            dp2[idx] = l[i]
    print(dp2)
    print(dp1)

# if __name__ == "__main__":
#
#     n = int(input())
#     arr = list(map(int, input().split()))
#     dp = [1] * n
#     for i in range(1, n):
#         for j in range(i):
#             if arr[i] > arr[j]:
#                 dp[i] = max(dp[i], dp[j]+1)
#     print(max(dp))
#     order = max(dp)
#     lst = []
#     for i in range(n-1, -1, -1):
#         if dp[i] == order:
#             lst.append(arr[i])
#             order -= 1
#     lst.reverse()
#     for i in lst:
#         print(i, end=' ')
#     print()
#
