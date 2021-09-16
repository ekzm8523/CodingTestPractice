"""
input : ["muzi", "frodo", "apeach", "neo"], ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"], 2
output : [2, 1, 1, 0]
"""

def solution(id_list, report, k):
    answer = [0] * len(id_list)
    report_dic = {}
    report_cnt_dic = {}

    for info in report:
        _from, _to = info.split()
        if _to in report_dic.keys():
            if _from in report_dic[_to]:
                continue
            report_dic[_to].append(_from)
            report_cnt_dic[_to] += 1
        else:
            report_dic[_to] = [_from]
            report_cnt_dic[_to] = 1

    id_order_dic = {}
    for i, id in enumerate(id_list):
        id_order_dic[id] = i

    for id in id_list:
        if id not in report_cnt_dic.keys():
            continue
        if report_cnt_dic[id] >= k:
            for _from in report_dic[id]:
                answer[id_order_dic[_from]] += 1
    return answer

if __name__ == "__main__":
    id_list, report, k = 	["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3

    print(solution(id_list, report, k))