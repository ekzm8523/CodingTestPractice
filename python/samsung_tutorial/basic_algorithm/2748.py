# https://www.acmicpc.net/problem/2748

# def Fibonacci(num):
#
#     if num == 0:
#         return 0
#     if num == 1 or num == 2:
#         return 1
#     else:
#         return Fibonacci(num - 1) + Fibonacci(num - 2)


if __name__ == "__main__":

    n = int(input())
    dp = [0] * (n + 1)

    dp[1] = 1

    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]

    print(dp[n])