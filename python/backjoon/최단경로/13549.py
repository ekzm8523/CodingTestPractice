import sys
from heapq import heappush as push, heappop as pop

input = lambda: sys.stdin.readline().strip()
INF = 100_001

if __name__ == '__main__':

    subin_point, sister_point = map(int, input().split())
    max_point = 100_000
    dp = [INF] * (max_point + 1)
    dp[subin_point] = 0
    hq = [(0, subin_point)]

    while hq:
        t, pos = pop(hq)
        if pos == sister_point:
            print(t)
            break
        if t > dp[pos]:  # 이미 방문한겨
            continue

        if pos * 2 <= max_point and dp[pos * 2] > t:
            dp[pos * 2] = t
            push(hq, (t, pos * 2))
        t += 1
        if pos + 1 <= max_point and dp[pos + 1] > t:
            dp[pos + 1] = t
            push(hq, (t, pos + 1))

        if pos - 1 >= 0 and dp[pos - 1] > t:
            dp[pos - 1] = t
            push(hq, (t, pos - 1))
