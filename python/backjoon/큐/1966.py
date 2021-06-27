# https://www.acmicpc.net/problem/1966

from collections import deque

if __name__ == "__main__":
    test_N = int(input())


    for i in range(test_N):
        N, M = list(map(int, input().split()))
        queue = deque(map(int, input().split()))

        cnt = 0
        size = len(queue)
        while queue:
            max_rate = max(queue)

            while max_rate > queue[0]:
                queue.rotate(-1)
                M = (M - 1 + size) % size
            queue.popleft()
            cnt += 1
            size -= 1

            if M == 0:
                print(cnt)
                break
            M -= 1
