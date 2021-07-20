# https://www.acmicpc.net/problem/16434

import sys
import math

def join_dungeon(h_max, map_list, h_atk):
    global n
    h_cur = h_max

    for i in range(n):
        t, a, h = map_list[i]
        if t == 1:
            if h_atk >= h:  # 한방에 끝날 때
                continue
            h_atk_cnt = math.ceil(h / h_atk)    # 이만큼 때려야 몬스터가 주금
            atk_cnt = math.ceil(h_cur / a)  # 이만큼 때려야 용사가 주금
            if h_atk_cnt > atk_cnt:     # 용사가 더 빨리 죽으면
                return False
            h_cur -= (h_atk_cnt - 1) * a    # 이게 실행되려면 용사가 h_atk_cnt만큼 때려서 몬스터를 죽인 경우니까 몬스터가 때린건 h_atk_cnt - 1

        elif t == 2:
            h_atk += a
            h_cur = min(h_max, h_cur + h)
    return True

if __name__ == "__main__":
    n, h_atk = map(int, sys.stdin.readline().split())
    INF = int(1e18)
    map_list = []
    for _ in range(n):
        # t == 1 -> 공격력이 a이고 생명력이 h인 몬스터가 있음
        # t == 2 -> 용사의 공격력 h_atk를 a만큼 증가시켜주고 현재 생명력 h_cur를 h만큼 회복
        t, a, h = map(int, sys.stdin.readline().split())
        map_list.append((t, a, h))

    left = 1
    right = INF
    answer = INF

    while left <= right:
        mid = (left + right) // 2

        if join_dungeon(mid, map_list, h_atk):  # True point
            right = mid - 1
            answer = mid
        else:
            left = mid + 1
    print(answer)






