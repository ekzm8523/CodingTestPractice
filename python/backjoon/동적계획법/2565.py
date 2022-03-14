# https://www.acmicpc.net/problem/2565
import sys
from bisect import bisect_left
"""
전깃줄이 교차하는 경우는 다음과 같다
(x1, y1), (x2, y2)가 교차하지 않는 경우는 
x1 > x2 -> y1 > y2
x1 < x2 -> y1 < y2 
이어야한다. -> 증가하면 같이 증가하고 감소하면 같이 감소해야 안겹칩
그럼 x를 기준으로 오름차순으로 해놓으면 y들의 증가하는 부분수열의 크기를 찾는 문제와 같아진다.
"""

if __name__ == '__main__':
    wire_cnt = int(sys.stdin.readline())

    wires = [tuple(map(int, sys.stdin.readline().split())) for _ in range(wire_cnt)]
    wires.sort()
    b_numbers = tuple(map(lambda x: x[1], wires))
    increase_dp = [0] * len(b_numbers)
    weight_dp = [0]

    for i in range(wire_cnt):
        target = b_numbers[i]
        if target > weight_dp[-1]:
            increase_dp[i] = len(weight_dp)
            weight_dp.append(target)
        else:
            idx = bisect_left(weight_dp, target)
            if weight_dp[idx] == target:  # 이미 존재하는 target이라면
                increase_dp[i] = idx  # 복붙
            else:  # 사잇값이면
                increase_dp[i] = idx
                weight_dp[idx] = target  # 갱신 (어차피 target이 더 작음)
    remain_wire_cnt = len(weight_dp) - 1
    print(wire_cnt - remain_wire_cnt)