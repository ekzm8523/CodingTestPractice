# https://programmers.co.kr/learn/courses/30/lessons/60057

def check_answer(results, answers):
    for i, (result, answer) in enumerate(zip(results, answers)):
        if result == answer:
            print(f"{i + 1}번 정답")
        else:
            print(f"{'*' * 10} {i + 1}번 오답 {'*' * 10}\n 정답 -> {answer} \n 내꺼 -> {result}")

def solution(s):
    """
    :param s: 압축할 문자열 
    :return: 압축한 문자열중 가장 짧은 길이
    """
    length_list = []
    result = ""

    if len(s) == 1:
        return 1

    for cut_size in range(1, len(s) // 2 + 1):
        cnt = 1
        tmp_str = s[: cut_size]
        for i in range(cut_size, len(s), cut_size):
            if tmp_str == s[i:i + cut_size]:
                cnt += 1
            else:
                if cnt == 1:
                    cnt = ""
                result += str(cnt) + tmp_str
                tmp_str = s[i:i + cut_size]
                cnt = 1
        if cnt == 1:
            cnt = ""
        result += str(cnt) + tmp_str
        length_list.append(len(result))
        result = ""


    return min(length_list)


if __name__ == "__main__":
    result = []
    result.append(solution("aabbaccc"))
    result.append(solution("ababcdcdababcdcd"))
    result.append(solution("abcabcdede"))
    result.append(solution("abcabcabcabcdededededede"))
    result.append(solution("xababcdcdababcdcd"))
    answer = [7, 9, 8, 14, 17]

    check_answer(result, answer)



