

def is_sorted(arr):
    prev = arr[0]
    for i in range(1, len(arr)):
        if arr[i] < prev:
            return False
        prev = arr[i]
    return True


def solution(arr, k):
    answer = 0
    idx = len(arr) - 1

    while not is_sorted(arr):
        m = 0
        ptr = -1
        for i in range(idx+1):
            if m < arr[i]:
                m = arr[i]
                ptr = i

        while ptr < idx:
            if idx < ptr + k:
                arr[ptr], arr[idx] = arr[idx], arr[ptr]

            else:
                arr[ptr], arr[ptr + k] = arr[ptr + k], arr[ptr]

            ptr += k
            answer += 1

        idx -= 1

    return answer

if __name__ == "__main__":
    print(solution([4, 5, 2, 3, 1], 2))
    print(solution([5, 4, 3, 2, 1], 4))
    print(solution([5, 4, 3, 2, 1], 2))

