# https://www.acmicpc.net/problem/1766
import sys
from collections import defaultdict
import heapq


if __name__ == '__main__':
    question_cnt, priority_cnt = map(int, sys.stdin.readline().split())

    priority = defaultdict(list)
    in_degree = [-1] + [0 for _ in range(question_cnt)]
    for _ in range(priority_cnt):
        x, y = map(int, sys.stdin.readline().split())
        priority[x].append(y)  # x가 없어지면 진입차수 빼야할 노드들
        in_degree[y] += 1  # 진입차수 + 1

    heap = []
    for i in range(1, question_cnt + 1):
        if in_degree[i] == 0:
            heap.append(i)
    answer = []
    while heap:
        current_node = heapq.heappop(heap)
        answer.append(current_node)
        for remove_item in priority[current_node]:
            in_degree[remove_item] -= 1
            if in_degree[remove_item] == 0:
                heapq.heappush(heap, remove_item)
    # if len(answer) == question_cnt:  # 문제에서 사이클은 없다고 했음
    print(*answer, end=" ")
