# https://programmers.co.kr/learn/courses/30/lessons/64061

def solution(board, moves):

    n = len(board)

    stack_board = [[] for _ in range(n)]

    for i in range(n-1, -1, -1):
        for j in range(n):
            if board[i][j] != 0:
                stack_board[j].append(board[i][j])

    stack = []
    answer = 0
    for move in moves:
        move -= 1
        if stack_board[move]:
            v = stack_board[move].pop()

            if stack and stack[-1] == v:
                stack.pop()
                answer += 2
            else:
                stack.append(v)

    return answer


if __name__ == "__main__":

    board = [[0,0,0,0,0],
             [0,0,1,0,3],
             [0,2,5,0,1],
             [4,2,4,4,2],
             [3,5,1,3,1]]
    moves = [1,5,3,5,1,2,1,4]
    print(solution(board, moves))