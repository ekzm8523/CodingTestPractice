def is_sorted(arr):
    prev = arr[0]
    for i in range(1, len(arr)):
        if arr[i] < prev:
            return False
        prev = arr[i]
    return True



answer = int(1e9)
def solution(arr, k):

    def dfs(arr, idx, pivot, depth):
        global answer

        if depth > answer:
            return

        arr[idx], arr[pivot] = arr[pivot], arr[idx]
        idx = pivot

        if is_sorted(arr):
            answer = depth
            return

        for i in range(k):
            if idx + i >= len(arr):
                break
            if arr[idx] < arr[idx + i]:
                dfs(arr.copy(), idx, idx + i, depth+1)
    for i in range(len(arr)):
        dfs(arr, i, i, 0)
    return answer

if __name__ == "__main__":

    print(solution([4, 5, 2, 3, 1], 2))
    print(solution([5, 4, 3, 2, 1], 4))
    print(solution([5, 4, 3, 2, 1], 2))

