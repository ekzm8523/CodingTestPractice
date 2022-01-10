# https://www.acmicpc.net/problem/1976

if __name__ == '__main__':
    n, m = map(int, input().split())
    l = [tuple(map(int, input().split())) for _ in range(m)]

    print(n, m, l)