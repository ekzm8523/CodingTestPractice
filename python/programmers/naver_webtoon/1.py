from collections import defaultdict


def solution(lottery):
    answer = []
    user_dic = {}
    for user_id, lotto in lottery:
        if not user_id in user_dic:
            user_dic[user_id] = [1, lotto]
        else:
            if user_dic[user_id][1]:  # 이미 당첨 되었다면
                continue
            else:
                user_dic[user_id] = [user_dic[user_id][0] + 1, lotto]


    for user_id in user_dic:
        if user_dic[user_id][1]:
            answer.append(user_dic[user_id][0])

    if answer:
        return sum(answer) // len(answer)
    return 0

if __name__ == "__main__":
    lotto = [[1,0],[35,0],[1,0],[100,1],[35,1],[100,1],[35,0],[1,1],[1,1]]
    print(solution(lotto))
    lotto = [[1,0],[2,0],[3,0],[1,0],[2,0],[1,0],[1,1],[2,0],[2,0],[2,1],[1,0],[1,1],[3,0],[3,0],[1,1]]
    print(solution(lotto))
    lotto = [[1,0],[2,0],[3,0]]
    print(solution(lotto))
