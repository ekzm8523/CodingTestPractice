
"""
https://programmers.co.kr/learn/courses/30/lessons/60059
열쇠는 회전과 이동이 가능
열쇠의 돌기와 자물쇠의 돌기가 만나서는 안된다.
열쇠는 회전하고 이동해서 자물쇠를 열 수 있으면 true, 없으면 false
N >= M, 둘다 2차원 정사각 배열, shape 틀릴 수 있다.
"""
from collections import Counter

def check_answer(results, answers):
    for i, (result, answer) in enumerate(zip(results, answers)):
        if result == answer:
            print(f"{i + 1}번 정답")
        else:
            print(f"{'*' * 10} {i + 1}번 오답 {'*' * 10}\n 정답 -> {answer} \n 내꺼 -> {result}")


def rotate_90(key):
    M = len(key)
    table = [[0] * M for _ in range(M)]
    for i in range(M):
        for j in range(M):
            if key[i][j]:
                table[j][M - i - 1] = 1

    return table


def rotate_180(key):
    M = len(key)
    table = [[0] * M for _ in range(M)]
    for i in range(M):
        for j in range(M):
            if key[i][j]:
                table[M - i - 1][M - j - 1] = 1

    return table


def rotate_270(key):
    M = len(key)
    table = [[0] * M for _ in range(M)]
    for i in range(M):
        for j in range(M):
            if key[i][j]:
                table[M - j - 1][i] = 1

    return table


def move_right(key):
    M = len(key)
    table = [[0] * M for _ in range(M)]
    for i in range(M):
        for j in range(0, M - 1):
            table[i][j+1] = key[i][j]

    return table


def move_left(key):
    M = len(key)
    table = [[0] * M for _ in range(M)]
    for i in range(M):
        for j in range(0, M - 1):
            table[i][j] = key[i][j+1]

    return table


def move_down(key):
    M = len(key)
    table = [[0] * M for _ in range(M)]
    for i in range(M - 1):
        for j in range(M):
            table[i+1][j] = key[i][j]

    return table


def move_up(key):
    M = len(key)
    table = [[0] * M for _ in range(M)]
    for i in range(M - 1):
        for j in range(M):
            table[i][j] = key[i+1][j]

    return table


def is_unlock_table(table):

    for row in table:
        for value in row:
            if not value:
                return False

    return True


def is_unlock(key, lock, right, down):
    """
    이차원 배열과 시작점 index를 받아 자물쇠가 열리는지 확인
    """

    M, N = len(key), len(lock)

    if (right + M) > N or (down + M) > N:
        print(f"****** out of range *******")
        return False

    table = lock.copy()

    for i in range(M):
        for j in range(M):
            if table[i + down][j + right] and key[i][j]:    # 돌기와 돌기가 만났을 때
                return False
            table[i + down][j + right] = table[i + down][j + right] or key[i][j]

    return is_unlock_table(table)


def solution(key, lock):

    M, N = len(key), len(lock)

    ori_key = key.copy()

    def unlock(key, lock):
        for right in range(N - M + 1):
            for down in range(N - M + 1):
                if is_unlock(key, lock, right, down):
                    return True
        return False
    for angle in range(4):

        key = ori_key.copy()
        for i in range(M):
            if unlock(key, lock):
                return True
            key = move_right(key)

        key = ori_key.copy()
        for i in range(M):
            if unlock(key, lock):
                return True
            key = move_left(key)

        key = ori_key.copy()
        for i in range(M):
            if unlock(key, lock):
                return True
            key = move_down(key)

        key = ori_key.copy()
        for i in range(M):
            if unlock(key, lock):
                return True
            key = move_up(key)
        ori_key = rotate_90(ori_key)
    return False

if __name__ == "__main__":
    key = [[0, 0, 0], [1, 0, 1], [0, 1, 1]]

    lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    answer = [True]
    result = []
    result.append(solution(key, lock))
    check_answer(result, answer)