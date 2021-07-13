
"""
규칙 1. i+1번째 이진수가 1이고 i+2번째부터 전부 0이면 i번째 이진수를 0으로 변경
규칙 2. 제한없이 맨 오른쪽 자리를 변경합니다.
13
1101 -> 0000
num
dp[num] = min(dp[규칙1(num)], dp[규칙2(num)], dp[num])

bitmask
bit shake it
sibal

"""


# def binary2int(bin_num):
#     size = len(bin_num)
#     bin_num = int(bin_num)
#     num = 0
#
#     for i in range(size):
#         v = bin_num % 10
#         num += v * (2**i)
#         bin_num //= 10
#     return num
#
#
# def Condition2(num):
#     bin_num = bin(num)[2:]
#     if bin_num[-1] == '0':
#
#
# def Condition1(num):
#     bin_num = bin(num)[2:]
#     idx = bin_num.rfind('1') - 1
#     size = len(bin_num)
#     ch_num =
#
# def bin_dp(num):
#     n1 = Condition1(num)
#     n2 =
#
#
# def minOperations(n):
#
#     dp = [0] * INF
#     bin_arr = bin(n)[2:]
#
#
# if __name__ == "__main__":
#     minOperations(13)
#     minOperations(11)



"""
#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'minOperations' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#

def minOperations(n):
    # Write your code here
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = minOperations(n)

    fptr.write(str(result) + '\n')

    fptr.close()

"""