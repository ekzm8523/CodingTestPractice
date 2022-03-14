# https://www.acmicpc.net/problem/2156
"""
조건 -> 연속으로 3잔은 마실 수 없다.
dp[i][0] : i번째를 안마셨을 때의 최댓값 -> 이전 dp값의 최댓값
dp[i][1] : i번째를 마셨을 때의 최댓값
 case 1 : 2번째 전의 잔을 안마셨을때 -> dp[i-2] + nums[i-1] + nums[i]
 case 2 : 1번째 전의 잔을 안마셨을때 -> dp[i-1][0]
"""
import sys

if __name__ == '__main__':
    test_cnt = int(sys.stdin.readline())
    dp = [[0, 0] for _ in range(test_cnt)]
    nums = [int(sys.stdin.readline()) for _ in range(test_cnt)]

    dp[0][1] = nums[0]
    if test_cnt > 1:
        dp[1][0] = nums[0]
        dp[1][1] = nums[0] + nums[1]
        for i in range(2, test_cnt):
            dp[i][0] = max(dp[i-1])
            dp[i][1] = nums[i] + max((dp[i-2][0] + nums[i-1], dp[i-1][0]))

    print(max(dp[test_cnt-1]))