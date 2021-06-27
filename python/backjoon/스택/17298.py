# https://www.acmicpc.net/problem/17298

if __name__ == "__main__":

    N = int(input())
    seq = list(map(int, input().split()))
    stack = []
    NGE = [-1] * N

    stack.append(0)
    i = 1
    while stack and i < N:
        while stack and seq[stack[-1]] < seq[i]:
            NGE[stack[-1]] = seq[i]
            stack.pop()

        stack.append(i)
        i += 1

    for i in range(N):
        print(NGE[i], end=' ')



