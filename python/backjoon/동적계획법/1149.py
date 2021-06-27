# https://www.acmicpc.net/problem/1149

if __name__ == "__main__":
    N = int(input())
    RGB_list = [list(map(int, input().split())) for _ in range(N)]

    for i in range(1, N):
        RGB_list[i][0] = min(RGB_list[i-1][1], RGB_list[i-1][2]) + RGB_list[i][0]
        RGB_list[i][1] = min(RGB_list[i - 1][0], RGB_list[i - 1][2]) + RGB_list[i][1]
        RGB_list[i][2] = min(RGB_list[i - 1][0], RGB_list[i - 1][1]) + RGB_list[i][2]

    print(min(RGB_list[N-1]))