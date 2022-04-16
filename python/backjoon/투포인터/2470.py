"""
용액 [-1,000,000,000, 1,000,000,000]
혼합 -> 특성값의 합
특성값을 0에 가깝게 만들기
[-2, 4, -99, -1, 98] -> -99 + 98 = -1
"""
import sys

input = lambda: sys.stdin.readline().strip()
INF = sys.maxsize

if __name__ == '__main__':
    solution_count = int(input())
    solutions = sorted(map(int, input().split()))

    left, right = 0, solution_count - 1
    select_left, select_right = left, right
    answer = INF
    while left < right:
        sum_ = solutions[left] + solutions[right]
        if answer > abs(sum_):
            answer = abs(sum_)
            select_left, select_right = left, right
        if sum_ >= 0:
            right -= 1
        else:
            left += 1

    print(solutions[select_left], solutions[select_right])


"""
5
-2 4 -99 -1 98
"""