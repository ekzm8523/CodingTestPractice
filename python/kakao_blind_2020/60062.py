# https://school.programmers.co.kr/learn/courses/30/lessons/60062?language=python3
"""
친구들을 순열로 나열한다.
가작 작은 명수의 친구들로 구성된 순열부터 하나씩 weak를 한 줄로 나열한 리스트에 넣어본다.
하나라도 성공하면 그게 정답
"""
from itertools import permutations
from collections import deque


def is_possible(friend_combination: tuple, serialized_weak: tuple) -> bool:
    ptr = serialized_weak[0]
    next_idx = 1
    for friend_workload in friend_combination:
        ptr += friend_workload
        while serialized_weak[next_idx] <= ptr:
            next_idx += 1
            if next_idx == len(serialized_weak):
                return True
        ptr = serialized_weak[next_idx]
    return False


def solution(n: int, weak: list, dist: list) -> int:

    for friend_count in range(1, len(dist) + 1):
        for friend_combination in permutations(dist, friend_count):
            serialized_weak = deque(weak)
            for _ in range(len(weak)):
                if is_possible(friend_combination, tuple(serialized_weak)):
                    return friend_count
                num = serialized_weak.popleft()
                serialized_weak.append(num + n)

    return -1


if __name__ == '__main__':
    n = 12
    weak = [1, 5, 6, 10]
    dist = [1, 2, 3, 4]
    print(solution(n, weak, dist))

    n = 12
    weak = [1, 3, 4, 9, 10]
    dist = [3, 5, 7]
    print(solution(n, weak, dist))
