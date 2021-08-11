# https://www.acmicpc.net/problem/1920

from bisect import bisect_left

def binary_search(A, q, n):
    left, right = 0, n - 1
    while left <= right:
        mid = (left + right) // 2
        if A[mid] == q:
            return 1
        elif A[mid] > q:
            right = mid - 1
        elif A[mid] < q:
            left = mid + 1
    return 0


def solution2():
    n = int(input())
    A = sorted(list(map(int, input().split())))

    m = int(input())
    Q = list(map(int, input().split()))

    for q in Q:
        print(binary_search(A, q, n))


def solution1():
    n = int(input())
    A = set(map(int, input().split()))

    m = int(input())
    Q = list(map(int, input().split()))

    for q in Q:
        if q in A:
            print(1)
        else:
            print(0)

if __name__ == "__main__":

    solution1()
    solution2()



