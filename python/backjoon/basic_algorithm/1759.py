# https://www.acmicpc.net/problem/1759
"""
서로 다른 L개의 알파벳 소문자, 최소 한 개의 모음(a, e, i, o, u), 최소 두 개의 자음
정렬된 문자열
C개의 문자로 만들 수 있는 암호를 모두 구하기
"""
from itertools import combinations

if __name__ == "__main__":
    l, c = map(int, input().split())

    gather = set(['a', 'e', 'i', 'o', 'u'])
    ontology = sorted(input().split())

    combs = tuple(combinations(ontology, l))

    for comb in combs:
        gather_cnt = 0
        for ch in comb:
            if ch in gather:
                gather_cnt += 1

        if 1 <= gather_cnt <= l - 2:
            print(''.join(comb))
