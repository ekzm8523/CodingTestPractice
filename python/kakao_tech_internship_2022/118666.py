# https://school.programmers.co.kr/learn/courses/30/lessons/118666
from collections import defaultdict


def solution(survey, choices):
    answer = []
    score_dict = defaultdict(int)
    for query, choice in zip(survey, choices):
        if choice <= 3:
            score_dict[query[0]] += 4 - choice
        elif choice >= 5:
            score_dict[query[1]] += choice - 4

    characteristic = ["RT", "CF", "JM", "AN"]
    for c in characteristic:
        if score_dict[c[0]] >= score_dict[c[1]]:
            answer.append(c[0])
        else:
            answer.append(c[1])
    return ''.join(answer)


if __name__ == '__main__':
    survey = ["AN", "CF", "MJ", "RT", "NA"]
    choices = [5, 3, 2, 7, 5]
    print(solution(survey, choices))

    survey = ["TR", "RT", "TR"]
    choices = [7, 1, 3]
    print(solution(survey, choices))