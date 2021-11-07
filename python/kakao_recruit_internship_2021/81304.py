# https://programmers.co.kr/learn/courses/30/lessons/81304
import sys
import heapq


# def dijkstra(graph, start, end, n):
#     table = [None] + [sys.maxsize for _ in range(n)]
#     visit = set()
#     pq = []
#     heapq.heappush(pq, (0, start))
#     table[start] = 0
#     while pq:
#         dist, node = heapq.heappop(pq)
#         if node in visit:
#             continue
#         visit.add(node)
#
#         for next_dist, next_node in graph[node]:
#             if table[next_node] > (next_dist + dist):
#                 table[next_node] = next_dist + dist
#                 heapq.heappush(pq, (table[next_node], next_node))
#
#     return table

def get_current_direction(cur_pos, next_pos, cur_state, traps_idx):
    is_cur_trap_on, is_next_trap_on = False, False
    if cur_pos in traps_idx:
        is_cur_trap_on = (cur_state & (1 << traps_idx[cur_pos])) > 0
    if next_pos in traps_idx:
        is_next_trap_on = (cur_state & (1 << traps_idx[next_pos])) > 0
    return is_cur_trap_on != is_next_trap_on    # False 면 역방향, True 면 순방향



def get_next_state(next_pos, cur_state, traps_idx):
    if next_pos in traps_idx:
        return cur_state ^ (1 << traps_idx[next_pos])
    return cur_state

INF = sys.maxsize
def solution(n, start, end, roads, traps):

    answer = INF
    min_cost = [[INF for _ in range(n+1)] for _ in range(2 ** len(traps))]
    traps_idx = {v: i for i, v in enumerate(traps)}
    graph = [[] for _ in range(n+1)]

    for _start, _end, _cost in roads:
        graph[_start].append([_end, _cost, False])
        graph[_end].append([_start, _cost, True])

    hq = []
    heapq.heappush(hq, [0, start, 0])   # sum, cur_pos, trap_state
    min_cost[0][start] = 0

    while hq:
        cur_sum, cur_pos, cur_state = heapq.heappop(hq)
        if cur_pos == end:
            answer = min(answer, cur_sum)
            continue
        if cur_sum > min_cost[cur_state][cur_pos]:  # 중복방문 처리
            continue
        for next_pos, next_cost, direction in graph[cur_pos]:
            if direction != get_current_direction(cur_pos, next_pos, cur_state, traps_idx):
                continue    #

            next_state = get_next_state(next_pos, cur_state, traps_idx)
            next_sum = next_cost + cur_sum

            if next_sum >= min_cost[next_state][next_pos]:
                continue

            min_cost[next_state][next_pos] = next_sum
            heapq.heappush(hq, [next_sum, next_pos, next_state])
    return answer

if __name__ == '__main__':
    n, start, end = 3, 1, 3
    roads = [[1, 2, 2], [3, 2, 3]]
    traps = [2]
    print(solution(n, start, end, roads, traps))

    n, start, end = 4, 1, 4
    roads = [[1, 2, 1], [3, 2, 1], [2, 4, 1]]
    traps = [2, 3]
    print(solution(n, start, end, roads, traps))
