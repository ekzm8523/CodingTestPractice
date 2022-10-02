from flask import Flask, request
import uuid
import random
import sys
sys.setrecursionlimit(1000000) # 재귀 깊이 제한 변경


# 특정한 플레이어(player)가 이겼는지 알려주는 함수
def is_win(player, access_token, auth_key):
    board = candidates[access_token][auth_key]['board']
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
def get_score(access_token, auth_key):
    if is_win('O', access_token, auth_key):
        return 1
    elif is_win('X', access_token, auth_key):
        return -1
    else:
        return 0


def minimax(player, cnt, access_token, auth_key): # (현재 플레이어, 현재까지 둔 돌의 개수)
    board = candidates[access_token][auth_key]['board']
    # 더 둘 곳이 없거나, 승부가 난 경우 확인
    score = get_score(access_token, auth_key)
    if cnt == 9 or score != 0:
        return score, None # 점수 반환
    if player == 'O': # maximizing player
        max_value = -int(1e9)
        for i in range(3):
            for j in range(3):
                # 백트래킹(backtracking) 수행
                if board[i][j] == '_':
                    board[i][j] = 'O'
                    value = minimax('X', cnt + 1, access_token, auth_key)[0]
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
                    value = minimax('O', cnt + 1, access_token, auth_key)[0]
                    if min_value > value:
                        min_position = i, j
                        min_value = value
                    board[i][j] = '_'
        return min_value, min_position


app = Flask(__name__)
# 등록된 참가자마다 각 시도를 [auth_key: {player, board, cnt}, ...] 형태로 저장하고, 연속으로 비기거나 이긴 횟수(continous)를 저장
candidates = {
    'ABCDEFGH12345678': {
        'continous': 0
    }
}
flag = 'MINIMAX_KING'
target = 30 # 연속으로 비기거나 이긴 횟수가 30 이상이라면 FLAG 반환


@app.route('/start', methods=['GET'])
def create():
    access_token = request.headers.get('Access-Token')
    # 사전에 등록된 참가자가 아닌 경우
    if access_token not in candidates:
        return {
            'status': 'unknown candidate'
        }
    # 현재 시도에 대한 대한 키(auth_key) 발급
    auth_key = str(uuid.uuid4())
    player = random.randint(0, 1) # 플레이어(player)의 순서 설정
    if player == 0:
        player = 'O'
        board = [
            ['_', '_', '_'],
            ['_', '_', '_'],
            ['_', '_', '_']
        ]
        cnt = 0
        position = 'none'
    else:
        # 컴퓨터가 'O'인 경우 바로 돌을 놓음
        player = 'X'
        board = [
            ['_', '_', '_'],
            ['_', 'O', '_'],
            ['_', '_', '_']
        ]
        cnt = 1
        position = '(1,1)'
    data = {
        'player': player, # 플레이어의 돌
        'board': board, # 바둑판의 상태
        'cnt': cnt # 현재 놓인 돌의 개수
    }
    candidates[access_token][auth_key] = data
    print(f'[New] {data}')
    # 클라이언트(client)에게 결과 반환
    return {
        'status': 'success',
        'auth_key': auth_key,
        'position': position
    }


@app.route('/query', methods=['POST'])
def index():
    access_token = request.headers.get('Access-Token')
    # 사전에 등록된 참가자가 아닌 경우
    if access_token not in candidates:
        return {
            'status': 'unknown candidate'
        }
    params = request.get_json()
    # auth_key가 올바르지 않을 때
    auth_key = params['auth_key']
    if auth_key not in candidates[access_token]:
        return {
            'status': 'unknown authentication key'
        }
    # 클라이언트(client)로부터 제출 받은 값
    if 'position' not in params:
        return {
            'status': 'position is needed'
        }
    position = params['position']
    try:
        x, y = map(int, position[1:-1].split(','))
        value = candidates[access_token][auth_key]['board'][x][y]
    except: # 클라이언트가 보낸 위치(position) 값이 비정상인 경우
        return {
            'status': 'invalid position'
        }

    # 현재 플레이어의 상태 불러오기
    player = candidates[access_token][auth_key]['player']
    board = candidates[access_token][auth_key]['board']

    if board[x][y] != '_': # 이미 돌이 놓인 위치인 경우
        print(f'[Taken] {candidates[access_token][auth_key]}')
        return {
            'status': 'already taken position',
        }

    # 플레이어가 돌 놓기
    candidates[access_token][auth_key]['board'][x][y] = player
    candidates[access_token][auth_key]['cnt'] += 1
    print(f'[Place] {candidates[access_token][auth_key]}')

    # 게임이 끝났다면 승패 여부 반환
    score = get_score(access_token, auth_key)
    # 점수(score)가 1 혹은 -1로 변경되는 경우는 [플레이어 승리]인 경우임
    if score == 1 or score == -1:
        result = 'player win'
        candidates[access_token]['continous'] += 1
        if candidates[access_token]['continous'] >= target:
            result = flag
        return {
            'status': 'success',
            'result': result
        }
    # 비기는 경우
    elif candidates[access_token][auth_key]['cnt'] == 9:
        result = 'draw'
        candidates[access_token]['continous'] += 1
        if candidates[access_token]['continous'] >= target:
            result = flag
        return {
            'status': 'success',
            'result': result
        }

    # 컴퓨터(computer)가 돌을 놓을 위치 계산
    cnt = candidates[access_token][auth_key]['cnt']
    computer = 'X' if player == 'O' else 'O'
    _, position = minimax(computer, cnt, access_token, auth_key)
    x, y = position

    # 컴퓨터가 돌 놓기
    candidates[access_token][auth_key]['board'][x][y] = computer
    candidates[access_token][auth_key]['cnt'] += 1
    print(f'[Place] {candidates[access_token][auth_key]}')

    # 게임이 끝났다면 승패 여부 반환
    score = get_score(access_token, auth_key)
    # 점수(score)가 1 혹은 -1로 변경되는 경우는 [컴퓨터 승리]인 경우임
    if score == 1 or score == -1:
        result = 'computer win'
        candidates[access_token]['continous'] = 0
        return {
            'status': 'success',
            'result': result,
            'position': '(' + str(x) + ',' + str(y) + ')'
        }
    # 비기는 경우
    elif candidates[access_token][auth_key]['cnt'] == 9:
        result = 'draw'
        candidates[access_token]['continous'] += 1
        if candidates[access_token]['continous'] >= target:
            result = flag
        return {
            'status': 'success',
            'result': result,
            'position': '(' + str(x) + ',' + str(y) + ')'
        }

    # 컴퓨터가 돌을 놓은 위치 반환
    return {
        'status': 'success',
        'position': '(' + str(x) + ',' + str(y) + ')'
    }


app.run(host="localhost", port=5002)
