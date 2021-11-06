"""
https://programmers.co.kr/learn/courses/30/lessons/81303
"""
from pprint import pprint

def cmd_up(dic, row, step):
    while step > 0:
        step -= 1
        row = dic[row][0]
    return row


def cmd_down(dic, row, step):
    while step > 0:
        step -= 1
        row = dic[row][1]
    return row


def cmd_del(dic, delete_log, row):
    # undo를 위해 delete log를 남겨둬야함
    before_row, next_row = dic[row]
    delete_log.append((row, before_row, next_row))

    # 맨 처음이자 마지막인 row가 삭제되는 경우는 없음

    if before_row == -1:    # 맨 처음 row 였을때
        dic[next_row][0] = before_row
        dic[row] = None
        return next_row

    elif next_row == len(dic):  # 맨 마지막 row 였을때
        dic[before_row][1] = next_row
        dic[row] = None
        return before_row
    else:
        dic[before_row][1] = next_row
        dic[next_row][0] = before_row
        dic[row] = None
        return next_row


def cmd_undo(dic, undo_info):
    key, before_row, next_row = undo_info
    dic[key] = [before_row, next_row]

    if next_row != len(dic):
        dic[next_row][0] = key

    if before_row != -1:
        dic[before_row][1] = key


def solution(n, k, cmd):
    delete_log = []

    dic = {i: [i-1, i+1] for i in range(n)}   # dic은 python 3.6부터 순서를 보장 set은 아직임

    for query in cmd:
        if query[0] == "U":
            k = cmd_up(dic, k, int(query.split()[-1]))
        elif query[0] == "D":
            k = cmd_down(dic, k, int(query.split()[-1]))
        elif query[0] == "C":
            k = cmd_del(dic, delete_log, k)

        elif query[0] == "Z":
            cmd_undo(dic, delete_log.pop())

    return ''.join(['X' if value is None else 'O' for value in dic.values()])


if __name__ == '__main__':
    n = 8
    k = 2
    cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]
    print(solution(n, k, cmd))

    n = 8
    k = 2
    cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]
    # cmd = ["C", "C", "C", "U 2", "C", "C", "C", "Z", "Z", "Z", "D 1", "C", "C", "C", "C", "Z", "Z", "Z", "C", "C", "D 1", "C", "Z", "Z", "Z", "Z", "Z", "Z", "Z",
    #        "D 2", "C", "U 6", "C", "D 5", "C", "C", "U 3", "Z", "Z", "Z", "D 5", "C", "C", "U 3", "C", "U 1", "C", "D 1", "C", "Z", "Z", "Z", "Z", "Z", "Z",
    #        "D 2", "D 1", "C"]
    print(solution(n, k, cmd))