# https://www.acmicpc.net/problem/15486
"""
dp[1][0] -> 1번째 상담을 했을때 최댓 값 -> T[1]은 3이므로 dp[4][1], dp[4][0] 둘중 큰놈 + P[1]
dp[1][1] -> 1번째 상담을 안했을 때 최댓 값 -> dp[2][0]과 dp[2][1] 둘중 큰놈
뒤에서부터 계산 ( 탑 다운 )
"""
import sys

def is_valid_idx(idx):
    return 0 < idx <= n

def is_valid_day(day):
    return day <= n + 1

if __name__ == "__main__":
    n = int(sys.stdin.readline())

    T = [None]
    P = [None]
    for _ in range(n):
        t, p = map(int, sys.stdin.readline().split())
        T.append(t)
        P.append(p)
    dp = [None] + [0] * n

    # day + T[day] -> 끝나는 날
    for day in range(n, 0, -1):
        end_point = day + T[day]
        # 포함할 때
        if is_valid_day(end_point): # 포함할 수 있는지 검사
            if is_valid_idx(end_point):
                dp[day] = P[day] + dp[end_point]
            else:
                dp[day] = P[day]

        # 포함하지 않을 때
        if is_valid_idx(day + 1):
            dp[day] = max(dp[day + 1], dp[day])
    print(dp[1])








