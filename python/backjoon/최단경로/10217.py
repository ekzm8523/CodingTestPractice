# https://www.acmicpc.net/problem/10217
import sys

if __name__ == "__main__":

    t = int(sys.stdin.readline())
    INF = sys.maxsize
    for _ in range(t):
        n, m, k = map(int, sys.stdin.readline().split())    # 공항의 수 N, 총 지원비용 M, 티켓정보의 수 K
        airport = [[] for _ in range(n + 1)]
        for _ in range(k):
            u, v, c, d = map(int, sys.stdin.readline().split()) # 출발공항, 도착공항, 비용, 소요시간
            airport[u].append((v, c, d))
        # 인천은 언제나 1번 도시, LA는 언제나 N번 도시
        # 찬민이 LA에 도착하는 가장 짧은 소요 시간 출력
        # node * money 만큼의 table을 생성
        table = [[INF for _ in range(m + 1)] for _ in range(n + 1)]     # cost, time
        table[1][0] = 0

        # 원래 다익스트라처럼 방문하지 않은 노드중에 가장 짧은 거리를 탐색하는게 아닌 cost 순으로 table 을 돌면서 방문
        for cost in range(m + 1):
            for node in range(n + 1):
                if table[node][cost] == INF:
                    continue

                for v, c, d in airport[node]:
                    if cost + c > m:
                        continue
                    if table[v][cost + c] > table[node][cost] + d:
                        table[v][cost + c] = table[node][cost] + d

        answer = min(table[n])
        print("Poor KCM" if answer == INF else answer)
