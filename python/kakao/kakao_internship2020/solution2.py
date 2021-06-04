# https://programmers.co.kr/learn/courses/30/lessons/62048
import itertools
import re

def solution(expression):
    answer = 0
    expressions = set(re.findall("\D", expression))
    prior = itertools.permutations(expressions)
    cand = []

    for op in prior:
        temp = re.compile("(\D)").split(expression)
        for exp in op:
            while exp in temp:
                idx = temp.index(exp)
                temp = temp[:idx-1] + [str(eval(''.join(temp[idx-1:idx+2])))] + temp[idx+2:]

        cand.append(abs(int(temp[0])))


    return max(cand)

if __name__ == "__main__":
    expression = "100-200*300-500+20"
    print(solution(expression) == 60420)
