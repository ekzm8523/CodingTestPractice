# https://www.acmicpc.net/problem/2213

"""
최대 독립 집합을 구하는 문제
트리에서 독립집합은 서로 인접하지 않으면 독립집합임
즉 노드를 선택하면 그 인접한 노드는 선택하지 못함
선택한 노드의 인접 집합의 가중치 합이 가장 작은 노드를 선택
dp[1][0] -> 1번째 노드를 포함 할 때 -> sum(dp[i][1] for i in 1의 자식노드)
dp[1][1] -> 1번째 노드를 포함하지 않을 때 -> max(sum(dp[i][0] for i in 1의 자식노드), sum(dp[i][1] for i in 1의 자식노드))
dfs 사용하여 후위수식
"""

import sys

def dfs(visit_node):
    visit[visit_node] = True
    dp[visit_node][0] = weights[visit_node]
    dp[visit_node][1] = 0
    trace_list[visit_node][0].append(visit_node)
    for child in childrens[visit_node]:
        if not visit[child]:
            dfs(child)
            dp[visit_node][0] += dp[child][1]
            trace_list[visit_node][0] += trace_list[child][1]
            if dp[child][0] >= dp[child][1]:
                dp[visit_node][1] += dp[child][0]
                trace_list[visit_node][1] += trace_list[child][0]
            else:
                dp[visit_node][1] += dp[child][1]
                trace_list[visit_node][1] += trace_list[child][1]


if __name__ == "__main__":

    n = int(sys.stdin.readline())

    weights = [None] + list(map(int, sys.stdin.readline().split()))
    childrens = [None] + [[] for _ in range(n)]

    for _ in range(n - 1):
        a, b = map(int, sys.stdin.readline().split())
        if a < b:
            childrens[a].append(b)
        else:
            childrens[b].append(a)

    dp = [None] + [[0] * 2 for _ in range(n)]
    visit = [None] + [False] * n
    trace_list = [None] + [[[], []]for _ in range(n)]
    dfs(1)

    if dp[1][0] >= dp[1][1]:
        print(dp[1][0])
        trace_list[1][0].sort()
        for node in trace_list[1][0]:
            print(node, end=" ")
    else:
        print(dp[1][1])
        trace_list[1][1].sort()
        for node in trace_list[1][1]:
            print(node, end=" ")
