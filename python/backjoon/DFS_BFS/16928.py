# https://www.acmicpc.net/problem/16928
import sys
from collections import deque

input = lambda: sys.stdin.readline().strip()

if __name__ == '__main__':
    N, M = map(int, input().split())
    ladders = {}
    snakes = {}
    dp = [1000] * 101

    for _ in range(N):
        a, b = map(int, input().split())
        ladders[a] = b
    for _ in range(M):
        a, b = map(int, input().split())
        snakes[a] = b

    q = deque()
    dp[1] = 0
    q.append((1, 0))
    answer = None
    while q:
        cur, dis = q.popleft()
        for jump in range(1, 7):
            next_ptr = cur + jump
            if next_ptr > 100:
                break
            if next_ptr in ladders:
                if dp[ladders[next_ptr]] > dis + 1:
                    dp[ladders[next_ptr]] = dis + 1
                    q.append((ladders[next_ptr], dis + 1))
            elif next_ptr in snakes:
                if dp[snakes[next_ptr]] > dis + 1:
                    dp[snakes[next_ptr]] = dis + 1
                    q.append((snakes[next_ptr], dis + 1))
            elif dp[next_ptr] > dis + 1:
                dp[next_ptr] = dis + 1
                q.append((next_ptr, dis + 1))

    print(dp[100])

