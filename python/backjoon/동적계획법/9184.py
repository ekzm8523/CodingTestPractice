import sys

if __name__ == '__main__':

    num = int(sys.stdin.readline())
    if 1 <= num <= 2:
        print(num)
    else:
        first = 1
        second = 2

        for _ in range(num - 2):
            third = (first + second) % 15746
            first, second = second, third
        print(third % 15746)

