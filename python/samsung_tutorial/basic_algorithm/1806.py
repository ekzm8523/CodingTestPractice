# https://www.acmicpc.net/problem/1806
"""
10 < N < 100,000
N 자리수로 만들어진 수열의 부분합중 그 합이 S 이상이 되는 것 중, 가장 짧은 것의 길이를 구하라
"""
import math

if __name__ == "__main__":

    n, s = map(int, input().split())
    sequence = list(map(int, input().split()))

    prefix_sum = [0]

    for i in range(0, n):
        prefix_sum.append(prefix_sum[i] + sequence[i])

    # 여기서 two pointer
    left = right = 0
    answer = math.inf
    while left < n:
        sum_value = prefix_sum[right] - prefix_sum[left]
        if sum_value >= s:
            answer = min(answer, right - left)
            # right == left 일때는 0이라서 left가 right를 넘어설 일이 없다.
            left += 1
        elif sum_value < s:
            if right == n:
                break
            right += 1
    if s == 0:
        print(1)
    else:
        print(0 if answer == math.inf else answer)
"""
10 100
5 1 3 5 10 7 4 9 2 8
"""