# https://www.acmicpc.net/problem/1744

import sys
from bisect import bisect_right

def solution(N, nums):

    answer = 0

    stop_idx = bisect_right(nums, 0)  # 처음으로 0보다 큰 num의 idx를 반환
    i = 0
    while i < stop_idx:
        if stop_idx - i == 1:
            answer += nums[i]
            i += 1
            break
        answer += (nums[i] * nums[i+1])
        i += 2

    stop_idx = i-1
    i = N-1
    while i > stop_idx:
        if i - stop_idx == 1:
            answer += nums[i]
            break
        if nums[i] == 1 or nums[i-1] == 1:
            answer += nums[i]
            i -= 1
            continue
        answer += (nums[i] * nums[i-1])
        i -= 2
    return answer


if __name__ == "__main__":

    N = int(sys.stdin.readline())
    nums = sorted([int(sys.stdin.readline()) for _ in range(N)])

    print(solution(N, nums))
