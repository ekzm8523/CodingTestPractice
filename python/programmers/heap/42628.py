# https://programmers.co.kr/learn/courses/30/lessons/42628

from heapq import heappop as pop, heappush as push


def solution(operations):
    remove_set = set()
    idx = 0
    min_hq = []
    max_hq = []

    for operation in operations:
        op, num = operation.split()
        num = int(num)
        if op == "I":
            push(min_hq, (num, idx))
            push(max_hq, (-num, idx))
            idx += 1
        elif num == 1:
            while max_hq and max_hq[0][1] in remove_set:
                pop(max_hq)
            if not max_hq:
                continue
            _, remove_idx = pop(max_hq)
            remove_set.add(remove_idx)
        elif num == -1:
            while min_hq and min_hq[0][1] in remove_set:
                pop(min_hq)
            if not min_hq:
                continue
            _, remove_idx = pop(min_hq)
            remove_set.add(remove_idx)

    answer = [0, 0]

    while min_hq and min_hq[0][1] in remove_set:
        pop(min_hq)
    if min_hq:
        answer[1] = min_hq[0][0]

    while max_hq and max_hq[0][1] in remove_set:
        pop(max_hq)
    if max_hq:
        answer[0] = -max_hq[0][0]

    return answer


if __name__ == "__main__":

    operations = ["I 16","D 1"]
    print(solution(operations))
    operations = ["I 7","I 5","I -5","D -1"]
    print(solution(operations))
    operations = ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]
    print(solution(operations))
    operations = ["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]
    print(solution(operations))

