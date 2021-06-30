# https://www.acmicpc.net/problem/2467
import sys
if __name__ == "__main__":
    N = int(input())
    arr = list(map(int, input().split()))
    left_record = left = 0
    right_record = right = N-1
    min_record = sys.maxsize

    while left < right:
        special_value = arr[left] + arr[right]

        if abs(special_value) < min_record:
            min_record = abs(special_value)
            left_record = left
            right_record = right

        if special_value < 0:
            left += 1
        elif special_value > 0:
            right -= 1
        else:
            break

    print(arr[left_record], arr[right_record])