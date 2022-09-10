# https://school.programmers.co.kr/learn/courses/30/lessons/118667

def solution(queue1, queue2):
    array = queue1 + queue2
    array_sum = sum(array)
    target_sum = array_sum // 2

    if array_sum % 2 == 1 or any((num > target_sum for num in array)):
        return -1
    array += array
    start_left, start_right = 0, len(queue1) - 1
    left, right = start_left, start_right

    current_sum = sum(queue1[left:right + 1])
    answer = 0
    while left <= right < len(array):
        if current_sum < target_sum:
            right += 1
            answer += 1
            if right < len(array):
                current_sum += array[right]
        elif current_sum > target_sum:
            current_sum -= array[left]
            left += 1
            answer += 1
        else:
            return answer

    return -1


if __name__ == '__main__':
    queue1 = [3, 2, 7, 2]
    queue2 = [4, 6, 5, 1]
    print(solution(queue1, queue2))

    queue1 = [1, 2, 1, 2]
    queue2 = [1, 10, 1, 2]
    print(solution(queue1, queue2))

    queue1 = [1, 1]
    queue2 = [1, 5]
    print(solution(queue1, queue2))

    queue1 = [3, 1]
    queue2 = [3, 3]
    print(solution(queue1, queue2))

    # [3, 2, 7, 2, 4, 6, 5, 1]