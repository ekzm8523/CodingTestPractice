# https://www.acmicpc.net/problem/2003
import sys

if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().split())

    nums = list(map(int, sys.stdin.readline().split()))
    answer = 0
    left = 0
    while left < n:
        sum_nums = 0

        for right in range(left, n):
            sum_nums += nums[right]
            if sum_nums > m:
                break
            elif sum_nums == m:
                answer += 1

        left += 1
    print(answer)
