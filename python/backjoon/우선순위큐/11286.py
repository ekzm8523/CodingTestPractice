# https://www.acmicpc.net/problem/11286
import sys
import heapq

if __name__ == '__main__':
    query_cnt = int(sys.stdin.readline())
    heap = []
    for _ in range(query_cnt):
        q = int(sys.stdin.readline())
        if q == 0:
            print(heapq.heappop(heap)[1] if heap else 0)
        else:
            heapq.heappush(heap, (abs(q), q))
