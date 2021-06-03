# https://programmers.co.kr/learn/courses/30/lessons/77485

from pprint import pprint

def rotate(ar, q):

    x = q[0] - 1
    y = q[1] - 1
    dx = q[2] - q[0]
    dy = q[3] - q[1]
    pre_val = ar[x][y]
    save_tmp = [ar[x][y]]
    for col in range(y, y + dy):
        save_tmp.append(ar[x][col + 1])
        ar[x][col + 1] = save_tmp[-2]

    for row in range(x, x + dx):
        save_tmp.append(ar[row + 1][y + dy])
        ar[row + 1][y + dy] = save_tmp[-2]

    for col in range(y + dy, y, -1):
        save_tmp.append(ar[x + dx][col - 1])
        ar[x + dx][col - 1] = save_tmp[-2]


    for row in range(x + dx, x, -1):
        save_tmp.append(ar[row - 1][y])
        ar[row - 1][y] = save_tmp[-2]

    return ar, min(save_tmp)

def solution(rows, columns, queries):
    """
    :param rows: 행 개수
    :param columns: 열 개수
    :param queries: [x1, y1, x2, y2] 이게 한 쿼리 (여러개)
    :return: 회전 후 배
    """
    ar = []
    for row in range(rows):
        r = []
        for col in range(columns):
            r.append(row*columns + col + 1)
        ar.append(r)
    answer = []
    for q in queries:
        ar, min_num = rotate(ar, q)
        answer.append(min_num)
        # 돌아야 하는 횟수 : (q[2] - q[0]) * 2 +

    return answer


if __name__ == "__main__":
    rows1 = 6
    rows2 = 3
    rows3 = 100
    columns1 = 6
    columns2 = 3
    columns3 = 97

    queries1 = [[2,2,5,4],[3,3,6,6],[5,1,6,3]]  # [8, 10, 25]
    queries2 = [[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]    # [1, 1, 5, 3]
    queries3 = [[1,1,100,97]]   # [1]

    print(solution(rows1, columns1, queries1))
    print(solution(rows2, columns2, queries2))
    print(solution(rows3, columns3, queries3))
