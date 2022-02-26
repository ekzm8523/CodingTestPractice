"""
https://programmers.co.kr/learn/courses/30/lessons/92345/solution_groups?language=python3
minmax algorithm 을 사용해야하는 문제이며 보통 게임 인공지능에서 가장 기본적인 알고리즘이다.
(쉽다는건 아니다.)

"""


def solution(board, aloc, bloc):
    move = ((-1, 0), (0, 1), (1, 0), (0, -1))  # 시계방향
    row_size = len(board)
    col_size = len(board[0])

    def dfs(x, y, x2, y2):
        nonlocal board
        if board[x][y] == 0:  # 두 플레이어가 함께 있다가 떠난 경우
            return 0

        current_move_cnt = 0  # 아무곳도 갈 수 없으면 0이 return 될거임
        for dx, dy in move:
            nx, ny = x + dx, y + dy
            if 0 <= nx < row_size and 0 <= ny < col_size and board[nx][ny] == 1:
                board[x][y] = 0
                new_move_cnt = dfs(x2, y2, nx, ny) + 1  # 턴 바꿔서 돌리기
                board[x][y] = 1

                # 현재 지는 턴인데 새로운 턴은 이길 때 -> 이기는 쪽의 값을 저장
                if current_move_cnt % 2 == 0 and new_move_cnt % 2 == 1:
                    current_move_cnt = new_move_cnt
                # 현재 턴과 다음 턴 둘다 질때 -> 최대한 늦게 져야함
                elif current_move_cnt % 2 == 0 and new_move_cnt % 2 == 0:
                    current_move_cnt = max(current_move_cnt, new_move_cnt)
                # 현재 턴과 다음 턴 둘다 이길때 -> 최대한 빨리 이겨야함
                elif current_move_cnt % 2 == 1 and new_move_cnt % 2 == 1:
                    current_move_cnt = min(current_move_cnt, new_move_cnt)
                # 현재 이기고 있는데 질때? 무시함

        return current_move_cnt

    return dfs(aloc[0], aloc[1], bloc[0], bloc[1])


if __name__ == '__main__':
    board = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
    aloc = [1, 0]
    bloc = [1, 2]
    print(solution(board, aloc, bloc))

    board = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    aloc = [1, 0]
    bloc = [1, 2]
    print(solution(board, aloc, bloc))

    board = [[1, 1, 1, 1, 1]]
    aloc = [0, 0]
    bloc = [0, 4]
    print(solution(board, aloc, bloc))

    board = [[1]]
    aloc = [0, 0]
    bloc = [0, 0]
    print(solution(board, aloc, bloc))