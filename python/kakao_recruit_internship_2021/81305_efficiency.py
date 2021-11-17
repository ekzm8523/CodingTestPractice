# https://programmers.co.kr/learn/courses/30/lessons/81305
import sys
from itertools import combinations
import copy
from collections import deque

def is_devide_group(criterion, k, num, links, search_order):
    size = len(num)

    # dp[v][0] -> v를 루트로 가지고 criterion 을 넘지 않는 최소 그룹 수
    # dp[v][1] -> 최소 그룹 수로 나눴을때 v를 포함한 서브 트리의 sum 값
    dp = [[sys.maxsize, 0] for _ in range(size)]

    max_depth = links[search_order[-1]][-1]

    while search_order:
        v = search_order.pop()
        if num[v] > criterion:
            return False
        l, r, depth = links[v]
        if l != -1 and r != -1:  # 왼쪽 오른쪽 자식 둘다 있을떄
            if dp[l][1] + dp[r][1] + num[v] <= criterion:
                dp[v][0] = dp[l][0] + dp[r][0] - 1
                dp[v][1] = dp[l][1] + dp[r][1] + num[v]
            elif dp[l][1] + num[v] <= criterion or dp[r][1] + num[v] <= criterion:
                dp[v][0] = dp[l][0] + dp[r][0]
                dp[v][1] = min(dp[l][1], dp[r][1]) + num[v]
            elif num[v] <= criterion:
                dp[v][0] = dp[l][0] + dp[r][0] + 1
                dp[v][1] = num[v]
            else:
                return False

        elif l != -1 and r == -1:  # 왼쪽 자식만 있을때
            if dp[l][1] + num[v] <= criterion:
                dp[v][0] = dp[l][0]
                dp[v][1] = dp[l][1] + num[v]
            else:
                dp[v][0] = dp[l][0] + 1
                dp[v][1] = num[v]
        elif l == -1 and r != -1:  # 오른쪽 자식만 있을떄
            if dp[r][1] + num[v] <= criterion:
                dp[v][0] = dp[r][0]
                dp[v][1] = dp[r][1] + num[v]
            else:
                dp[v][0] = dp[r][0] + 1
                dp[v][1] = num[v]
        else:
            dp[v][0] = 1
            dp[v][1] = num[v]
        if depth == 0:
            return dp[v][0] <= k

def find_root(links):
    candidate = set(range(len(links)))

    for link in links:
        if link[0] != -1:
            candidate.remove(link[0])
        if link[1] != -1:
            candidate.remove(link[1])

    return candidate.pop()


def preprocess_links(links, root):
    q = deque((root, ))
    links[root].append(0)
    search_order = []

    while q:
        node = q.popleft()

        l, r, depth = links[node]
        search_order.append(node)
        if l != -1:
            links[l].append(depth + 1)
            q.append(l)
        if r != -1:
            links[r].append(depth + 1)
            q.append(r)

    return search_order

def solution(k, num, links):
    _sum = sum(num)
    answer = sys.maxsize
    if k == 1:
        return _sum
    l, r = _sum // 4, _sum
    root = find_root(links)
    search_order = preprocess_links(links, root)

    while l <= r:
        mid = (l + r) // 2
        if is_devide_group(mid, k, num, links, copy.copy(search_order)):
            r = mid - 1
            answer = mid
        else:
            l = mid + 1

    return answer

if __name__ == '__main__':
    # k = 3
    # num = [12, 30, 1, 8, 8, 6, 20, 7, 5, 10, 4, 1]
    # links = [[-1, -1], [-1, -1], [-1, -1], [-1, -1], [8, 5], [2, 10], [3, 0], [6, 1], [11, -1], [7, 4], [-1, -1], [-1, -1]]
    # print(solution(k, num, links))
    #
    # k = 1
    # num = [6, 9, 7, 5]
    # links = [[-1, -1], [-1, -1], [-1, 0], [2, 1]]
    # print(solution(k, num, links))
    #
    # k = 2
    # num = [6, 9, 7, 5]
    # links = [[-1, -1], [-1, -1], [-1, 0], [2, 1]]
    # print(solution(k, num, links))

    k = 4
    num = [6, 9, 7, 5]
    links = [[-1, -1], [-1, -1], [-1, 0], [2, 1]]
    print(solution(k, num, links))