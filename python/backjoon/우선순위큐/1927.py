# https://www.acmicpc.net/problem/1927
import heapq, sys

if __name__ == "__main__":
    N = int(input())
    heap = []

    for i in range(N):
        a = int(sys.stdin.readline())
        if a == 0:
            if heap:
                print(heapq.heappop(heap))
            else:
                print(0)
        else:
            heapq.heappush(heap, a)