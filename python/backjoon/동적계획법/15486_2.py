# https://www.acmicpc.net/problem/15486

# 1일부터 도는데 그날 상담을 하는 경우 안하는 경우 두개로 나뉜다.
import sys

if __name__ == "__main__":

    consulting_cnt = int(sys.stdin.readline())
    consulting_list = [tuple(map(int, sys.stdin.readline().split())) for _ in range(consulting_cnt)]
    dp = [0] * (consulting_cnt + 1)
    max_weight = 0
    for day in range(consulting_cnt):
        take_days, weight = consulting_list[day]
        # 오늘 상담을 하는 경우
        max_weight = max(max_weight, dp[day])
        if day + take_days <= consulting_cnt:
            dp[day + take_days] = max(dp[day + take_days], max_weight + weight)

    print(max(dp[-1], max_weight))

