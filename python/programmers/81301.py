# https://programmers.co.kr/learn/courses/30/lessons/81301

def solution(s):
    answer = []

    word_dic = {
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }

    l = 0
    r = 1
    size = len(s)
    while True:
        word_cond = s[l:r]
        if word_cond in word_dic.keys():
            answer.append(word_dic[word_cond])
            l = r

        elif word_cond.isdigit():
            answer.append(word_cond)
            l = r

        if r > size:
            print()
            break
        r += 1


    return int("".join(answer))

if __name__ == "__main__":

    s = "one4seveneight"
    print(solution(s))
    s = "23four5six7"
    print(solution(s))
    s = "2three45sixseven"
    print(solution(s))
    s = "123"
    print(solution(s))