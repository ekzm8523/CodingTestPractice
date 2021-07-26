# https://www.acmicpc.net/problem/8983

"""
범위를 봤을때 이분탐색이 필요하다.
동물의 위치를 하나씩 정하고
사대의 index를 left right mid로 정하면서 돌기
"""
import sys

def calc_distance(shot, pos):
    return abs(shot - pos[0]) + pos[1]

def solution(shot_pos, animal_pos):
    global m, n, l
    # print(shot_pos)
    # print(animal_pos)
    # print(f"사대 : {m}개, 동물 : {n}마리, 사정거리 : {l}")
    answer = 0

    for x, y in animal_pos:

        left = 0
        right = m
        # print(f"x : {x} , y : {y}")
        while left <= right:
            mid = (left + right) // 2
            dis = calc_distance(shot_pos[mid], (x, y))
            # print(f"left : {left}, right : {right}, mid : {mid} , shot_pos : {shot_pos[mid]}, distance : {dis}")
            if dis <= l:
                answer += 1
                # print("통과 ! ")
                break
            if shot_pos[mid] == x:
                break
            elif shot_pos[mid] < x:
                left = mid + 1
            else:
                right = mid - 1
        # print()
    print(answer)


from bisect import bisect

if __name__ == "__main__":
    m, n, l = map(int, sys.stdin.readline().split())    # 사대의 수 m , 동물의 수 n, 사정거리 l

    shot_pos = sorted(list(map(int, sys.stdin.readline().split())))

    animal_pos = []

    for _ in range(n):
        x, y = map(int, sys.stdin.readline().split())
        animal_pos.append((x, y))

    solution(shot_pos, animal_pos)

    bisects = []
    for pos in animal_pos:
        bisects.append(bisect(shot_pos, pos[0]))

    cnt = 0

    for i in range(n):
        if (bisects[i] < m and shot_pos[bisects[i]] - animal_pos[i][0] + animal_pos[i][1] <= l) or \
                (0 < bisects[i] and animal_pos[i][0] - shot_pos[bisects[i] - 1] + animal_pos[i][1] <= l ):
            cnt += 1
    print(cnt)