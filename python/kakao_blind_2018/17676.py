"""
two pointer 문제인듯
모든 로그의 처리시작, 처리완료 구간을 나눈다음
처리시작부터 1초, 처리완료시간까지 1초 이런식으로 슬라이딩 윈도우로 가면 될듯?
"""
from datetime import datetime, timedelta

def preprocess_second(s):
    if s[-1] == "s":
        s = s[:-1]
    s = f"{float(s):0.3f}"
    if s.find(".") != -1:
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

    return sorted(new_lines, key=lambda x: x[1])


def solution(lines):
    """
    start end 둘다 넣고 set는 indexing만 넣어서 start event
    """

    # init setting
    ptr = 0
    lines = preprocessing(lines)  # index dictionary 처럼 쓸것임
    traffic_set = set()
    cur_start = datetime(2016, 9, 15, 0, 0, 0, 0)
    cur_end = datetime(2016, 9, 15, 0, 0, 0, 999999)

    event_queue = set()
    for i, (start, end) in enumerate(lines):
        if cur_start <= start <= cur_end:
            traffic_set.add(i)

        if end <= cur_end:
            traffic_set.add(i)
            continue


        if cur_start > start:
            event_queue.add((start, 0))
        event_queue.add((start, 1))
    event_queue = sorted(event_queue, key=lambda x: x[0])
    print(event_queue)

    for start, end in lines:
        print(start, end)

    return "*"*50

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