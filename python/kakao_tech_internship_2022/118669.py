# https://school.programmers.co.kr/learn/courses/30/lessons/118669
import math
from heapq import heappop as pop, heappush as push

INF = int(1e7) + 1

def solution(n, paths, gates, summits) -> list:
    answer = [0, math.inf]

    graph = [[] for _ in range(n + 1)]
    for a, b, dis in paths:
        graph[a].append((b, dis))
        graph[b].append((a, dis))
    summit_set = set(summits)
    gate_set = set(gates)

    def dijkstra(gate: int, summit: int, graph: list) -> int:
        dp = [INF] * len(graph)
        visit = [False] * len(graph)
        dp[gate], visit[gate] = 0, True
        hq = [(0, gate)]  # weight, gate number

        while hq:
            current_intensity, visit_number = pop(hq)

            if current_intensity > dp[visit_number]:
                continue

            for next_number, distance in graph[visit_number]:
                if (next_number in gate_set and next_number != gate) or\
                        (next_number in summit_set and next_number != summit):
                    continue
                new_intensity = max(current_intensity, distance)
                if new_intensity < dp[next_number]:
                    dp[next_number] = new_intensity
                    push(hq, (new_intensity, next_number))
        return dp[summit]

    for gate in gates:
        for summit in summits:
            intensity = dijkstra(gate, summit, graph)
            if answer[1] >= intensity:
                if answer[1] == intensity and answer[0] < summit:
                    continue
                answer[0], answer[1] = summit, intensity

    return answer


if __name__ == '__main__':
    n = 6
    paths = [[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]]
    gates = [1, 3]
    summits = [5]
    print(solution(n, paths, gates, summits))

    n = 7
    paths = [[1, 4, 4], [1, 6, 1], [1, 7, 3], [2, 5, 2], [3, 7, 4], [5, 6, 6]]
    gates = [1]
    summits = [2, 3, 4]
    print(solution(n, paths, gates, summits))

    n = 7
    paths = [[1, 2, 5], [1, 4, 1], [2, 3, 1], [2, 6, 7], [4, 5, 1], [5, 6, 1], [6, 7, 1]]
    gates = [3, 7]
    summits = [1, 5]
    print(solution(n, paths, gates, summits))

    n = 5
    paths = [[1, 3, 10], [1, 4, 20], [2, 3, 4], [2, 4, 6], [3, 5, 20], [4, 5, 6]]
    gates = [1, 2]
    summits = [5]
    print(solution(n, paths, gates, summits))
