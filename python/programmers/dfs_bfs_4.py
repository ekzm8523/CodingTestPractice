
from collections import defaultdict

def dfs(ticket_dic, depth, key, answer):

    answer.append(key)
    value_list = ticket_dic[key]
    print(value_list)
    for i in range(len(value_list)):
        if value_list[i] != "none":
            key = value_list[i]
            value_list[i] = "none"

    dfs(ticket_dic, depth + 1, key, answer)


def solution(tickets):
    answer = []
    ticket_dic = defaultdict(list)
    print(tickets)
    for k, v in tickets:
        ticket_dic[k].append(v)
    print(ticket_dic)

    for k, v in ticket_dic.items():
        ticket_dic[k] = sorted(v)
    dfs(ticket_dic, tickets[0][0], answer)

    print(ticket_dic)

if __name__ == "__main__":
    tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
    print(solution(tickets))