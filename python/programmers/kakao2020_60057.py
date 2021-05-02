# https://programmers.co.kr/learn/courses/30/lessons/60057


def solution(s):
    length_list = []

    result = ""
    LENGTH = len(s)

    if len(s) == 1:
        return 1
    for cut_size in range(1, LENGTH // 2 + 1) : # 1 ~ 4
        cnt = 1
        temp_str = s[:cut_size]
        for i in range(cut_size, LENGTH, cut_size):
            if temp_str == s[i : i+cut_size]:
                cnt += 1
            else:
                if cnt == 1:
                    cnt = ""
                result += str(cnt) + temp_str
                temp_str = s[i : i+cut_size]
                cnt = 1
        if cnt == 1:
            cnt = ""
        result += str(cnt) + temp_str
        length_list.append(len(result))
        result = ""


    return min(length_list)

if __name__ == "__main__":
    s = "abcabcabcabcdededededede"
    print(solution(s))
"""
"aabbaccc"                  7
"ababcdcdababcdcd"          9
"abcabcdede"                8
"abcabcabcabcdededededede"  14
"xababcdcdababcdcd"	        17
"""
