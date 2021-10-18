"""
https://programmers.co.kr/learn/courses/30/lessons/81301
"""

def solution(s):

    str2int = {"zero": '0', "one": '1', "two": '2', "three": '3', "four": '4',
               "five": '5', "six": '6', "seven": '7', "eight": '8', "nine": '9'}

    for key, value in str2int.items():
        s = s.replace(key, value)

    return s


if __name__ == '__main__':
    s = "one4seveneight"
    print(solution(s))
    s = "23four5six7"
    print(solution(s))
    s = "2three45sixseven"
    print(solution(s))
    s = "123"
    print(solution(s))
