
from collections import deque
if __name__ == "__main__":
    N, K = map(int, input().split())

    def bfs(v):
        count = 0
        q = deque([(v, count)])
        while q:
            v, count = q.popleft()
            if not visited[v]:
                visited[v] = True
                if v == K:
                    return count
                count += 1
                if (v * 2) <= 100000:
                    q.append((v*2, count))
                if (v - 1) >= 0:
                    q.append((v-1, count))
                if (v + 1) <= 100000:
                    q.append((v+1, count))
    visited = [False] * 100001
    print(bfs(N))