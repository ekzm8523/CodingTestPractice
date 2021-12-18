# https://programmers.co.kr/learn/courses/30/lessons/17679
"""
2 * 2 sliding window
"""
from pprint import pprint

def sliding_window(m, n, board):
    erase_set = []
    for row in range(m-1):
        for col in range(n-1):
            target = board[row][col]

            if target and target == board[row][col+1] == board[row+1][col] == board[row+1][col+1]:
                erase_set.append((row, col))

    return erase_set


def drop_object(m, n, board):
    new_board = [[] for _ in range(n)]
    for row in range(m):
        for col in range(n):
            if board[row][col]:
                new_board[col].append(board[row][col])

    for col in range(n):
        size = len(new_board[col])
        for i in range(m - size):
            board[i][col] = None
        for i in range(size):
            board[m - size + i][col] = new_board[col][i]


def solution(m, n, board):
    answer = 0

    board = [[ch for ch in row] for row in board]
    erase_set = sliding_window(m, n, board)
    while erase_set:
        for x, y in erase_set:
            board[x][y] = board[x+1][y] = board[x][y+1] = board[x+1][y+1] = None
        drop_object(m, n, board)
        erase_set = sliding_window(m, n, board)

    for row in board:
        for col in row:
            if not col:
                answer += 1
    return answer


if __name__ == '__main__':
    m, n = 4, 5
    board = ["CCBDE", "AAADE", "AAABF", "CCBBF"]
    print(solution(m, n, board))

    m, n = 6, 6
    board = ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]
    print(solution(m, n, board))
