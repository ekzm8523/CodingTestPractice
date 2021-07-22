# https://www.acmicpc.net/problem/9370
import sys
import heapq

def dijkstra(start):
    distance_table = [INF] * (n + 1)
    distance_table[start] = 0
    visit = set()
    visit.add(start)
    hq = [(0, start)]

    while hq:
        current_dis, current_node = heapq.heappop(hq)
        if current_dis > distance_table[current_node]:
            continue
        visit.add(current_node)

        for next_node, dis in graph[current_node]:
            if next_node in visit:
                continue
            if current_dis + dis < distance_table[next_node]:
                distance_table[next_node] = current_dis + dis
                heapq.heappush(hq, (distance_table[next_node], next_node))

    return distance_table


if __name__ == "__main__":

    test = int(sys.stdin.readline())
    INF = sys.maxsize
    for time in range(test):
        n, m, t = map(int, sys.stdin.readline().split())    # n: node갯수, m: edge갯수, t: 목적지 node 갯수
        s, g, h = map(int, sys.stdin.readline().split())    # s: 출발지, g, h: g와 h사이의 다리를 지남
        graph = [[] for _ in range(n + 1)]
        for _ in range(m):
            a, b, c = map(int, sys.stdin.readline().split())
            graph[a].append((b, c))
            graph[b].append((a, c))


        candidates = []
        for _ in range(t):
            candidates.append(int(sys.stdin.readline()))

        gh_dis = 0
        for node, dis in graph[g]:
            if node == h:
                gh_dis = dis

        s_distance_table = dijkstra(s)
        g_distance_table = dijkstra(g)
        h_distance_table = dijkstra(h)

        answer = []
        for candidate in candidates:
            if s_distance_table[candidate] == min(s_distance_table[g] + gh_dis + h_distance_table[candidate],
                                                  s_distance_table[h] + gh_dis + g_distance_table[candidate]):
                answer.append(candidate)
        answer.sort()
        for value in answer:
            print(value, end=" ")
        print()