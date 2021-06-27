# https://www.acmicpc.net/problem/9663
"""
이차원 배열을 통해 퀸을 검증하면 시간 초과가 나오므로 이차원 배열을 쓰지 않는 방식으로 풀이
row는 어차피 하나씩 놓으면 되니까 검증을 안해도 된다.
column과 대각선 slash, 역대각선 back_slash 세가지만 구별하면 되는데
column은 N짜리 배열
slash는 (x, y)가 있다고 칠때 대각선은 x + y가 같다면 대각선으로 볼 수 있다.
bask_slash 는 위와 비슷한 방법으로 (x, y) 에서 x와 y의 차이가 같으면 대각선상에 있다.

"""
def n_queen(row):
    global N, col, slash, back_slash, case
    if row == N:
        case += 1
        return

    for j in range(N):
        if not (col[j] or slash[row + j] or back_slash[row - j + N - 1]):
            col[j] = slash[row + j] = back_slash[row - j + N - 1] = True
            n_queen(row + 1)
            col[j] = slash[row + j] = back_slash[row - j + N - 1] = False

if __name__ == "__main__":
    N = int(input())
    col = [False] * N
    slash = [False] * (2 * N - 1)
    back_slash = [False] * (2 * N - 1)
    case = 0
    n_queen(0)

    print(case)

