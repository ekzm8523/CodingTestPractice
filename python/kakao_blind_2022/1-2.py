# https://programmers.co.kr/learn/courses/30/lessons/92334

def solution(id_list, report, k):
    report_count = {user_id: 0 for user_id in id_list}
    deduplication_report = set(report)
    response_count = {user_id: 0 for user_id in id_list}

    for row in deduplication_report:
        reporter, reported_person = row.split()
        report_count[reported_person] += 1

    for row in deduplication_report:
        reporter, reported_person = row.split()
        if report_count[reported_person] >= k:
            response_count[reporter] += 1

    return [response_count[user_id] for user_id in id_list]


if __name__ == '__main__':
    id_list = ["muzi", "frodo", "apeach", "neo"]
    report = ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"]
    k = 2
    print(solution(id_list, report, k))

    id_list = ["con", "ryan"]
    report = ["ryan con", "ryan con", "ryan con", "ryan con"]
    k = 3
    print(solution(id_list, report, k))

