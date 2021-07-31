
import sys
from math import log2
if __name__ == "__main__":

    m = int(sys.stdin.readline())

    bin_dp = [[0] * (m + 1) for _ in range(20)] # bin_dp.shape -> (depth, m + 1)
    bin_dp[0] = [None] + list(map(int, sys.stdin.readline().split()))

    q = int(sys.stdin.readline())

    # initialization
    for depth in range(1, 20):
        for n in range(1, m + 1):
            bin_dp[depth][n] = bin_dp[depth-1][bin_dp[depth-1][n]]
    # -> f_4(3) -> f_2(f_2(3))
    for _ in range(q):
        n, x = map(int, sys.stdin.readline().split())

        while n > 0:
            depth = int(log2(n & -n)) # 맨 마지막으로 나오는 1의 위치
            # print(f"n -> {n} , delete -> {n & -n}")
            x = bin_dp[depth][x]
            n -= (n & -n)
        # print("-" * 50)
        print(x)
