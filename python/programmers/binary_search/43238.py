# https://programmers.co.kr/learn/courses/30/lessons/43238?language=python3
import sys


def solution(n, times):
    answer = sys.maxsize

    left, right = 0, int(sum(times) / len(times) / len(times) * n) * 2  # 적절한 값에서 시작 성능 2배이상 차이날 수 있음

    while left <= right:
        mid = (left + right) // 2
        passed_person = 0
        for time in times:
            passed_person += mid // time
        if passed_person >= n:
            right = mid - 1
            answer = mid
        else:
            left = mid + 1

    return answer


if __name__ == "__main__":
    n = 6
    times = [7, 10]
    print(solution(n, times))