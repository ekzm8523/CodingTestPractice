
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
from collections import defaultdict


def solution(board, r, c):
    move = ((-1, 0), (0, 1), (1, 0), (0, -1))  # 시계방향
    min_move_count = math.inf
    pos_info = defaultdict(list)
    for row in range(4):
        for col in range(4):
            if board[row][col]:
                pos_info[board[row][col]].append((row, col))

    combinations = list(permutations(pos_info.keys(), len(pos_info)))

    print(combinations)

    def bfs(start, target, is_left_first):
        """
        start에서 target number를 is_left_first flag에 맞게 최단 거리로 순회하고 position을 return한다.
        """
        move_cnt = 0


    combination_size = len(pos_info)
    for combination in combinations:
        for i in range(2**combination_size):
            current_pos = (r, c)
            current_move_count = 0
            binary_set = f"{bin(i)[2:]:0{combination_size}}"
            for idx, card_number in enumerate(combination):
                current_pos, move_count = bfs(current_pos, card_number, binary_set[idx] == '0')
                current_move_count += move_count
            if current_move_count < min_move_count:
                min_move_count = current_move_count


    return min_move_count



if __name__ == '__main__':
    board = [[1, 0, 0, 3], [2, 0, 0, 0], [0, 0, 0, 2], [3, 0, 1, 0]]
    r, c = 1, 0
    print(solution(board, r, c))

    board = [[3, 0, 0, 2], [0, 0, 1, 0], [0, 1, 0, 0], [2, 0, 0, 3]]
    r, c = 1, 0
    print(solution(board, r, c))