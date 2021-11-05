import random

def quicksort(arr, size):
    if size <= 1:
        return arr

    pivot = arr[size // 2]

    left, mid, right = [], [], []

    for num in arr:
        if num < pivot:
            left.append(num)
        elif num > pivot:
            right.append(num)
        else:
            mid.append(num)

    return quicksort(left, len(left)) + mid + quicksort(right, len(right))


def improve_quicksort(arr, size):
    def sort(left, right):
        if right <= left:
            return
        mid = partition(left, right)
        sort(left, mid-1)
        sort(mid, right)

    def partition(left, right):
        pivot = arr[(left + right) // 2]
        while left <= right:
            while arr[left] < pivot:
                left += 1
            while arr[right] > pivot:
                right -= 1
            if left <= right:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1
        return left
    return sort(0, size-1)

if __name__ == '__main__':
    l = list(range(10))
    random.shuffle(l)

    print(l)
    print(quicksort(l, 10))
    improve_quicksort(l, 10)
    print(l)



