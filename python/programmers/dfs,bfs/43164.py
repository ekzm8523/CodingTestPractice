# https://programmers.co.kr/learn/courses/30/lessons/43164

def solution(tickets):
    answer = []
    tickets.sort(key=lambda x: (x[0], x[1]))
    ticket_size = len(tickets)
    visit = [False] * ticket_size
    is_finish = False

    def dfs(current_airport, depth):
        nonlocal answer, is_finish
        if is_finish:
            return
        answer.append(current_airport)
        if depth == ticket_size:
            is_finish = True
            return

        for i, ticket in enumerate(tickets):
            if ticket[0] == current_airport and not visit[i]:
                visit[i] = True
                dfs(ticket[1], depth + 1)
                visit[i] = False
        if not is_finish:
            answer.pop()
    dfs("ICN", 0)
    return answer


if __name__ == '__main__':
    tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
    print(solution(tickets))

    tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]
    print(solution(tickets))
