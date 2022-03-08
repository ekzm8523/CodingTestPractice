import sys

if __name__ == "__main__":
    node_cnt, edge_cnt = map(int, input().split())

    table = [[sys.maxsize] * (node_cnt) for _ in range(node_cnt)]

    for _ in range(edge_cnt):
        a, b, w = map(int, input().split())
        table[a-1][b-1] = w

    for i in range(node_cnt):
        for j in range(node_cnt):
            for k in range(node_cnt):
                table[i][j] = min(table[i][j], table[i][k] + table[k][j])

    answer = sys.maxsize
    for i in range(node_cnt):
        answer = min(answer, table[i][i])

    print(answer if answer < sys.maxsize else -1)