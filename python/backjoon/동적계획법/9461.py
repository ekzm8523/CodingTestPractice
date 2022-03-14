import sys

if __name__ == '__main__':
    test_cnt = int(sys.stdin.readline())

    nums = [int(sys.stdin.readline()) for _ in range(test_cnt)]
    max_num = max(nums)

    dp = [0, 1, 1, 1, 2, 2]

    for i in range(6, max_num + 1):
        dp.append(dp[i-1] + dp[i-5])

    for num in nums:
        print(dp[num])