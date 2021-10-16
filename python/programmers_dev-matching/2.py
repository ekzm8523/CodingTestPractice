def solution(leave, day, holidays):
    week_dic = {"MON": 1, "TUE": 2, "WED": 3, "THU": 4, "FRI": 5, "SAT": 6, "SUN": 7}
    for k in week_dic:
        if k == day:
            continue
        week_dic[k] = week_dic[k] - week_dic[day] + 1
        if week_dic[k] <= 0:
            week_dic[k] += 7
    week_dic[day] = 1
    # print(week_dic)

    red_day = set(holidays)
    for i in range(5):
        sat = week_dic["SAT"] + 7 * i
        sun = week_dic["SUN"] + 7 * i
        if sat <= 30:
            red_day.add(sat)
        if sun <= 30:
            red_day.add(sun)
    # print(red_day)

    # start two pointer

    left, right = 1, 1
    if 1 not in red_day:
        leave -= 1

    answer = tmp = 1
    while True:
        if right == 30:
            break

        if right + 1 in red_day:
            right += 1
            tmp += 1
        elif leave > 0:
            right += 1
            leave -= 1
            tmp += 1
        else:
            if left not in red_day:
                leave += 1
            tmp -= 1
            left += 1
        answer = max(answer, tmp)
        # print(left, right, leave, answer, tmp)
    return answer



if __name__ == '__main__':
    # leave = 4
    # day = "FRI"
    # holidays = [6, 21, 23, 27, 28]
    # print(solution(leave, day, holidays))

    leave = 1
    day = "MON"
    holidays = []
    print(solution(leave, day, holidays))

    # leave = 30
    # day = "MON"
    # holidays = [1, 2, 3, 4, 28, 29, 30]
    # print(solution(leave, day, holidays))

