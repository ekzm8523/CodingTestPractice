# https://www.acmicpc.net/problem/1766
import sys
from heapq import heappop as pop, heappush as push

input = lambda: sys.stdin.readline().strip()

if __name__ == "__main__":
    problem_cnt, priority_cnt = map(int, input().split())

    priorities = {}
    injects = [0] * (problem_cnt + 1)

    for _ in range(priority_cnt):
        a, b = map(int, input().split())
        if a not in priorities:
            priorities[a] = []
        priorities[a].append(b)
        injects[b] += 1

    hq = []
    for i, cnt in enumerate(injects[1:]):
        if cnt == 0:
            push(hq, i + 1)

    answer = []
    while hq:
        node = pop(hq)
        answer.append(node)
        if node in priorities:
            for key in priorities[node]:
                injects[key] -= 1
                if injects[key] == 0:
                    push(hq, key)
    print(*answer)