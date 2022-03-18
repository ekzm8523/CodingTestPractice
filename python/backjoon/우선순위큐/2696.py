# https://www.acmicpc.net/problem/2696
"""
min hq와 max hq를 사용해 중앙값 고정
규칙 1. max hq의 최댓값(top)은 항상 min hq의 최솟값(top)보다 작다
규칙 2. min hq의 크기가 1 더 커야함
-> min hp의 top이 중앙값

1. num이 max_hq의 top보다 크면 오른쪽으로 들어가야하니까
min_hq 에 num push
min hq 에서 하나 pop 해와서 max_hq에 push

작으면 왼쪽으로 들어가야하니까
max_hq에 num push
max_hq에서 하나 pop 해와서 min_hq에 push

그리고 min_hq.top출력
"""
import math
from heapq import heappop as pop, heappush as push
import sys

if __name__ == "__main__":


    test_cnt = int(sys.stdin.readline())

    for test_num in range(test_cnt):

        num_cnt = int(sys.stdin.readline())
        nums = []
        for _ in range(math.ceil(num_cnt / 10)):
            nums.extend(list(map(int, sys.stdin.readline().split())))
        answer = [nums[0]]
        left_hq = []  # max hq
        right_hq = [nums[0]]  # min hq

        for i in range(1, num_cnt):
            if right_hq[0] < nums[i]:
                push(right_hq, nums[i])
            else:
                push(left_hq, -nums[i])
                push(right_hq, -pop(left_hq))

            if i % 2 == 0:  # 0부터 시작이라 짝수일때 출력
                push(left_hq, -pop(right_hq))
                answer.append(right_hq[0])

        print(len(answer))

        for i, num in enumerate(answer):
            if i % 10 == 0 and i > 0:  # new row
                print()
            print(num, end=" ")
        print()




"""
3
9
1 2 3 4 5 6 7 8 9
9
9 8 7 6 5 4 3 2 1
23
23 41 13 22 -3 24 -31 -11 -8 -7
3 5 103 211 -311 -45 -67 -73 -81 -99
-33 24 56
"""