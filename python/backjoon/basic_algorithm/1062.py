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
        ontology |= word    # 26개 - 5개의 모든 경우의 수 말고 필요한 단어만 bitmask 하기 위한 변수


    if k < 5:
        print(0)
    else:
        ontology = init_bitmask(ontology, word_list)    # word 들을 bit 로 전부 변경
        size = len(ontology)

        k -= 5  # 'a', 'c', 'i', 't', 'n'은 이미 dictionary 에 포함되었다는 가정
        # size 와 k 중 더 작은 값으로 combination -> 이유는 k가 ontology 보다 훨씬 클때 문제가 생기기 때문이다 -> 51%에서 오류
        # combination의 특성상 뒷 파라미터가 size를 over하면 빈 리스트를 반환한다.
        combs = list(combinations(ontology.values(), min(size, k)))
        answer = 0

        for comb in combs:
            cnt = 0
            comb_bit = sum(comb)    # combination의 bit_mask
            for word in word_list:  # word의 bit_mask
                if comb_bit & word == word: # combination으로 나온 조합으로 word를 만들 수 있다면
                    cnt += 1    # cnt 증가
            answer = max(answer, cnt)

        print(answer)