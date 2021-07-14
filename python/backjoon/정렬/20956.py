# https://www.acmicpc.net/problem/20956
"""
N개의 아이스크림중 가장 양이 많은 아이스크림을 선택
가장 많은 양의 아이스크림이 여러개라면 가장 왼쪽
아이스크림의 양이 7의 배수라면 민트초코맛이다
민초를 먹으면 남은 아이스크림의 순서를 좌우로 뒤집는다.
K = 7
i = 3
K - i + 1 = 5

"""
from collections import deque

if __name__ == "__main__":
    n, m = map(int, input().split())

    amounts = list(map(int, input().split()))

    dq_dic = {}

    for i in range(n):
        if amounts[i] not in dq_dic:
            dq_dic[amounts[i]] = deque([i+1])
        else:
            dq_dic[amounts[i]].append(i+1)

    sorted_dq = sorted(dq_dic.items(), key=lambda x: x[0], reverse=True)
    reverse = False
    cnt = 0

    for value, dq in sorted_dq:
        while dq:
            if not reverse:
                idx = dq.popleft()
            else:
                idx = dq.pop()
            print(idx)
            cnt += 1
            if value % 7 == 0:
                reverse = not reverse
            if cnt == m:
                break
        if cnt == m:
            break