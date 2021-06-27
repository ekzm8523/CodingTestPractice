# https://www.acmicpc.net/problem/11047

if __name__ == "__main__":
    N, K = list(map(int, input().split()))
    coin = [int(input()) for _ in range(N)]
    cnt = 0

    for i in range(N-1, -1, -1):
        mod = (K // coin[i])
        cnt += mod
        K -= (mod * coin[i])
        if K == 0:
            break
    print(cnt)
