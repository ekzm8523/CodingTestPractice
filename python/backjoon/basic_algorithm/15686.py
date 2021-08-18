# https://www.acmicpc.net/problem/15686
"""
거리는 L1 노름 계산식
0: 빈칸
1: 집
2: 치킨
도시에 있는 치킨집 중에서 최대 M개를 고르고, 나머지 치킨집은 모두 폐업시켜야 한다.
어떻게 고르면, 도시의 치킨 거리가 가장 작게 될지 구하는 프로그램을 작성하시오.
"""

import sys
from itertools import combinations

def calculate_distance(pos1, pos2):
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])


if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().split())
    table = [list(sys.stdin.readline().split()) for _ in range(n)]

    house_pos = []
    chicken_pos = []

    for i in range(n):
        for j in range(n):
            if table[i][j] == '1':
                house_pos.append((i, j))
            elif table[i][j] == '2':
                chicken_pos.append((i, j))
    answer = sys.maxsize
    combs = tuple(combinations(chicken_pos, m))
    for chicken_comb in combs:
        city_chicken_distance = 0
        for house in house_pos:
            distance = sys.maxsize
            for chicken in chicken_comb:
                distance = min(distance, calculate_distance(chicken, house))
            city_chicken_distance += distance

        answer = min(answer, city_chicken_distance)

    print(answer)
