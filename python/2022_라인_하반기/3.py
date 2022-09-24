from collections import deque
from typing import List

ice_move = [(-1, 0), (0, 1), (1, 0), (0, -1)]
fire_move = [(-1, 0), (0, 1), (1, 0), (0, -1), (-1, 1), (1, 1), (1, -1), (-1, -1)]


def solution(n: int, m: int, fires: List[List[int]], ices: List[List[int]]) -> List[List[int]]:
    record_table = [[0] * n for _ in range(n)]

    def bfs(totem_pos: List[int], is_fire: bool):

        visit = [[False] * n for _ in range(n)]
        q = deque()
        x, y = totem_pos
        q.append((x, y, 0))

        while q:
            x, y, distance = q.popleft()

            sign, moves = (1, fire_move) if is_fire else (-1, ice_move)
            if distance == 0:
                record_table[x][y] = record_table[x][y] + sign * m
                visit[x][y] = True
            else:
                record_table[x][y] = record_table[x][y] + sign * (m - (distance - 1))
            if distance < m:  # 다음을 탐색할 이유가 있을 때
                for dx, dy in moves:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < n and not visit[nx][ny]:
                        visit[nx][ny] = True
                        q.append((nx, ny, distance + 1))

    for fire in fires:
        fire[0], fire[1] = fire[0] - 1, fire[1] - 1
        bfs(fire, is_fire=True)
    for ice in ices:
        ice[0], ice[1] = ice[0] - 1, ice[1] - 1
        bfs(ice, is_fire=False)

    return record_table


if __name__ == '__main__':
    print(solution(3, 2, [[1, 1]], [[3, 3]]))
    print(solution(5, 3, [[5, 5], [1, 3], [5, 2]], [[1, 5], [3, 2]]))
