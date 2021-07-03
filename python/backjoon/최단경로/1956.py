# https://www.acmicpc.net/problem/1956

"""
최단 경로의 사이클 찾기
"""
INF = 10001

if __name__ == "__main__":
    V, K = map(int, input().split())

    FW_table = [[INF] * (V+1) for _ in range(V+1)]

    for i in range(1, K+1):
        start, end, length = map(int, input().split())
        FW_table[start][end] = length

    for k in range(1, V+1):
        for i in range(1, V+1):
            for j in range(1, V+1):
                if FW_table[i][j] > FW_table[i][k] + FW_table[k][j]:
                    FW_table[i][j] = FW_table[i][k] + FW_table[k][j]
    answer = INF

    for i in range(1, V+1):
        answer = min(FW_table[i][i], answer)
    if answer == INF:
        answer = -1
    print(answer)
