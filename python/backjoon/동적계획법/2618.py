# https://www.acmicpc.net/problem/2618
"""
메모이제이션을 사용
dp[A][B]는 경찰차1은 마지막으로 해결한 사건 번호가 A, 경찰차2는 마지막으로 해결한 사건 번호가 B라는 뜻
그렇다면 다음 사건 번호는 max(A, B) + 1이 된다.
"""
import sys

def calculate_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

if __name__ == "__main__":
    sys.setrecursionlimit(int(1e6))
    n = int(sys.stdin.readline())
    w = int(sys.stdin.readline())
    INF = sys.maxsize
    positions = [(1, 1), (n, n)] + [tuple(map(int, sys.stdin.readline().split())) for _ in range(w)]

    dp = [[-1 for _ in range(w+2)] for _ in range(w+2)]

    def explore(i, j):
        if i > w or j > w:  # 2번부터 사건번호 시작, w + 1에서 사건은 종료될것이다.
            return 0
        if dp[i][j] != -1:
            return dp[i][j]

        tmp = max(i, j) + 1
        ni = explore(tmp, j) + calculate_distance(positions[tmp], positions[i])
        nj = explore(i, tmp) + calculate_distance(positions[tmp], positions[j])
        dp[i][j] = min(ni, nj)
        return dp[i][j]


    def backtracking(x, y):
        if x > w or y > w: return
        nc = max(x, y) + 1
        nx = calculate_distance(positions[nc], positions[x])
        ny = calculate_distance(positions[nc], positions[y])

        if dp[nc][y] + nx < dp[x][nc] + ny:
            print(1)
            backtracking(nc, y)
        else:
            print(2)
            backtracking(x, nc)
        return

    print(explore(0, 1))
    backtracking(0,1)
