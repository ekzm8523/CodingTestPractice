"""
사원마다 소속된 팀 번호 있음
팀마다 최소 한명 출근
팀원 모두 재택이면 사원번호 가장 빠른사람이 출근
1. 재택근무 대상자를 모두 구한다
2. 그중 전원 재택인 팀을 찾는다.
3. 전원 재택인 팀중 사원번호 가장 빠른사람을 뺀다.


"""
from heapq import heappush as push, heappop as pop


def solution(num_teams, remote_tasks, office_tasks, employees):
    answer = []
    remote_tasks = set(remote_tasks)
    team_employees = {i + 1: [] for i in range(num_teams)}
    remote_employees = {i + 1: [] for i in range(num_teams)}
    for employee_number, row in enumerate(employees):
        employee_number += 1
        row = row.split()
        team_number, tasks = int(row[0]), set(row[1:])
        if tasks.issubset(remote_tasks):
            remote_employees[team_number].append(employee_number)
        team_employees[team_number].append(employee_number)

    answer = []
    for team_number in team_employees:
        if len(remote_employees[team_number]) == len(team_employees[team_number]):
            if len(remote_employees[team_number]) > 1:
                answer.extend(remote_employees[team_number][1:])
        else:
            answer.extend(remote_employees[team_number])
    return sorted(answer)


if __name__ == '__main__':
    num_teams = 3
    remote_tasks = ["development", "marketing", "hometask"]
    office_tasks = ["recruitment", "education", "officetask"]
    employees = ["1 development hometask", "1 recruitment marketing", "2 hometask", "2 development marketing hometask", "3 marketing", "3 officetask", "3 development"]
    print(solution(num_teams, remote_tasks, office_tasks, employees))

    num_teams = 2
    remote_tasks = ["design"]
    office_tasks = ["building", "supervise"]
    employees = ["2 design", "1 supervise building design", "1 design", "2 design"]
    print(solution(num_teams, remote_tasks, office_tasks, employees))
