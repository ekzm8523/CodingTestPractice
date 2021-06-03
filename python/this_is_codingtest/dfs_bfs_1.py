
def dfs(table, x, y):
    if x <= -1 or x >= len(table) or y <= -1 or y >= len(table[0]):
        return False

    if table[x][y] == 0:
        table[x][y] = 1
        dfs(table, x - 1, y)
        dfs(table, x + 1, y)
        dfs(table, x, y - 1)
        dfs(table, x, y + 1)

        return True
    return False

if __name__ == "__main__":
    n, m = map(int, input().split())

    table = []
    check_table = []
    for i in range(n):
        table.append(list(map(int, input())))

    result = 0
    for i in range(n):
        for j in range(m):
            if table[i][j] != 1 and dfs(table, i, j) == True:
                result += 1

    print(result)
