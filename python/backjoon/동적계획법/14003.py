# https://www.acmicpc.net/problem/14003
from bisect import bisect_right, bisect_left, bisect

if __name__ == '__main__':
    length = int(input())
    sequence = list(map(int, input().split()))
    sequence_dp = []
    dp = [-int(1e10)]  # dp 를 위한 dp

    dp_size = 1
    for value in sequence:
        idx = bisect_left(dp, value)
        if idx == dp_size:
            dp.append(value)
            dp_size += 1
        else:
            dp[idx] = value
        sequence_dp.append(idx)

    idx = dp_size - 1
    print(idx)
    answer = []
    for i in range(length-1, -1, -1):
        if sequence_dp[i] == idx:
            answer.append(sequence[i])
            idx -= 1
    print(*answer[::-1])
