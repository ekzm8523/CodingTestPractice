"""
https://programmers.co.kr/learn/courses/30/lessons/17677
자카드 유사도 : 두 집합의 교집합 크기를 두 집합의 합집합 크기로 나눈 값

*** Counter와 정규표현식을 잘 썼으면 더 간결한 코드가 나왔을 것 같다 ***
"""
from collections import defaultdict

COMPLEMENT = 65536


def convert_dict(word):
    dic = defaultdict(int)
    for i in range(len(word)-1):
        key = word[i:i+2]
        if key.isalpha():
            key = key.lower()
            dic[key] += 1
    return dic


def find_intersection(dic1, dic2):
    intersection_dic = {}
    for key in dic1:
        if key in dic2:
            value = min(dic1[key], dic2[key])
            intersection_dic[key] = value
    return intersection_dic


def find_union(dic1, dic2):
    union_dic = dic1.copy()
    for key in dic2:
        if key in union_dic:
            union_dic[key] = max(union_dic[key], dic2[key])
        else:
            union_dic[key] = dic2[key]
    return union_dic


def solution(str1, str2):

    dic1 = convert_dict(str1)
    dic2 = convert_dict(str2)

    intersection = find_intersection(dic1, dic2)
    union = find_union(dic1, dic2)

    A = sum(intersection.values())
    B = sum(union.values())
    if A == 0 and B == 0:
        return COMPLEMENT
    else:
        return int(sum(intersection.values()) * COMPLEMENT / sum(union.values()))


if __name__ == '__main__':
    str1 = "FRANCE"
    str2 = "french"
    print(solution(str1, str2))

    str1 = "handshake"
    str2 = "shake hands"
    print(solution(str1, str2))

    str1 = "aa1+aa2"
    str2 = "AAAA12"
    print(solution(str1, str2))

    str1 = "E=M*C^2"
    str2 = "e=m*c^2"
    print(solution(str1, str2))

