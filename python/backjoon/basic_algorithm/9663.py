"""
Queen은 상하좌우 + 대각선 4개 -> 8방향 자유롭게 이동가능
메모리 제한이 128MB라서 분명 메모리초과가 뜰 것이다.
일단 row는 한줄에 하나니까 고려할 필요 없다.
그렇다면 고려해야할건 column과 대각선인데
만약 n = 5, visit = (2, 3)이라고 치면 우측 대각선은 y-x == 1이라면 우측대각선이다.
좌측 대각선은 (3,2), (4,1), (5,0)은 두개 합이 같다면?

"""

if __name__ == "__main__":

    n = int(input())
    answer = 0
    slash_right = [False] * (n + n)
    slash_left = [False] * (n + n)
    col_visit = [False] * n
    def dfs(row):
        global answer
        for col in range(n):
            if col_visit[col] or slash_right[col-row] or slash_left[col+row]:
                continue
            col_visit[col] = slash_right[col - row] = slash_left[col + row] = True
            if row == n - 1:
                answer += 1
            else:
                dfs(row+1)
            col_visit[col] = slash_right[col - row] = slash_left[col + row] = False
    dfs(0)
    print(answer)
