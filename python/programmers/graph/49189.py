# https://programmers.co.kr/learn/courses/30/lessons/49189?language=python3

from collections import defaultdict, deque, Counter
import sys


def solution(n, edges):
    graph = defaultdict(list)
    visit = [False] * (n + 1)
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)

    table = [sys.maxsize] * (n + 1)
    q = deque()
    q.append(1)
    visit[1] = True
    table[1] = 0
    while q:
        current_node = q.popleft()

        for next_node in graph[current_node]:
            if not visit[next_node]:
                table[next_node] = min(table[next_node], table[current_node] + 1)
                visit[next_node] = True
                q.append(next_node)

    max_len = max(table[1:])

    return Counter(table)[max_len]


if __name__ == "__main__":
    n = 6
    vertex = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
    print(solution(n, vertex))