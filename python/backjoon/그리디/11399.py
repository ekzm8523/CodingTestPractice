# https://www.acmicpc.net/problem/11399

if __name__ == "__main__":
    N = int(input())
    P = sorted(list(map(int, input().split())))

    answer = 0
    for i in range(N):
        answer += (N - i) * P[i]

    print(answer)