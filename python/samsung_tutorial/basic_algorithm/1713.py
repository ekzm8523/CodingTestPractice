# https://www.acmicpc.net/problem/1713
"""
추천 -> 사진틀 게시
사진틀 자리 없을떄? -> 1. 추천수 가장 적은 순, 2. 게시된 날짜가 오래된 순
"""
import heapq

if __name__ == "__main__":
    n = int(input())
    size = int(input())
    recommendation = list(map(int, input().split()))
    dic = {}
    cnt = 0

    for i in range(size):
        if not recommendation[i] in dic:
            if cnt == n:
                delete_key = sorted(dic.items(), key=lambda x: (x[1][0], x[1][1]))[0][0]
                dic.pop(delete_key)
                cnt -= 1
            dic[recommendation[i]] = [1, i]
            cnt += 1

        else:
            dic[recommendation[i]][0] += 1

    for key in sorted(dic):
        print(key, end=" ")
