import sys
sys.setrecursionlimit(1000000) # 재귀 깊이 제한 변경


# 특정한 플레이어(player)가 이겼는지 알려주는 함수
def is_win(player):
    # 각 행을 확인
    for i in range(3):
        if board[i][0] == player and board[i][1] == player and board[i][2] == player:
            return True
    # 각 열을 확인
    for i in range(3):
        if board[0][i] == player and board[1][i] == player and board[2][i] == player:
            return True
    # 두 대각선을 확인
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    return False


# 먼저 두는 'O'의 점수(score = utility)를 계산하는 함수
def get_score():
    if is_win('O'):
        return 1
    elif is_win('X'):
        return -1
    else:
        return 0


def minimax(player, cnt): # (현재 플레이어, 현재까지 둔 돌의 개수)
    # 더 둘 곳이 없거나, 승부가 난 경우 확인
    score = get_score()
    if cnt == 9 or score != 0:
        return score, None # 점수 반환
    if player == 'O': # maximizing player
        max_value = -int(1e9)
        for i in range(3):
            for j in range(3):
                # 백트래킹(backtracking) 수행
                if board[i][j] == '_':
                    board[i][j] = 'O'
                    value = minimax('X', cnt + 1)[0]
                    if max_value < value:
                        max_position = i, j
                        max_value = value
                    board[i][j] = '_'
        return max_value, max_position
    elif player == 'X': # minimizing player
        min_value = int(1e9)
        for i in range(3):
            for j in range(3):
                # 백트래킹(backtracking) 수행
                if board[i][j] == '_':
                    board[i][j] = 'X'
                    value = minimax('O', cnt + 1)[0]
                    if min_value > value:
                        min_position = i, j
                        min_value = value
                    board[i][j] = '_'
        return min_value, min_position


# 게임 설정 초기화
board = [
    ['_', '_', '_'],
    ['_', '_', '_'],
    ['_', '_', '_']
]
player = 'O' # 플레이어 O가 먼저 시작

# 돌아가면서 최선의 위치에 돌을 놓기
cnt = 0
while True:
    # 현재 플레이어가 두어야 하는 최선의 위치 탐색
    value, position = minimax(player, cnt)
    x, y = position
    board[x][y] = player # 돌을 놓기
    cnt += 1
    print("=======")
    for i in range(3):
        for j in range(3):
            print(board[i][j], end=' ')
        print()
    # 게임이 끝난 뒤에 승패 여부 출력
    score = get_score()
    if score == 1:
        print('Player O win!')
        break
    elif score == -1:
        print('Player X win!')
        break
    elif cnt == 9:
        print('Draw!')
        break
    # 다음에 돌을 두어야 하는 플레이어 변경(스위치)하기
    if player == 'O': player = 'X'
    else: player = 'O'
