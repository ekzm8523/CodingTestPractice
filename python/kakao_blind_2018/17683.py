# https://programmers.co.kr/learn/courses/30/lessons/17683

def solution(m, musicinfos):
    answer = ''
    return answer


if __name__ == '__main__':
    m = "ABCDEFG"
    musicinfos = ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]
    answer = "HELLO"
    result = solution(m, musicinfos)
    assert answer == result

    m = "CC#BCC#BCC#BCC#B"
    musicinfos = ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]
    answer = "FOO"
    result = solution(m, musicinfos)
    assert answer == result



    m = "ABC"
    musicinfos = ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]
    answer = "WORLD"
    result = solution(m, musicinfos)
    assert answer == result
