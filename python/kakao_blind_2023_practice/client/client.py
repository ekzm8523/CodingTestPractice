import requests
import json

"""
API_HOST = '[API_SERVER]'
headers = {
    'Access-Token': '[YOUR_ACCESS_TOKEN]',
    'Content-Type': 'application/json'
}
"""
API_HOST = 'http://localhost:5002'
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


def get_next(table):
    for i in range(3):
        for j in range(3):
            if table[i][j] is None:
                table[i][j] = 1
                return i, j



if __name__ == '__main__':
    # auth_key를 발급 받고, 문제 풀이 시작
    response = request('/start', 'GET')
    print(f'Response status: {response.status_code}')
    data = response.json()
    print(f'Response: {data}')
    key = data['auth_key']
    table = [[None] * 3 for _ in range(3)]
    if data['position'] != 'none':
        pos = eval(data["position"])
        if pos != "none":
            table[pos[0]][pos[1]] = 0

    not_lose_cnt = 0
    # game start
    while not_lose_cnt < 30:
        # turn은 무조건 사용자임
        next_pos = get_next(table)
        res = request("/query", "POST", {"auth_key": key, "position": str(next_pos)})
        body = res.json()
        x, y = eval(body['position'])
        table[x][y] = 0

        if "result" in body:
            if body["result"] in ("player win", "draw"):
                not_lose_cnt += 1
            elif body['result'] == "computer win":
                not_lose_cnt = 0
            else:  # 30번 이상 이겨서 얻은 FLAG
                print(body['result'])
                break
            for i in range(3):
                for j in range(3):
                    table[i][j] = None
            response = request('/start', 'GET')
            data = response.json()
            key = data['auth_key']
            pos = eval(data["position"])
            if pos != "none":
                table[pos[0]][pos[1]] = 0
