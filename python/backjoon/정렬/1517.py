import sys
input = lambda: sys.stdin.readline().strip()


def merge(start, end):
    global answer, arr, buffer
    mid = (start + end) // 2
    left_ptr, left_end, right_ptr, right_end = start, mid, mid + 1, end
    main_ptr = left_ptr
    while left_ptr <= left_end and right_ptr <= right_end:
        if arr[left_ptr] > arr[right_ptr]:
            buffer[main_ptr] = arr[right_ptr]
            right_ptr += 1
            answer += left_end - left_ptr + 1
        else:
            buffer[main_ptr] = arr[left_ptr]
            left_ptr += 1
        main_ptr += 1

    while left_ptr <= left_end:
        buffer[main_ptr] = arr[left_ptr]
        left_ptr += 1
        main_ptr += 1

    while right_ptr <= right_end:
        buffer[main_ptr] = arr[right_ptr]
        right_ptr += 1
        main_ptr += 1

    for i in range(start, end + 1):
        arr[i] = buffer[i]


def merge_sort(start, end):
    if start < end:
        mid = (start + end) // 2
        merge_sort(start, mid)
        merge_sort(mid + 1, end)
        merge(start, end)


if __name__ == '__main__':
    N = int(input())
    arr = list(map(int, input().split()))
    buffer = [0] * N
    answer = 0
    merge_sort(0, N - 1)
    print(answer)

"""
8
21 10 12 20 25 13 15 22
10 21 12 20 25 13 15 22
10 12 21 20 25 13 15 22
10 12 20 21 25 13 15 22
10 12 20 21 13 25 15 22
10 12 20 21 13 15 25 22
10 12 20 21 13 15 22 25
10 12 20 13 21 15 22 25
10 12 20 13 15 21 22 25
10 12 13 20 15 21 22 25
10 12 13 15 20 21 22 25
"""