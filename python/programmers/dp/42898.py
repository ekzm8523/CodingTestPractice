# https://programmers.co.kr/learn/courses/30/lessons/42898
def solution(m, n, puddles):
    table = [[1] * m for _ in range(n)]
    for x, y in puddles:
        table[y-1][x-1] = 0
    dp = [[0] * m for _ in range(n)]
    dp[0][0] = 1

    for row in range(n):
        for col in range(m):

            if table[row][col] == 0:  # 물이면 no check
                continue
            if 0 < row and table[row-1][col]:
                dp[row][col] += dp[row-1][col]
            if 0 < col and table[row][col-1]:
                dp[row][col] += dp[row][col-1]
    return dp[-1][-1] % 1000000007


if __name__ == '__main__':
    m = 4
    n = 3
    puddles = [[2, 2]]
    print(solution(m, n, puddles))