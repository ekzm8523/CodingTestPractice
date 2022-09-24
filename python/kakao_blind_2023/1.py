import datetime


def solution(today, terms, privacies):
    answer = []

    term_dict = {}
    for term in terms:
        key, m = term.split()
        term_dict[key] = int(m)
    current_date = datetime.date(*map(int, today.split('.')))
    for i, privacy in enumerate(privacies):
        date, key = privacy.split()
        year, month, day = map(int, date.split('.'))
        month += term_dict[key]
        day -= 1
        if day == 0:
            day = 28
            month -= 1

        if month % 12 == 0:
            year += month // 12 - 1
            month = 12
        elif month > 12:
            year += month // 12
            month %= 12
        if datetime.date(year, month, day) < current_date:
            answer.append(i + 1)

    return answer



if __name__ == '__main__':
    print(solution("2022.05.19", ["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]))
    print(solution("2020.01.01", ["Z 3", "D 5"], ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]))