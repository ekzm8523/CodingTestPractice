# https://www.acmicpc.net/problem/1039
from itertools import combinations
from collections import deque
import copy

if __name__ == "__main__":
    n, k = input().split()
    k = int(k)
    m = len(n)

    combs = list(combinations(list(range(m)), 2))
    cand = set()
    dq = deque()
    dq.append(n)  # string, 변경 횟수
    def bfs(depth):
        next_cond = set()
        cycle = len(dq)
        for _ in range(cycle):
            x = dq.popleft()
            for a, b in combs:
                tmp = list(str(x))  # deepcopy 가 시간이 좀 걸림
                tmp[a], tmp[b] = tmp[b], tmp[a]
                if tmp[0] == '0':
                    continue
                tmp = int(''.join(tmp))
                if depth == k - 1:
                    cand.add(tmp)
                if tmp not in next_cond:
                    dq.append(tmp)
                    next_cond.add(tmp)

    for i in range(k):
        bfs(i)

    if cand:
        print(max(cand))
    else:
        print(-1)