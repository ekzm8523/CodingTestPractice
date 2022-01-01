def solution(records):
    answer = []
    admin_data = []
    nick_name_info = {}

    for record in records:
        if record[0] == 'E':
            query, user_id, nick_name = record.split()
            nick_name_info[user_id] = nick_name
            admin_data.append((query, user_id))
        elif record[0] == "L":
            admin_data.append(record.split())
        else:
            _, user_id, nick_name = record.split()
            nick_name_info[user_id] = nick_name

    for query, user_id in admin_data:
        if query[0] == "E":
            answer.append(f"{nick_name_info[user_id]}님이 들어왔습니다.")
        else:
            answer.append(f"{nick_name_info[user_id]}님이 나갔습니다.")

    return answer

if __name__ == '__main__':
    record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
    print(solution(record))
