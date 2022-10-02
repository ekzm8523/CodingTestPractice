import requests, json
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


"""
API_HOST = '[API_SERVER]'
headers = {
    'Access-Token': '[YOUR_ACCESS_TOKEN]',
    'Content-Type': 'application/json'
}
"""
API_HOST = 'http://localhost:5000'
headers = {
    'Access-Token': 'ABCDEFGH12345678',
    'Content-Type': 'application/json'
}

def request(path, method, data={}):
    url = API_HOST + path
    print(f'Request URL: {url}')
    print(f'HTTP Method: {method}')
    print(f'Headers: {headers}')

    if method == 'GET':
        return requests.get(url, headers=headers)
    elif method == 'POST':
        print(f'Sended data: {data}')
        return requests.post(url, headers=headers, data=json.dumps(data))


# FLAG를 얻을 때까지 게임을 반복 실행
game_count = 0
while True:
    # auth_key를 발급 받고, 문제 풀이 시작
    response = request('/start', 'GET')
    print(f'Response status: {response.status_code}')
    data = response.json()
    print(f'Response: {data}')
    key = data['auth_key']

    # 게임 설정 초기화
    board = [
        ['_', '_', '_'],
        ['_', '_', '_'],
        ['_', '_', '_']
    ]

    # 컴퓨터로부터 위치(position) 정보 받기
    position = data['position']
    if position == 'none':
        cnt = 0
        player = 'O'
    else:
        x, y = map(int, position[1:-1].split(','))
        board[x][y] = 'O'
        cnt = 1
        player = 'X'
    print("=======")
    for i in range(3):
        for j in range(3):
            print(board[i][j], end=' ')
        print()

    # 최선의 위치에 돌을 놓기
    while True:
        _, position = minimax(player, cnt)
        x, y = position
        board[x][y] = player
        print("=======")
        for i in range(3):
            for j in range(3):
                print(board[i][j], end=' ')
            print()

        # 서버(server)에 보낼 데이터 생성
        data = {
            'auth_key': key,
            'position': '(' + str(x) + ',' + str(y) + ')'
        }
        
        # 서버에 데이터를 전송한 뒤에 응답(response) 받기
        print('==============================================')
        response = request('/query', 'POST', data)
        print(f'Response status: {response.status_code}')
        data = response.json()
        print(f'Response: {data}')

        cnt += 1
        if "result" in data: # 게임이 끝난 경우(누군가 승리 혹은 무승부)
            print("[Terminated] Judge:", data["result"])
            break

        # 컴퓨터로부터 위치(position) 정보 받기
        position = data['position']
        x, y = map(int, position[1:-1].split(','))
        computer = 'X' if player == 'O' else 'O'
        board[x][y] = computer
        print("=======")
        for i in range(3):
            for j in range(3):
                print(board[i][j], end=' ')
            print()

        cnt += 1
        if "result" in data: # 게임이 끝난 경우(누군가 승리 혹은 무승부)
            print("[Terminated] Judge:", data["result"])
            break

    game_count += 1
    print("[Game Count]", game_count)
    if game_count == 30:
        print("[FLAG]", data["result"])
        break
