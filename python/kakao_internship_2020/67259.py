"""
직선 - 100원
코너 - 500원
bfs 로 풀되 각 위치에 memorization 을 한다.
1 번째 함정 : memorization으로 하되 방향 + cost의 조합이 있기 때문에 memo[nx][ny] = memo[x][y] + 100 이런식으로 참조하면 안되고
            그 방향에 cost를 q로 넣어줘야함
2 번째 함정 : 처음에는 bfs 한번만 돌리고 init queue에 두개의 시작점을 넣어줬을때 오답이 나올수가 있음
            -> 왜냐하면 memorization에는 방향이 들어있지 않기 때문

"""
from pprint import pprint
import math
from collections import deque

def is_move(size, row, col):
    return 0 <= row < size and 0 <= col < size

def solution(board: list):
    size = len(board)
    move = ((-1, 0), (0, 1), (1, 0), (0, -1))   # 방향 convention -> 0: 위 , 1: 오른쪽, 2: 아래, 3: 왼쪽

    def bfs(*start):
        q = deque([start])  # position(x, y), direction
        memorization = [[math.inf] * size for _ in range(size)]
        memorization[0][0] = 0
        while q:
            x, y, cost, head = q.popleft()
            for next_head, (dx, dy) in enumerate(move):
                nx, ny = x + dx, y + dy
                n_cost = cost + 100 if head == next_head else cost + 600
                if is_move(size, nx, ny) and board[nx][ny] == 0 and (next_head + 2) % 4 != head:
                    if memorization[nx][ny] > n_cost:
                        memorization[nx][ny] = n_cost
                        q.append((nx, ny, n_cost, next_head))

        return memorization[-1][-1]

    return min(bfs(0, 0, 0, 1), bfs(0, 0, 0, 2))


if __name__ == '__main__':
    board = [[0,0,0],[0,0,0],[0,0,0]]
    print(solution(board))
    board = [[0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0],
     [0, 0, 0, 1, 0, 0, 0, 1], [0, 0, 1, 0, 0, 0, 1, 0], [0, 1, 0, 0, 0, 1, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0]]
    print(solution(board))
    board = [[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]]
    print(solution(board))
    board = [[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]]
    print(solution(board))