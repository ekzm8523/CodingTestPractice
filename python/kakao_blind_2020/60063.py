# https://school.programmers.co.kr/learn/courses/30/lessons/60063
from collections import deque


def block_ordering(block1, block2):
    if block1[0] == block2[0]:  # HORIZONTAL MODE
        return (block2, block1) if block1[1] > block2[1] else (block1, block2)
    return (block2, block1) if block1[0] > block2[0] else (block1, block2)   # VERTICAL MODE


def get_movable_block(block1, block2, new_board):
    move = ((0, 1), (1, 0), (0, -1), (-1, 0))
    movable_list = []
    for dx, dy in move:
        nx1, ny1 = block1[0] + dx, block1[1] + dy
        nx2, ny2 = block2[0] + dx, block2[1] + dy
        next_block = ((nx1, ny1), (nx2, ny2))
        if new_board[nx1][ny1] and new_board[nx2][ny2]:
            movable_list.append(next_block)

    direction = (1, -1)
    if block1[0] == block2[0]:  # HORIZONTAL_MODE
        for d in direction:
            if new_board[block1[0] + d][block1[1]] and new_board[block2[0] + d][block2[1]]:
                movable_list.append(block_ordering(block1, (block1[0] + d, block1[1])))
                movable_list.append(block_ordering(block2, (block2[0] + d, block2[1])))

    else:  # VERTICAL MODE
        for d in direction:
            if new_board[block1[0]][block1[1] + d] and new_board[block2[0]][block2[1] + d]:
                movable_list.append(block_ordering(block1, (block1[0], block1[1] + d)))
                movable_list.append(block_ordering(block2, (block2[0], block2[1] + d)))

    return movable_list


def solution(board):
    board_size = len(board)
    new_board = [[0 for _ in range(board_size + 2)] for _ in range(board_size + 2)]
    for i in range(board_size):
        for j in range(board_size):
            new_board[i+1][j+1] = 0 if board[i][j] else 1

    visit = set()
    start_blocks = ((1, 1), (1, 2))
    visit.add(start_blocks)
    q = deque()
    q.append((start_blocks, 0))

    while q:
        current_blocks, distance = q.popleft()
        movable_blocks = get_movable_block(*current_blocks, new_board)
        for next_block in movable_blocks:
            if (board_size, board_size) in next_block:
                return distance + 1

            if next_block not in visit:
                visit.add(next_block)
                q.append((next_block, distance + 1))

    return 0


if __name__ == '__main__':
    board = [[0, 0, 0, 1, 1], [0, 0, 0, 1, 0], [0, 1, 0, 1, 1], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0]]
    print(solution(board))
