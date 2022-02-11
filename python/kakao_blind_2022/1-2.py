# https://programmers.co.kr/learn/courses/30/lessons/92334

def solution(id_list, report, k):
    report_set = {user_id: set() for user_id in id_list}

    for row in report:
        reporter, reported_person = row.split()
        report_set[reporter].add(reported_person)

    reported_count = {user_id: 0 for user_id in id_list}
    for reporter, reported_persons in report_set.items():
        for person in reported_persons:
            reported_count[person] += 1

    for person in reported_count:
        reported_count[person] = reported_count[person] >= k

    answer = []

    for user_id in id_list:
        cnt = 0
        for person in report_set[user_id]:
            if reported_count[person]:
                cnt += 1
        answer.append(cnt)

    return answer


if __name__ == '__main__':
    id_list = ["muzi", "frodo", "apeach", "neo"]
    report = ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"]
    k = 2
    print(solution(id_list, report, k))

    id_list = ["con", "ryan"]
    report = ["ryan con", "ryan con", "ryan con", "ryan con"]
    k = 3
    print(solution(id_list, report, k))

