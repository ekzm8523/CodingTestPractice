
# https://programmers.co.kr/learn/courses/30/lessons/72415
"""
문제 6 - 카드 짝 맞추기
1. 각 카드 쌍은 최대 6개이다. -> 6개의 쌍을 맞추는 조합은 최대 6! -> max combination count 720
ex ) 12345, 12354, 12435 ...
2. 순회할 순서가 정해지면 하나씩 맞춰본다
ex ) 1, 2, 3 순서라면 1-1, 1-2 가 있을거고 두개의 순서도 각각 넣어봐야 안다. 1-1, 1-2, 2-2, 2-1, 3-2, 3-1 -> 2^N 조합 -> max 64

최대 720 * 64 가지의 조합을 bfs로 최단거리를 구한다.

"""
import math
from itertools import permutations
from collections import defaultdict, deque
INF = math.inf


def ctrl_move(board, x, y, dx, dy):
    while True:
        nx = x + dx
        ny = y + dy
        if nx < 0 or nx >= 4 or ny < 0 or ny >= 4:
            return x, y

        else:
            if board[nx][ny] != 0:
                return nx, ny
            x, y = nx, ny


def solution(board, r, c):
    move = ((-1, 0), (0, 1), (1, 0), (0, -1))  # 시계방향
    min_move_count = INF
    pos_info = defaultdict(list)
    for row in range(4):
        for col in range(4):
            if board[row][col]:
                pos_info[board[row][col]].append((row, col))

    combinations = list(permutations(pos_info.keys(), len(pos_info)))

    def bfs(test_board, start, target) -> int:
        move_cnt = 0
        distance_table = [[INF for _ in range(4)] for _ in range(4)]
        q = deque()
        x, y = start
        q.append((x, y, 0))
        distance_table[x][y] = 0
        while q:
            x, y, distance = q.popleft()
            distance += 1
            for dx, dy in move:
                nx, ny = dx + x, dy + y

                if 0 <= nx <= 3 and 0 <= ny <= 3 and distance_table[nx][ny] > distance:
                    distance_table[nx][ny] = distance
                    q.append((nx, ny, distance))
                    if (nx, ny) == target:
                        return distance
                nx, ny = ctrl_move(test_board, x, y, dx, dy)
                if distance_table[nx][ny] > distance:
                    distance_table[nx][ny] = distance
                    q.append((nx, ny, distance))
                    if (nx, ny) == target:
                        return distance
        return move_cnt

    combination_size = len(pos_info)
    for combination in combinations:
        for i in range(2**combination_size):
            current_pos = [r, c]
            current_move_count = 0
            binary_set = f"{bin(i)[2:]:0>{combination_size}}"

            test_board = [[col for col in row] for row in board]

            for idx, card_number in enumerate(combination):
                if binary_set[idx] == '0':
                    first_target, second_target = pos_info[card_number]
                else:
                    second_target, first_target = pos_info[card_number]
                current_move_count += bfs(test_board, current_pos, first_target)
                current_move_count += bfs(test_board, first_target, second_target)
                current_pos = second_target

                test_board[first_target[0]][first_target[1]] = test_board[second_target[0]][second_target[1]] = 0
                if current_move_count > min_move_count:
                    break
            if current_move_count < min_move_count:
                min_move_count = current_move_count

    return min_move_count + combination_size * 2



if __name__ == '__main__':
    board = [[1, 0, 0, 3], [2, 0, 0, 0], [0, 0, 0, 2], [3, 0, 1, 0]]
    r, c = 1, 0
    print(solution(board, r, c))

    board = [[3, 0, 0, 2], [0, 0, 1, 0], [0, 1, 0, 0], [2, 0, 0, 3]]
    r, c = 1, 0
    print(solution(board, r, c))