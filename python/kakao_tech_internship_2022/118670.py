# https://school.programmers.co.kr/learn/courses/30/lessons/118670
"""
Shift Row 를 효율적이게 하는 방법
dict로 row를 표현하고 key값만 switching 하면 row수만큼만 돌면 됨

Rotate를 효율적이게 하는 방법
row들을 바끄는건 어쩔 수 없고 각각의 dict로 표현된 row를 deque로 한다면 coloum rotate는 O(1)로 할 수 있고 row만 O(row_size) 만큼 돌면 됨
그럼 모든 명령의 시간복잡도는 O(row_size)니까 50000 * 100000 -> 50억
아마 시간초과가 날 것 같은데 행길이 * 열길이가 100,000 이라는 제한을 준걸 보니 만약 열이 컬럼보다 더 크다면 반시계반향으로 90도를 꺾어주면 row가 가장 길어봐야 1000일듯??

deque[-1]도 시간복잡도 1이라고는 하는데 테스팅이 필요할 것 같다.

-> 그것보다 row만 deque로 관리해주는게 아니라 모서리 네 방향을 전부 deque로 관리하면 되잖아?

"""
from collections import deque


def solution(rc, operations):
    row_size, col_size = len(rc), len(rc[0])
    row_order = deque(range(row_size))
    table = {i: deque(rc[i][1:-1]) for i in range(row_size)}
    left_col, right_col = deque((rc[i][0] for i in range(row_size))), deque((rc[i][-1] for i in range(row_size)))

    for operation in operations:
        top_row, bottom_row = table[row_order[0]], table[row_order[-1]]
        if operation[0] == "R":  # Rotation
            top_row.appendleft(left_col.popleft())
            right_col.appendleft(top_row.pop())
            bottom_row.append(right_col.pop())
            left_col.append(bottom_row.popleft())
        else:  # ShiftRow
            row_order.rotate()
            left_col.rotate()
            right_col.rotate()
    new_table = [[0] * col_size for _ in range(row_size)]
    for real_row, row in enumerate(row_order):
        new_table[real_row][0], new_table[real_row][-1] = left_col.popleft(), right_col.popleft()
        new_table[real_row][1:-1] = table[row]

    return new_table


if __name__ == '__main__':
    # rc = [[1, 2], [3, 4], [5, 6]]
    # operations = ["Rotate", "ShiftRow"]
    # print(solution(rc, operations))

    rc = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    operations = ["Rotate", "ShiftRow"]
    print(solution(rc, operations))

    rc = [[8, 6, 3], [3, 3, 7], [8, 4, 9]]
    operations = ["Rotate", "ShiftRow", "ShiftRow"]
    print(solution(rc, operations))

    rc = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    operations = ["ShiftRow", "Rotate", "ShiftRow", "Rotate"]
    print(solution(rc, operations))
