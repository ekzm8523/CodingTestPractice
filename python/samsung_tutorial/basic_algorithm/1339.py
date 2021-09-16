# https://www.acmicpc.net/problem/1339
"""
점수제도로 9부터 순차적으로 알파벳에 할당해주는 식으로 앓고리즘을 짜면 될듯
자릿수 * 10 만큼 점수를 주고 sort하면 될듯?
"""

from collections import defaultdict
import sys


if __name__ == "__main__":

    score_dic = defaultdict(int)

    n = int(sys.stdin.readline())

    # 단어를 받으면서 동시에 알파벳별 점수를 매겨준다
    word_list = []
    for _ in range(n):
        word = sys.stdin.readline().rstrip()
        word_list.append(word)
        score = 1
        for ch in word[::-1]:
            score_dic[ch] += score
            score *= 10

    score_dic = dict(sorted(score_dic.items(), key=lambda x: x[1], reverse=True))

    # 우리가 매핑해야할 점수로 변환 score가 높은순 부터 9~0
    i = 9
    for key in score_dic:
        score_dic[key] = i
        i -= 1

    answer = 0
    for word in word_list:
        score = 1
        for ch in word[::-1]:
            answer += score_dic[ch] * score
            score *= 10
    print(answer)



