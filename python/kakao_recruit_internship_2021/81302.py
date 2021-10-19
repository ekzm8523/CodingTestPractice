"""
https://programmers.co.kr/learn/courses/30/lessons/81302
using bfs
P : 응시자
O : 빈 테이블
X : 파티션 (가림막)
"""
from collections import deque


def keep_distance_check(pos, place):
    move = ((-1, 0), (0, 1), (1, 0), (0, -1))
    q = deque(((pos[0], pos[1], 0),))

    visit = set()
    while q:
        row, col, dis = q.popleft()
        visit.add((row, col))
        if dis == 2:
            continue
        for dx, dy in move:
            nx, ny = dx + row, dy + col
            if 0 <= nx < 5 and 0 <= ny < 5 and (nx, ny) not in visit:
                if place[nx][ny] == 'O':
                    q.append((nx, ny, dis + 1))
                elif place[nx][ny] == 'P':
                    return False

    return True


def solution(places):
    answer = []

    for place in places:
        result = []
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    result.append(keep_distance_check((i, j), place))
        answer.append(1 if sum(result) == len(result) else 0)

    return answer


if __name__ == '__main__':
    places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
              ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
              ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
              ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
              ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]

    print(solution(places))