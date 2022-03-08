# https://www.acmicpc.net/problem/2252
from collections import defaultdict, deque
import sys


if __name__ == "__main__":
    student_cnt, compare_cnt = map(int, sys.stdin.readline().split())

    table = [0] * (student_cnt + 1)
    graph = defaultdict(list)

    for _ in range(compare_cnt):
        a, b = map(int, sys.stdin.readline().split())
        table[b] += 1
        graph[a].append(b)

    q = deque()
    for i in range(1, student_cnt + 1):
        if table[i] == 0:
            q.append(i)
    answer = []
    while q:
        current_node = q.popleft()
        answer.append(current_node)

        for next_node in graph[current_node]:
            table[next_node] -= 1
            if table[next_node] == 0:
                q.append(next_node)
    print(*answer)