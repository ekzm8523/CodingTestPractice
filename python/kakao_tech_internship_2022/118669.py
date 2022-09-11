# https://school.programmers.co.kr/learn/courses/30/lessons/118669
from heapq import heappop as pop, heappush as push

INF = int(1e7) + 1


def solution(n, paths, gates, summits) -> list:
    graph = [[] for _ in range(n + 1)]
    for a, b, dis in paths:
        graph[a].append((b, dis))
        graph[b].append((a, dis))
    summit_set = set(summits)

    dp = [INF] * len(graph)
    hq = []  # weight, gate number
    for gate in gates:
        hq.append((0, gate))
        dp[gate] = 0

    while hq:
        current_intensity, visit_number = pop(hq)

        if current_intensity > dp[visit_number] or visit_number in summit_set:  # 산봉우리나 이미 더 낮은 intensity가 존재할 때
            continue

        for next_number, distance in graph[visit_number]:
            new_intensity = max(current_intensity, distance)
            if new_intensity < dp[next_number]:
                dp[next_number] = new_intensity
                push(hq, (new_intensity, next_number))
    answer = [0, INF]
    summits.sort()
    for summit in summits:
        if answer[1] > dp[summit]:
            answer[0], answer[1] = summit, dp[summit]

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
