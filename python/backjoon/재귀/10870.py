# https://www.acmicpc.net/problem/10870

def Fibonacci(n):
    if n == 0 or n == 1:
        return n
    return Fibonacci(n-1) + Fibonacci(n-2)


if __name__ == "__main__":
    n = int(input())
    print(Fibonacci(n))