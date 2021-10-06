"""
시간복잡도 상관없는 문제
1. 불량 사용자를 키값으로 갖고 그거랑 매칭되는 value 로 dict를 만든다
2. product 라는 내장 카르테지안 프로덕트를 구하는 메서드를 사용해 모든 경우의수를 구한다.
( 대신 중복제거가 되지 않기 때문에 중복제거는 다음과 같은 순서를 거친다.
- 1. cand 내에 중복된 값이 있는지 확인 -> set으로 변환했을때 크기 변화가 있으면 중복값 존재
- 2. 기존에 있던 후보군들과 중복조합인지 확인하기 위해 sort를 하면 list로 변환이 되고 다시 튜플로 변환해서 set에 추가해준다.
"""

from itertools import product

def matching_check(id, ban_id):

    if len(id) != len(ban_id):
        return False

    for a, b in zip(id, ban_id):
        if b != "*" and a != b:
            return False

    return True

def solution(user_id, banned_id):
    ban_dic = {}
    for ban_id in banned_id:
        if ban_id in ban_dic:
            continue
        ban_dic[ban_id] = []
        for id in user_id:
            if matching_check(id, ban_id):
                ban_dic[ban_id].append(id)

    items = []
    for ban_id in banned_id:
        items.append(ban_dic[ban_id])

    answer = set()
    ban_size = len(banned_id)
    for cand in product(*items):

        cand = set(cand)
        if len(cand) == ban_size:
            answer.add(tuple(sorted(cand)))
            print(answer)
    return len(answer)

if __name__ == "__main__":

    user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
    banned_id = ["fr*d*", "abc1**"]
    print(solution(user_id, banned_id))

    user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
    banned_id = ["*rodo", "*rodo", "******"]
    print(solution(user_id, banned_id))

    user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
    banned_id = ["fr*d*", "*rodo", "******", "******"]
    print(solution(user_id, banned_id))
