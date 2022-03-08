import sys


if __name__ == '__main__':
    node_cnt = int(input())
    edge_cnt = int(input())

    table = [[sys.maxsize] * node_cnt for _ in range(node_cnt)]
    for _ in range(edge_cnt):
        a, b, w = map(int, input().split())
        table[a-1][b-1] = min(table[a-1][b-1], w)

    for k in range(node_cnt):
        for i in range(node_cnt):
            for j in range(node_cnt):
                if i == j:
                    continue
                table[i][j] = min(table[i][j], table[i][k] + table[k][j])

    for row in table:
        for col in row:
            print(0 if col == sys.maxsize else col, end=" ")
        print()