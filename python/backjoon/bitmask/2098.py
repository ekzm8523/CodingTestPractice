import sys
import math
input = lambda: sys.stdin.readline().strip()


if __name__ == "__main__":
    city_cnt = int(input())

    dp = [[math.inf] * (1 << city_cnt) for _ in range(city_cnt)]
    matrix = [tuple(map(int, input().split())) for _ in range(city_cnt)]

    def tsp(current, visited):
        if visited == (1 << city_cnt) - 1:
            return matrix[current][0] or math.inf

        if dp[current][visited] != math.inf:
            return dp[current][visited]

        for city in range(city_cnt):
            if visited & (1 << city) == 0 and matrix[current][city] != 0:
                dp[current][visited] = min(
                    dp[current][visited],
                    tsp(city, visited | (1 << city)) + matrix[current][city]
                )
        return dp[current][visited]
    print(tsp(0, 1 << 0))
