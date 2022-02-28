# https://programmers.co.kr/learn/courses/30/lessons/42895?language=python3
"""
dp[2] -> dp[1] *,-,+,/ dp[1]
dp[3] -> dp[1] *,-,+,/ dp[2]
dp[4] -> dp[1] *,-,+,/ dp[3], dp[2] *,-,+,/ dp[2]
dp[5] -> dp[1] * dp[4], dp[2] * dp[3]
"""
from math import ceil

def solution(N, number):
    if N == number:
        return 1
    dp = [None] + [set() for _ in range(8)]

    dp[1].add(N)

    for i in range(2, 9):
        dp[i].add(int(str(N) * i))  # i == 2 , N == 5 -> 55

        for j in range(1, i):
            for num1 in dp[j]:
                for num2 in dp[i-j]:
                    dp[i].add(num1 * num2)
                    if num2 != 0:
                        dp[i].add(num1 // num2)
                    dp[i].add(num1 + num2)
                    dp[i].add(num1 - num2)

        if number in dp[i]:
            return i
    return -1


if __name__ == '__main__':
    # n = 5
    # numbers = 12
    # print(solution(n, numbers))

    n = 2
    numbers = 11
    print(solution(n, numbers))
