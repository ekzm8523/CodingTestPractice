# https://www.acmicpc.net/problem/2167
import sys

if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().split())

    table = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    prefix_table = [[0] * m for _ in range(n)]
    k = int(sys.stdin.readline())
    for i in range(n):
        prefix_table[i][0] = table[i][0]
        for j in range(1, m):
            prefix_table[i][j] = prefix_table[i][j-1] + table[i][j]
    for j in range(m):
        for i in range(1, n):
            prefix_table[i][j] += prefix_table[i-1][j]

    for _ in range(k):
        i, j, x, y = map(int, sys.stdin.readline().split())

        if i == 1 and j == 1:
            answer = prefix_table[x-1][y-1]
        if i == 1 and j > 1:
            answer = prefix_table[x-1][y-1] - prefix_table[x-1][j-2]
        if i > 1 and j == 1:
            answer = prefix_table[x-1][y-1] - prefix_table[i-2][y-1]
        if i > 1 and j > 1:
            answer = prefix_table[x - 1][y - 1] - prefix_table[x - 1][j - 2] - prefix_table[i - 2][y - 1] + \
                     prefix_table[i - 2][j - 2]
        print(answer)


