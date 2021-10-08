"""
two pointer?
left = right = 0에서 시작해서 하나씩 dic에 넣는다.
1. dic size 가 goal size보다 작으면 right 하나씩 늘려줌
2. goal size에 다달으면 left를 하나씩 증가해주면서 사이즈를 줄여본다.
다시 dic size가 goal size보다 작으면 1번 2번 반복
"""
from collections import defaultdict


def solution(gems):

    goal_size = len(set(gems))  # 담아야하는 보석 종류의 갯수
    gem_size = len(gems)    # 보석의 개수

    answer = [1, gem_size]  # 최악의 상황

    # initialize
    gem_dic = defaultdict(int)
    gem_dic[gems[0]] = 1
    l = r = 0

    while True:
        n = len(gem_dic.keys())     # 보석 종류 갯수
        if n < goal_size:   # 보석종류가 부족하면
            if r == gem_size - 1:   # 더이상 오른쪽으로 갈 수 없다면 break
                break
            r += 1; gem_dic[gems[r]] += 1      # 조금 더 담아보기

        else:   # 보석종류는 충분하다 사이즈를 줄여보자
            if answer[1] - answer[0] > r - l:   # answer update
                answer[0], answer[1] = l + 1, r + 1

            gem_dic[gems[l]] -= 1   # left 움직이기 전에 빼주고 움직이기
            if gem_dic[gems[l]] == 0:   # 만약 0개라면 갯수 헷갈리지 않도록 지워주기
                del gem_dic[gems[l]]
            l += 1

    return answer

if __name__ == '__main__':
    gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
    print(solution(gems))

    gems = ["AA", "AB", "AC", "AA", "AC"]
    print(solution(gems))

    gems = ["XYZ", "XYZ", "XYZ"]
    print(solution(gems))

    gems = ["ZZZ", "YYY", "NNNN", "YYY", "BBB"]
    print(solution(gems))