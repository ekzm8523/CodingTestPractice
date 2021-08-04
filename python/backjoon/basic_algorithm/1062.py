import sys
from itertools import combinations

def init_bitmask(ontology, word_list):
    bit_dic = {}
    for i, ch in enumerate(ontology):
        bit_dic[ch] = (1 << i)

    for i, word in enumerate(word_list):
        tmp = 0
        for ch in word:
            tmp += bit_dic[ch]
        word_list[i] = tmp

    return bit_dic




if __name__ == "__main__":

    n, k = map(int, sys.stdin.readline().split())

    word_list = []
    ontology = set()
    for _ in range(n):
        word = set(sys.stdin.readline().strip()[4:-4]).difference('a', 'c', 'i', 't', 'n')
        word_list.append(word)
        ontology |= word



    if k < 5:
        print(0)
    else:
        ontology = init_bitmask(ontology, word_list)

        size = len(ontology)

        k -= 5

        combs = list(combinations(ontology, min(size, k)))
        answer = 0

        for comb in combs:
            cnt = 0
            comb_bit = 0
            for ch in comb:
                comb_bit += ontology[ch]

            for word in word_list:
                if comb_bit & word == word:
                    cnt += 1
            answer = max(answer, cnt)

        print(answer)