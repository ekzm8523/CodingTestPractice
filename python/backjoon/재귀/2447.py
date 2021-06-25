# https://www.acmicpc.net/problem/2447

def draw_star(n):
    global table

    if n == 3:
        table[0][:3] = table[2][:3] = [1]*3
        table[1][:3] = [1, 0, 1]
        return

    a = n // 3
    draw_star(a)
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                continue
            for k in range(a):
                table[a * i + k][a * j:a * (j + 1)] = table[k][:a]


if __name__ == "__main__":
    n = int(input())    # 3, 27, 81 ...
    table = [[0 for i in range(n)] for i in range(n)]
    draw_star(n)
    for row in table:
        for value in row:
            if value:
                print('*', end = '')
            else:
                print(' ', end = '')
        print()