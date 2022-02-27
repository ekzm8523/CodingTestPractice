# https://programmers.co.kr/learn/courses/30/lessons/43162




def solution(n, computers):
    answer = 0
    visit = [False] * n

    def dfs(current_node: int):
        nonlocal visit

        visit[current_node] = True
        for next_node, is_connect in enumerate(computers[current_node]):
            if is_connect and not visit[next_node]:
                dfs(next_node)

    for i in range(n):
        if not visit[i]:
            dfs(i)
            answer += 1

    return answer



if __name__ == '__main__':
    n = 3
    computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
    print(solution(n, computers))

    n = 3
    computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
    print(solution(n, computers))