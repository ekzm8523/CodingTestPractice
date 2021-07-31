"""
최소의 얼리 어답터를 구해야함 -> 얼리어답터가 아닌사람의 최댓값
dp[i][0] -> i번 노드가 얼리어답터가 아닐 때 -> 연결된 모든 노드는 얼리어답터여야함
dp[i][1] -> i번 노드가 얼리어답터일 때 -> 연결된 모든 노드의 얼리어답터이거나 얼리어답터가 아닌 값들의 최댓값
"""

import sys

def dfs(current_node):
    visit[current_node] = True
    dp[current_node][0] = 1
    for node in graph[current_node]:
        if not visit[node]:
            dfs(node)
            dp[current_node][0] += dp[node][1]  # not early adopter
            dp[current_node][1] += max(dp[node][0], dp[node][1])    # early adopter



if __name__ == "__main__":
    sys.setrecursionlimit(int(1e6))
    n = int(sys.stdin.readline())
    graph = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)
    dp = [[0, 0] for _ in range(n + 1)]
    visit = [False] * (n + 1)
    dfs(1)

    print(n - max(dp[1]))