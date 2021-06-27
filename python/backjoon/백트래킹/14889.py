# https://www.acmicpc.net/problem/14889

import itertools, sys


if __name__ == "__main__":
    N = int(input())

    S = [list(map(int, input().split())) for _ in range(N)]
    s = [i + 1 for i in range(N)]
    combination = list(itertools.combinations(s, N//2))

    min_diff = sys.maxsize

    for set_a in combination:
        sum_a = sum_b = 0
        for i in set_a:
            for j in set_a:
                if i == j:
                    continue
                sum_a += S[i-1][j-1]
        set_b = set(s) - set(set_a)
        for i in set_b:
            for j in set_b:
                if i == j:
                    continue
                sum_b += S[i - 1][j - 1]
        if min_diff > abs(sum_a - sum_b):
            min_diff = abs(sum_a - sum_b)

    print(min_diff)
