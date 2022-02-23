# https://programmers.co.kr/learn/courses/30/lessons/92344
"""
type 1 : 공격
type 2 : 회복
skill -> [type, r1, c1, r2, c2, degree]
"""

def solution(board, skill):
    answer = 0
    row_size = len(board)
    col_size = len(board[0])
    prefix_board = [[0 for _ in range(col_size)] for _ in range(row_size)]
    for t, r1, c1, r2, c2, degree in skill:
        if t == 1:
            degree *= -1

        prefix_board[r1][c1] += degree

        if c2 + 1 < col_size:
            prefix_board[r1][c2+1] -= degree
        if r2 + 1 < row_size:
            prefix_board[r2+1][c1] -= degree
            if c2 + 1 < col_size:
                prefix_board[r2 + 1][c2 + 1] += degree

    for row_idx in range(row_size):
        for col_idx in range(col_size-1):
            prefix_board[row_idx][col_idx+1] += prefix_board[row_idx][col_idx]
    for col_idx in range(col_size):
        for row_idx in range(row_size-1):
            prefix_board[row_idx + 1][col_idx] += prefix_board[row_idx][col_idx]

    for row_idx in range(row_size):
        for col_idx in range(col_size):
            if prefix_board[row_idx][col_idx] + board[row_idx][col_idx] > 0:
                answer += 1

    return answer


if __name__ == '__main__':
    board = [[5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5]]
    skill = [[1, 0, 0, 3, 4, 4], [1, 2, 0, 2, 3, 2], [2, 1, 0, 3, 1, 2], [1, 0, 1, 3, 3, 1]]
    print(solution(board, skill))

    board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    skill = [[1, 1, 1, 2, 2, 4], [1, 0, 0, 1, 1, 2], [2, 2, 0, 2, 0, 100]]
    print(solution(board, skill))
