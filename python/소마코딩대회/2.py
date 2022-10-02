import sys
import bisect

input = lambda: sys.stdin.readline().strip()


def main():
    n = int(input())
    coordinates = {}
    x_list = []

    for _ in range(n):
        x, y = map(int, input().split())
        coordinates[x] = y
        x_list.append(x)

    q = int(input())
    for _ in range(q):
        k = float(input())
        idx = bisect.bisect_left(x_list, k)
        dif = coordinates[x_list[idx]] - coordinates[x_list[idx-1]]
        if dif < 0:
            print(-1)
        elif dif > 0:
            print(1)
        else:
            print(0)
if __name__ == '__main__':
    main()