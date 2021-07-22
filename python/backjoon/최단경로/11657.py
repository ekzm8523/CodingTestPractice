# https://www.acmicpc.net/problem/11657

"""
A에서 B로 가는 시간 T에는 음수도 있다.
이미 방문한 노드에 다시 방문했을때 거리가 줄어든다면 무한 타임루프에 걸린 것 이므로 -1 출력
1번 노드에서 2....N까지의 최단 거리를 출력 (다익스트라)
만약 가는 경로가 없다면 -1을 출력 (위와 다름)

Wrong!!

음수의 간선이 있는 최단 경로 알고리즘은 벨만 포드 알고리즘!!


"""

import sys
import heapq
INF = int(1e9)


# if __name__ == "__main__":
#     N, M = map(int, sys.stdin.readline().split())
#     graph = [[] for _ in range(N + 1)]
#     table = [INF] * (N + 1)
#     table[0] = graph[0] = None
#     for _ in range(M):
#         A, B, T = map(int, sys.stdin.readline().split())
#         graph[A].append((B, T))
#
#
#     table[1] = 0
#     hq = []
#     visit = set()
#     for node, time in graph[1]:
#         table[node] = time
#         heapq.heappush(hq, (time, node))
#         visit.add(1)
#
#
#     while hq:
#         current_time, current_node = heapq.heappop(hq)
#         visit.add(current_node)
#
#         for node, time in graph[current_node]:
#             if table[node] > (current_time + time):
#                 if node in visit:
#                     print(1)
#                     exit()
#                 table[node] = current_node + time
#             if node not in visit:
#                 heapq.heappush(hq, (table[node], node))
#
#     for i in range(2, N + 1):
#         print(-1) if table[i] == INF else print(table[i])


import sys

if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(N + 1)]
    INF = sys.maxsize
    times = [INF] * (N + 1)

    for _ in range(M):
        a, b, time = map(int, sys.stdin.readline().split())
        graph[a].append((b, time))

    # initialization
    graph[0] = times[0] = None
    times[1] = 0
    is_possible = True
    # start bellman ford
    for cnt in range(1, N + 1):     # N-1번만큼 반복 후 마지막번째에 또 업데이트가 이루어 지면 무한 타임머신
        for i in range(1, N + 1):
            for node, time in graph[i]:
                if times[i] != INF and times[i] + time < times[node]:   # time[i] != INF가 없으면 52퍼에서 틀린다 왜그러지?
                    times[node] = times[i] + time
                    if cnt == N:
                        is_possible = False

    if is_possible:
        for i in range(2, N + 1):
            print(times[i]) if times[i] != INF else print(-1)
    else:
        print(-1)
    # for i in range(N + 1):
    #     print(f"{i} : {graph[i]} time : {times[i]}")


