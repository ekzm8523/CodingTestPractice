# https://www.acmicpc.net/problem/2579
"""
규
1. 계단은 한 번에 한 계단씩 또는 두 계단씩 오를 수 있다. 즉, 한 계단을 밟으면서 이어서 다음 계단이나, 다음 다음 계단으로 오를 수 있다.
2. 연속된 세 개의 계단을 모두 밟아서는 안 된다. 단, 시작점은 계단에 포함되지 않는다.
3. 마지막 도착 계단은 반드시 밟아야 한다.
"""
if __name__ == "__main__":
    N = int(input())
    seq = 0
    stairs = [int(input()) for _ in range(N)]
    DP = [0 for _ in range(N)]
    DP[0] = stairs[0]
    if N >= 2:
        DP[1] = stairs[0] + stairs[1]
    if N >= 3:
        DP[2] = max(stairs[0] + stairs[2], stairs[1] + stairs[2])
        for i in range(3, N):
            DP[i] = max(DP[i-2] + stairs[i], DP[i-3] + stairs[i-1] + stairs[i])
    print(DP[-1])

