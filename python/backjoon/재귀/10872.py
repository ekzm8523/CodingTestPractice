# https://www.acmicpc.net/problem/10872


def factorial(n, fac):
    if n == 0:
        return fac
    else:
        return n * factorial(n-1, fac)

if __name__ == "__main__":
    n = int(input())
    print(factorial(n, 1))
