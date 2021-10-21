"""
https://programmers.co.kr/learn/courses/30/lessons/81303
"""

# from collections

def cmd_up(row, step):



def cmd_down():
    ...


def cmd_del():
    # undo를 위해 delete log를 남겨둬야함
    ...


def cmd_undo():
    ...


def solution(n, k, cmd):
    answer = ''
    delete_log = []

    dic = {i: i+1 for i in range(n)}   # dic은 python 3.6부터 순서를 보장 set은 아직임
    delete_set = set()

    for query in cmd:
        if query[0] == "U":
            k += int(query[-1])
        elif query[0] == "D":
            k -= int(query[-1])
        elif query[0] == "C":
            delete_log.append(k)

        elif query[0] == "Z":
            cmd_undo()
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