# https://www.acmicpc.net/problem/11404
import sys


if __name__ == "__main__":
    INF = sys.maxsize
    n = int(input())
    m = int(input())

    FW_table = [[INF] * n for _ in range(n)]

    for i in range(m):
        start, end, cost = map(int, input().split())
        FW_table[start - 1][end - 1] = min(cost, FW_table[start - 1][end - 1])

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                if FW_table[i][j] > FW_table[i][k] + FW_table[k][j]:
                    FW_table[i][j] = FW_table[i][k] + FW_table[k][j]


    for row in FW_table:
        for col in row:
            if col == INF:
                print(0, end=" ")
            else:
                print(col, end=" ")
        print()