"""
어차피 앞에서부터 바꿔야함
앞에 한번 뒤에 한번
이렇게 하는게 최적일듯?
원소 두개의 합을 비교하고 같으면 다음꺼는 패스해도 됨 -> 이게 연산 줄이는 포인트
"""

def solution(arr, brr):
    answer = 0

    flag = True  # True -> 앞에서부터 , False -> 뒤에서부터
    left, right = 0, len(arr) - 1
    while left < right:
        if flag:
            if arr[left] == brr[left]:
                left += 1
                answer -= 1
            elif arr[left] + arr[left + 1] == brr[left] + brr[left + 1]:
                arr[left], arr[left + 1] = brr[left], brr[left + 1]
                left += 2

            else:
                dif = brr[left] - arr[left]
                arr[left] += dif
                arr[left + 1] -= dif
                left += 1

        else:
            if arr[right] == brr[right]:
                right -= 1
                answer -= 1
            elif arr[right] + arr[right - 1] == brr[right] + brr[right - 1]:
                arr[right], arr[right - 1] = brr[right], brr[right - 1]
                right -= 2
            else:
                dif = brr[right] - arr[right]
                arr[right] += dif
                arr[right - 1] -= dif
                right -= 1
        answer += 1
        flag = not flag

    return answer



if __name__ == '__main__':
    arr = [3, 7, 2, 4]
    brr = [4, 5, 5, 2]
    print(solution(arr, brr))
    arr = [6, 2, 2, 6]
    brr = [4, 4, 4, 4]
    print(solution(arr, brr))
