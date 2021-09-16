import sys
from collections import defaultdict

if __name__ == "__main__":

    t = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    A = list(map(int, sys.stdin.readline().split()))
    m = int(sys.stdin.readline())
    B = list(map(int, sys.stdin.readline().split()))

    A_sum = defaultdict(int)
    B_sum = defaultdict(int)

    for i in range(n):
        sum_value = 0
        for j in range(i, n):
            sum_value += A[j]
            A_sum[sum_value] += 1

    for i in range(m):
        sum_value = 0
        for j in range(i, m):
            sum_value += B[j]
            B_sum[sum_value] += 1

    answer = 0

    for key in A_sum.keys():
        answer += B_sum[t - key] * A_sum[key]
    print(answer)