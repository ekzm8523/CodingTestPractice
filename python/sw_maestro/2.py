"""
insert -> 덮어쓰기
find -> 1 ~ N 까지 순차 탐색, 처음으로 만난 키의 메모리 크기 출력 -> 없을때는 None, k라는 키가 여러 레벨에 존재할 수 있음
avalanche -> 다음 레벨로 옮기는데 중복키는 덮어쓰기
"""
from collections import defaultdict
import sys


def main():
    level_cnt, query_cnt = map(int, input().split())
    memory_settings = [None] + list(map(int, input().split())) + [sys.maxsize]
    avalanche_set = {i: defaultdict(int) for i in range(1, level_cnt + 1)}
    for _ in range(query_cnt):
        query = input().split()
        if query[0] == "I":
            key, weight = map(int, query[1:])
            avalanche_set[1][key] = weight
            for level in range(1, level_cnt):
                if sum(avalanche_set[level].values()) > memory_settings[level]:
                    for key in avalanche_set[level]:
                        avalanche_set[level+1][key] = avalanche_set[level][key]
                    avalanche_set[level].clear()
                else:
                    break

        elif query[0] == "F":
            key = int(query[1])
            is_find = False
            for level in range(1, level_cnt + 1):
                if key in avalanche_set[level]:
                    print(level, avalanche_set[level][key])
                    is_find = True
                    break
            if not is_find:
                print("none")

if __name__ == "__main__":
    main()


"""
4 11
5 11 24
I 2 3
I 1 3
F 2
I 2 2
F 2
I 3 5
I 3 4
F 4
F 2
I 4 20
F 4
"""