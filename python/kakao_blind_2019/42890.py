
from itertools import combinations

def solution(relation):
    answer = 0

    # column_size = len(relation[0])
    # row_size = len(relation)
    # material = set(range(column_size))
    # combination_size = 0
    # candidate_key = []
    # while combination_size < column_size:
    #     combination_size += 1
    #
    #     combs = list(map(set, combinations(range(column_size), combination_size)))
    #     print(combs)
    #     for comb in combs:
    #         flag = True
    #         for candidate in candidate_key:
    #             if candidate == candidate & comb:
    #                 flag = False
    #                 break
    #         if flag:
    #             for row in
    #
    #
    #     print(combs)
    #
    #     s = set()
    #     for comb in combs
    #         for row in relation:
    #             for comb


    return answer


if __name__ == '__main__':
    relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]
    print(solution(relation))
