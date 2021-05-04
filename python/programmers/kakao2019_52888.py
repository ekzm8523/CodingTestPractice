# https://programmers.co.kr/learn/courses/30/lessons/42888

def solution(records):
    answer = []

    # 닉네임 변경 1. 채팅방을 나간 후, 새로운 닉네임으로 다시 들어간다.
    # 닉네임 변경 2. 채팅방에서 닉네임을 변경한다.
    # 기존에 대화의 닉네임도 전부 변경된다.

    record_dic = {}
    record_list = []
    for record in records:
        record = record.split()
        query = record[0]
        if query == "Enter":
            record_dic[record[1]] = record[2]
            record_list.append((query, record[1]))
        elif query == "Leave":
            record_list.append((query, record[1]))
        elif query == "Change":
            record_dic[record[1]] = record[2]

    for query, id in record_list:
        if query == "Enter":
            answer.append(f"{record_dic[id]}님이 들어왔습니다.")
        elif query == "Leave":
            answer.append(f"{record_dic[id]}님이 나갔습니다.")

    return answer

if __name__ == "__main__":

    record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
    print(solution(record))