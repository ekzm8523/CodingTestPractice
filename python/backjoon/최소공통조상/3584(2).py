# https://www.acmicpc.net/problem/3584
import sys

if __name__ == "__main__":

    T = int(sys.stdin.readline())
    for _ in range(T):
        n = int(sys.stdin.readline())
        parents = [None] * (n + 1)

        for _ in range(n - 1):
            a, b = map(int, sys.stdin.readline().split())
            parents[b] = a

        a, b = map(int, sys.stdin.readline().split())

        list_a = [a]
        while parents[a] != None:
            list_a.append(parents[a])
            a = parents[a]
        list_b = [b]
        while parents[b] != None:
            list_b.append(parents[b])
            b = parents[b]

        idx_a = len(list_a) - 1
        idx_b = len(list_b) - 1
        answer = None
        while idx_a >= 0 and idx_b >= 0:
            if list_a[idx_a] != list_b[idx_b]:
                break
            answer = list_a[idx_a]
            idx_a -= 1
            idx_b -= 1
        print(answer)






