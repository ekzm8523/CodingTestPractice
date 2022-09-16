# https://school.programmers.co.kr/learn/courses/30/lessons/118670


def solution(rc, operations):
    answer = [[]]
    return answer


if __name__ == '__main__':
    rc = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    operations = ["Rotate", "ShiftRow"]
    print(solution(rc, operations))

    rc = [[8, 6, 3], [3, 3, 7], [8, 4, 9]]
    operations = ["Rotate", "ShiftRow", "ShiftRow"]
    print(solution(rc, operations))

    rc = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    operations = ["ShiftRow", "Rotate", "ShiftRow", "Rotate"]
    print(solution(rc, operations))
