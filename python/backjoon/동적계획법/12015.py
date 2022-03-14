# https://www.acmicpc.net/problem/12015
"""
기존의 LIS가 N^2으로 돌았던 이유는 I보다 작은 친구들을 다 돌았기 때문
"""
import sys
from bisect import bisect_left

if __name__ == '__main__':
    n = int(input())

    sequence = [0] + list(map(int, input().split()))
    dp = [0] * (n + 1)  # i번째 숫자를 포함했을때 증가수열 크기
    dp2 = [-sys.maxsize]  # i 사이즈의 증가수열중 마지막 숫자 -> 오름차순 되어있을거임

    for i in range(1, n + 1):
        num = sequence[i]  # compare number
        if dp2[-1] < num:  # compare number가 가장 크다면
            dp[i] = len(dp2)  # 0도 포함했기 때문에 size로 최신화 시켜주면 됨
            dp2.append(num)  # 마지막에 추가
        else:
            idx = bisect_left(dp2, num)  # num이 들어갈 수 있는 인덱스
            if dp2[idx] == num:  # 이미 있는 숫자라면
                dp[i] = idx  # 그냥 업데이트
            else:  # 없는 숫자면 그 왼쪽 인덱스와 비교해야함
                idx -= 1
                dp[i] = idx + 1
                dp2[idx + 1] = min(dp2[idx + 1], num)

    print(max(dp))