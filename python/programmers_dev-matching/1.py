import re

def solution(registered_list, new_id):
    answer = ''

    registered_set = set(registered_list)

    if new_id not in registered_set:
        return new_id

    idx = -1
    for i, s in enumerate(new_id):
        if s.isdigit():
            idx = i
            break

    if idx == -1:
        s, n = new_id, 0
    else:
        s, n = new_id[:idx], int(new_id[idx:])

    while True:
        new_str = s + str(n) if n > 0 else s
        if new_str not in registered_set:
            return new_str
        n += 1



if __name__ == '__main__':
    registered_list = ["card", "ace13", "ace16", "banker", "ace17", "ace14"]
    new_id = "ace15"
    print(solution(registered_list, new_id))

    registered_list = ["cow", "cow1", "cow2", "cow3", "cow4", "cow9", "cow8", "cow7", "cow6", "cow5"]
    new_id = "cow"
    print(solution(registered_list, new_id))

    registered_list = ["bird99", "bird98", "bird101", "gotoxy"]
    new_id = "bird98"
    print(solution(registered_list, new_id))

    registered_list = ["apple1", "orange", "banana3"]
    new_id = "apple"
    print(solution(registered_list, new_id))
