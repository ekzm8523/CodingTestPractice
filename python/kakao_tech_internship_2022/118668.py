# https://school.programmers.co.kr/learn/courses/30/lessons/118668
"""
나름 그리디 아닐까?
기본 패시브 알고력 + 1, 코딩력 + 1,
dp[0][0011]
next -> 2
min(dp[0][0011], dp[2][0111] + graph[0][2])
min(dp[cur][visited], dp[next][visited | 1 << next] + graph[cur][next])
우리도 dp를 이용하는게 좋을듯
dp[alp][cop] -> alp, cop 까지 도달하는 최소 시간
10, 10 -> 0
10, 15 -> 5
20, 20 ->
"""
from collections import deque


def update(q: deque, dp: list, next_alp: int, next_cop: int, cur_alp: int, cur_cop: int, cost: int) -> None:
    if dp[next_alp][next_cop] > dp[cur_alp][cur_cop] + cost:
        dp[next_alp][next_cop] = dp[cur_alp][cur_cop] + cost
        q.append((next_alp, next_cop, dp[next_alp][next_cop]))


def solution(alp, cop, problems):
    max_alp, max_cop = 0, 0
    for problem in problems:
        max_alp, max_cop = max(max_alp, problem[0]), max(max_cop, problem[1])

    dp = [[300] * (max_cop + 30) for _ in range(max_alp + 30)]
    dp[alp][cop] = 0
    q = deque()
    q.append((alp, cop, 0))
    while q:
        i, j, cur_cost = q.popleft()
        if cur_cost > dp[i][j] or (i >= max_alp and j >= max_cop):
            continue
        if i < max_alp:
            update(q=q, dp=dp, next_alp=i + 1, next_cop=j, cur_alp=i, cur_cop=j, cost=1)
        if j < max_cop:
            update(q=q, dp=dp, next_alp=i, next_cop=j + 1, cur_alp=i, cur_cop=j, cost=1)

        for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
            if i >= alp_req and j >= cop_req:
                next_alp, next_cop = i + alp_rwd, j + cop_rwd
                next_alp = min(next_alp, max_alp)
                next_cop = min(next_cop, max_cop)
                update(q=q, dp=dp, next_alp=next_alp, next_cop=next_cop, cur_alp=i, cur_cop=j, cost=cost)

    return dp[max_alp][max_cop]


if __name__ == '__main__':
    alp, cop = 10, 10
    problems = [[10, 15, 2, 1, 2], [20, 20, 3, 3, 4]]
    print(solution(alp, cop, problems))

    alp, cop = 0, 0
    problems = [[0, 0, 2, 1, 2], [4, 5, 3, 1, 2], [4, 11, 4, 0, 2], [10, 4, 0, 4, 2]]
    print(solution(alp, cop, problems))
