from bisect import bisect_left
import sys


def find_increase_cnt(n: int, sequence: list):
    increase_dp = [0] * n
    weight_dp = [-sys.maxsize]

    for i in range(n):
        target = sequence[i]

        if target > weight_dp[-1]:  # 어차피 가장 큰놈이면
            increase_dp[i] = len(weight_dp)
            weight_dp.append(target)
        else:
            idx = bisect_left(weight_dp, target)  # target이 들어갈 수 있는 idx 찾기
            if weight_dp[idx] == target:  # 이미 있는 놈이면
                increase_dp[i] = idx
            else:  # 사잇값이면
                increase_dp[i] = idx
                weight_dp[idx] = target  # 갱신
    return len(weight_dp) - 1


if __name__ == '__main__':
    n = int(sys.stdin.readline())
    sequence = list(map(int, sys.stdin.readline().split()))
    answer = 0
    for i in range(1, n + 1):
        increase_cnt = find_increase_cnt(i, sequence[:i])
        decrease_cnt = find_increase_cnt(n - i + 1, list(map(lambda x: -x, sequence[i-1:])))
        answer = max(answer, increase_cnt + decrease_cnt - 1)

    print(answer)



"""
9
1 5 2 1 4 4 4 2 1
"""