# https://www.acmicpc.net/problem/10942
"""
1 2 1 3 1 2 1
1~5가 팰린드롬일려면 2~4가 팰린드롬이어야한다.
0 : 아직 미정
-1 : 무조건 팰린드롬 아님
1 : 팰린드롬

"""
import sys

input = lambda: sys.stdin.readline().strip()


class PalindromeEnum:
    SUCCESS = 1
    FAIL = 0
    UNKNOWN = -1


if __name__ == '__main__':
    array_size = int(input())
    arr = [None] + list(map(int, input().split()))
    dp = [[-1] * (array_size + 1) for i in range(array_size + 1)]
    query_size = int(input())
    for _ in range(query_size):
        start, end = map(int, input().split())
        tmp_start, tmp_end = start, end
        flag = PalindromeEnum.UNKNOWN

        while tmp_start < tmp_end and tmp_end - tmp_start > 2:
            if dp[tmp_start][tmp_end] == PalindromeEnum.UNKNOWN:
                tmp_start += 1
                tmp_end -= 1
            elif dp[tmp_start][tmp_end] == PalindromeEnum.SUCCESS:
                flag = PalindromeEnum.SUCCESS
                break
            else:
                flag = PalindromeEnum.FAIL
                break
        while tmp_start >= start:
            flag = PalindromeEnum.SUCCESS if flag and arr[tmp_start] == arr[tmp_end] else PalindromeEnum.FAIL
            dp[tmp_start][tmp_end] = flag
            tmp_start -= 1
            tmp_end += 1

        print(flag)