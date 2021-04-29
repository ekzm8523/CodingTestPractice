# https://programmers.co.kr/learn/courses/30/lessons/43162

from collections import defaultdict

def dfs(comuters, check, index):
    check[index] = True

    for i in range(len(check)):
        if computers[index][i] and not check[i]:
            dfs(comuters, check, i)



def solution(computers, n):
    answer = 0
    check = [False] * n

    for i in range(n):
        if not check[i]:
            dfs(computers, check, i)
            answer+=1

    return answer


if __name__ == "__main__":
    # computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
    computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
    n = 3
    print(solution(computers, n))