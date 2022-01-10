"""
https://programmers.co.kr/learn/courses/30/lessons/42890
제한사항을 보니 완전탐색을 해도 충분히 통과할 것 같았다.
최대한 효율성있게 코드를 짜려고 노력했으며 가장 cost가 많이 드는 유일성을 먼저 최소성 check부터 하게 해서
검사하려는 후보키가 최소성검사에 걸리지 않을때만 검사하도록 했다.
여기서 더 효율적이게 만드려면 최소성 check를 bit mask를 이용하면 될 것 같다.
ㅋㅋㅋㅋㅋㅋ 비트마스크를 써봤는데 시간이 더 늘었다
최소성 check의 cost가 그리 높지 않아서 convert 비용이 더 들은듯
비트마스크 연습했다고 치지 뭐..
"""
import itertools
from math import log2


def solution(relation):
    column_size = len(relation[0])
    row_size = len(relation)
    combinations = []
    for combination_size in range(1, column_size+1):
        combinations.extend(list(map(set, itertools.combinations(range(column_size), combination_size))))

    candidate_keys = []
    for combination in combinations:
        is_minimality = True
        for candidate_key in candidate_keys:  # 최소성 check
            if candidate_key & combination == candidate_key:
                is_minimality = False
                break
        if is_minimality:
            s = set([tuple(row[key] for key in combination) for row in relation])
            if len(s) == row_size:  # 유일성
                candidate_keys.append(combination)

    return len(candidate_keys)
asdfasdfasdf

def int2bit(keys: tuple, length: int) -> int:
    """
    if length = 4, keys = (1, 3)
    bit is 0101
    return value is 5
    """
    board = ['0' for _ in range(length)]
    for key in keys:
        board[key] = '1'
    return int(''.join(board), 2)



def bit2key(bit: int) -> list:
    """
    if length = 4, bit = 5
    real bit is 0101
    return (1, 3)
    """
    keys = []
    while bit:
        idx = bit & -bit  # 0이 아닌 마지막 비트를 찾는 방법
        keys.append(int(log2(idx)))
        bit -= idx  # bit 값이 아닌 int 값으로 나오기 때문에 주의

    return keys


def solution_with_bitmask(relation):
    column_size = len(relation[0])
    row_size = len(relation)
    combinations = []
    for combination_size in range(1, column_size + 1):
        combination = list(itertools.combinations(range(column_size), combination_size))
        for comb in combination:
            combinations.append(int2bit(comb, column_size))


    candidate_keys = []
    for combination in combinations:
        is_minimality = True
        for candidate_key in candidate_keys:  # 최소성 check
            if candidate_key & combination == candidate_key:
                is_minimality = False
                break
        if is_minimality:
            key_combination = bit2key(combination)
            s = set([tuple(row[key] for key in key_combination) for row in relation])
            if len(s) == row_size:  # 유일성
                candidate_keys.append(combination)

    return len(candidate_keys)


if __name__ == '__main__':
    relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]
    print(solution_with_bitmask(relation))
