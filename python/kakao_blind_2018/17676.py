"""
two pointer 문제인듯
모든 로그의 처리시작, 처리완료 구간을 나눈다음
처리시작부터 1초, 처리완료시간까지 1초 이런식으로 슬라이딩 윈도우로 가면 될듯?
"""
from datetime import datetime, timedelta


def preprocess_second(s):
    if s[-1] == "s":    # 처리시간은 s가 붙어있으므로 제거
        s = s[:-1]
    s = f"{float(s):0.3f}"
    if s.find(".") != -1:   # .이 있을수도 있고 없을수도 있음
        s, ms = map(int, s.split("."))
    else:
        s, ms = int(s), 0

    return int(s), int(ms) * 1000


def preprocess_time(t):
    h, m, s = t.split(":")
    h = int(h)
    m = int(m)
    s, ms = preprocess_second(s)
    return h, m, s, ms


def preprocessing(lines):
    new_lines = []
    for line in lines:
        day, end_time, process_time = line.split()
        year, month, day = map(int, day.split('-'))
        t, m, s, ms = preprocess_time(end_time)
        end = datetime(year, month, day, t, m, s, ms)

        p_s, p_ms = preprocess_second(process_time)
        p_ms -= 1000  # 시작시간을 포함하기 때문에 처리시간에서 0.001초 빼주기
        process_time = timedelta(seconds=p_s, microseconds=p_ms)
        start = end - process_time

        new_lines.append((start, end))

    return new_lines    # 어차피 종료시간으로 정렬되어 있음


def solution(lines):
    lines = preprocessing(lines)
    second_td = timedelta(0, 0, 999000)
    max_cnt = 0
    for i in range(len(lines)):
        cnt = 0
        for j in range(i, len(lines)):
            if lines[i][1] + second_td >= lines[j][0]:
                cnt += 1
        max_cnt = max(cnt, max_cnt)

    return max_cnt

if __name__ == '__main__':
    lines = [
        "2016-09-15 03:10:33.020 0.011s",
        "2016-09-15 00:00:01.000 2s"
    ]
    print(solution(lines))
    lines = [
        "2016-09-15 01:00:04.002 2.0s",
        "2016-09-15 01:00:07.000 2s"
    ]
    print(solution(lines))
    lines = [
            "2016-09-15 20:59:57.421 0.351s",
            "2016-09-15 20:59:58.233 1.181s",
            "2016-09-15 20:59:58.299 0.8s",
            "2016-09-15 20:59:58.688 1.041s",
            "2016-09-15 20:59:59.591 1.412s",
            "2016-09-15 21:00:00.464 1.466s",
            "2016-09-15 21:00:00.741 1.581s",
            "2016-09-15 21:00:00.748 2.31s",
            "2016-09-15 21:00:00.966 0.381s",
            "2016-09-15 21:00:02.066 2.62s"
            ]

    print(solution(lines))