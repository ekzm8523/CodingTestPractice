# https://www.acmicpc.net/problem/1005


from collections import deque
import sys
if __name__ == "__main__":

    T = int(input())
    INF = sys.maxsize

    for _ in range(T):
        N, K = map(int, sys.stdin.readline().split())    # N: 건물의 갯수, K: 건설순서규칙의 총 개수
        build_times = [0] + list(map(int, sys.stdin.readline().split()))
        build_seq = [[] for _ in range(N+1)]
        in_degree = [0] * (N + 1)
        in_degree[0] = build_seq[0] = None
        dp = [0] * (N + 1)

        for i in range(K):
            a, b = map(int, sys.stdin.readline().split())
            build_seq[a].append(b)
            in_degree[b] += 1

        end = int(sys.stdin.readline())

        q = deque()

        for i in range(1, N+1):
            if in_degree[i] == 0:
                q.append(i)
                dp[i] = build_times[i]

        while q:
            current_node = q.popleft()

            for node in build_seq[current_node]:
                in_degree[node] -= 1
                if in_degree[node] == 0:
                    q.append(node)
                dp[node] = max(dp[current_node] + build_times[node], dp[node])

        print(dp[end])

