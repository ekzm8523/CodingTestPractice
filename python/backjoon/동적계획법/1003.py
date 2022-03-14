import sys

if __name__ == '__main__':

    test_cnt = int(sys.stdin.readline())

    nums = [int(sys.stdin.readline()) for _ in range(test_cnt)]
    max_num = max(nums)
    dp = [(1, 0), (0, 1)]

    for i in range(2, max_num + 1):
        dp.append((dp[i-2][0] + dp[i-1][0], dp[i-2][1] + dp[i-1][1]))

    for num in nums:
        print(*dp[num])