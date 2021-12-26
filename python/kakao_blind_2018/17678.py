# https://programmers.co.kr/learn/courses/30/lessons/17678
'''
0 < n <= 20 : 셔틀 운행 횟수
0 < t <= 60 : 셔틀 운행 간격
0 < m <= 45 : 한 셔틀에 탈 수 있는 최대 크루 수
'''

def convert_minute(str_time):
    s, m = str_time.split(':')
    return int(s) * 60 + int(m)


def print_time(m):
    return f"{m // 60:0>2}:{m % 60:0>2}"

def solution(n, t, m, timetable):
    timetable = sorted(list(map(convert_minute, timetable)))
    start = convert_minute("09:00")
    last_shuttle = start + (n - 1) * t

    cnt, last_time = 0, 0
    current_shuttle = start
    flag = True
    for time in timetable:
        while time > current_shuttle or cnt >= m:   # 다음 버스 타야할 때
            if current_shuttle == last_shuttle:  # 이번차가 막차에요
                flag = False
                break
            else:  # 다음차
                current_shuttle += t
                cnt = 0
        if not flag:  # 막차 지나가면 끝
            break
        if time > last_time:  # 마지막으로 탄 시간 기록
            last_time = time
        cnt += 1

    if cnt >= m:  # 마지막차의 인원수가 다 차서 1분 빨리와야할 때
        return print_time(last_time-1)
    else:  # 마지막차 탈 수 있을때
        return print_time(last_shuttle)

if __name__ == '__main__':

    n, t, m = 1, 1, 5
    timetable = ["08:00", "08:01", "08:02", "08:03"]
    print(solution(n, t, m, timetable))
    n, t, m = 2, 10, 2
    timetable =["09:10", "09:09", "08:00"]
    print(solution(n, t, m, timetable))
    n, t, m = 2, 1, 2
    timetable = ["09:00", "09:00", "09:00", "09:00"]
    print(solution(n, t, m, timetable))
    n, t, m = 1, 1, 5
    timetable = ["00:01", "00:01", "00:01", "00:01", "00:01"]
    print(solution(n, t, m, timetable))
    n, t, m = 1, 1, 1
    timetable = ["23:59"]
    print(solution(n, t, m, timetable))
    n, t, m = 10, 60, 45
    timetable = ["23:59","23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"]
    print(solution(n, t, m, timetable))

