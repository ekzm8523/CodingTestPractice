"""
https://programmers.co.kr/learn/courses/30/lessons/81303
현재 up 이랑 down 이랑 반대로 되어있음 여기부터 고쳐야함 ㅁㅅㅁ...

"""

# from collections

def cmd_up(dic, row, step):
    if step == 0:
        return row
    return cmd_up(dic, dic[row][1], step-1)


def cmd_down(dic, row, step):
    if step == 0:
        return row
    return cmd_down(dic, dic[row][0], step-1)


def cmd_del(dic, delete_log, row):
    # undo를 위해 delete log를 남겨둬야함
    delete_log.append(row)
    next_row, before_row = dic[row]
    if before_row == -1:    # 맨 처음 row 였을때
        dic[row+1][0] = before_row
        dic[row] = None
        return next_row

    elif next_row == len(dic):  # 맨 마지막 row 였을때
        dic[row-1][1] = next_row
        dic[row] = None
        return before_row
    else:
        dic[row-1][1] = next_row
        dic[row+1][0] = before_row
        dic[row] = None
        return next_row


def cmd_undo(dic, k, row):
    next_row, before_row = row - 1, row + 1

    while before_row >= 0:
        if dic[before_row]:
            break
        before_row -= 1

    while next_row < k:
        if dic[next_row]:
            break
        next_row += 1

    dic[row] = [before_row, next_row]

    if before_row == -1 and next_row == k:
        return
    if before_row == -1:
        dic[next_row][0] = row
    if next_row == k:
        dic[before_row][1] = row


def solution(n, k, cmd):
    answer = ''
    delete_log = []

    dic = {i: [i-1, i+1] for i in range(n)}   # dic은 python 3.6부터 순서를 보장 set은 아직임


    for query in cmd:
        if query[0] == "U":
            k = cmd_up(dic, k, int(query[-1]))
        elif query[0] == "D":
            k = cmd_down(dic, k, int(query[-1]))
        elif query[0] == "C":
            cmd_del(dic, delete_log, k)

        elif query[0] == "Z":
            cmd_undo(dic, n, k)
    return answer


if __name__ == '__main__':
    n = 8
    k = 2
    cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]
    print(solution(n, k, cmd))

    n = 8
    k = 2
    cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]
    print(solution(n, k, cmd))