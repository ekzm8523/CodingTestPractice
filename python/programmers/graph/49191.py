# https://programmers.co.kr/learn/courses/30/lessons/49191?language=python3
from collections import defaultdict
from dataclasses import dataclass, field
from typing import Set


@dataclass
class Node:
    win: Set[int] = field(default_factory=set)
    lose: Set[int] = field(default_factory=set)


def solution(n, results):
    answer = 0
    graph = defaultdict(Node)

    for a, b in results:  # a가 b를 이김
        graph[a].win.add(b)
        graph[b].lose.add(a)


    for node in range(1, n + 1):
        q = list(graph[node].win)
        while q:
            current_node = q.pop()
            for next_node in graph[current_node].win:
                if next_node not in graph[node].win:
                    graph[node].win.add(next_node)
                    q.append(next_node)
                if next_node not in graph[current_node].win:
                    graph[current_node].win.add(next_node)

        q = list(graph[node].lose)
        while q:
            current_node = q.pop()
            for next_node in graph[current_node].lose:
                if next_node not in graph[node].lose:
                    graph[node].lose.add(next_node)
                    q.append(next_node)
                if next_node not in graph[current_node].lose:
                    graph[current_node].lose.add(next_node)
        if len(graph[node].win) + len(graph[node].lose) == n - 1:
            answer += 1

    return answer


if __name__ == "__main__":
    n = 5
    results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
    print(solution(n, results))