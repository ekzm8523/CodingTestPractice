# https://www.acmicpc.net/problem/1655

import sys, heapq

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    left, right = [], []

    for i in range(N):
        num = int(sys.stdin.readline())
        if len(left) == len(right):
            heapq.heappush(left, -num)
        else:
            heapq.heappush(right, num)

        if right and -left[0] > right[0]:
            left_value = -heapq.heappop(left)
            right_value = heapq.heappop(right)
            heapq.heappush(left, -right_value)
            heapq.heappush(right, left_value)
        print(-left[0])


