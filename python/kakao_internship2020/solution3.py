# https://programmers.co.kr/learn/courses/30/lessons/67258
from collections import defaultdict

def length(A):
    return A[1]-A[0]

def solution(gems):
    answer = [0, len(gems)-1]
    gem_kind = set(gems)
    l = r = 0
    gem_dic = defaultdict(int)
    gem_dic[gems[0]] = 1

    while 0 <= l < len(gems) and 0 <= r < len(gems):
        print(l, r, gem_dic)
        if len(gem_dic) == len(gem_kind):
            if length(answer) > r - l:
                answer = [l, r]
            else:
                if gem_dic[gems[l]] == 1:
                    del gem_dic[gems[l]]
                else :
                    gem_dic[gems[l]] -= 1
                l += 1
        else:
            r += 1
            if r == len(gems):
                break
            gem_dic[gems[r]] += 1


    return [answer[0]+1, answer[1]+1]

if __name__ == "__main__":

    print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"])) # 3,7
    print(solution(["AA", "AB", "AC", "AA", "AC"]))
    print(solution(["XYZ", "XYZ", "XYZ"]))
    print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))
