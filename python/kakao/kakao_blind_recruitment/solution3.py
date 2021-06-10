
"""
https://programmers.co.kr/learn/courses/30/lessons/60059
열쇠는 회전과 이동이 가능
열쇠의 돌기와 자물쇠의 돌기가 만나서는 안된다.
열쇠는 회전하고 이동해서 자물쇠를 열 수 있으면 true, 없으면 false
N >= M, 둘다 2차원 정사각 배열, shape 틀릴 수 있다.
"""

def check_answer(results, answers):
    for i, (result, answer) in enumerate(zip(results, answers)):
        if result == answer:
            print(f"{i + 1}번 정답")
        else:
            print(f"{'*' * 10} {i + 1}번 오답 {'*' * 10}\n 정답 -> {answer} \n 내꺼 -> {result}")


def attach(x, y, M, key, board):
    for i in range(M):
        for j in range(M):
            board[x+i][y+j] += key[i][j]


def detach(x, y, M, key, board):
    for i in range(M):
        for j in range(M):
            board[x+i][y+j] -= key[i][j]


def rotate90(arr):
    return list(zip(*arr[::-1]))


def check(board, M, N):
    for i in range(N):
        for j in range(N):
            if board[M+i][M+j] != 1:
                return False
    return True


def solution(key, lock):
    M, N = len(key), len(lock)

    board = [[0] * (M * 2 + N) for _ in range(M * 2 + N)]
    # 자물쇠 중앙 배치
    for i in range(N):
        for j in range(N):
            board[M + i][M + j] = lock[i][j]

    rotated_key = key
    # 모든 방향 (4번 루프)
    for _ in range(4):
        rotated_key = rotate90(rotated_key)
        for x in range(1, M + N):
            for y in range(1, M + N):
                # 열쇠 넣어보기
                attach(x, y, M, rotated_key, board)
                # lock 가능 check
                if (check(board, M, N)):
                    return True
                # 열쇠 빼기
                detach(x, y, M, rotated_key, board)

    return False


if __name__ == "__main__":
    key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]

    lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    answer = [True]
    result = []
    result.append(solution(key, lock))
    check_answer(result, answer)