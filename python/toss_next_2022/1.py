"""
1 ~ n번까지 n명
각각 숙련도를 가지고 있고 숙련도의 합이 팀의 숙련도
일부 선수들은 이전에 같은 팀에 속함
이 선수들이 모두 팀에 포함되면 팀의 숙련도가 2배 (버프)

연속되는 번호를 가진 선수 K명으로 팀을 구성해야 함
구성할 수 있는 팀 중 숙련도가 가장 높은 팀의 숙련도로 구성
1 <= len(skills) == n <= 500000
    skills[i] is (i + 1) 선수의 숙련도
    1 <= skills[1...i] <= 1000
1 <= len(team) <= n
"""

def solution(skills, team, k):
    """
    prefix sum을 사용? two pointer?
    둘 다 연산량은 비슷할 것 같고 추가 공간복잡도가 필요없는 two pointer가 나을듯
    """
    min_team, max_team = min(team) - 1, max(team) - 1

    weight_sum = answer = sum(skills[:k])
    if 0 <= min_team and max_team <= k - 1:
        answer *= 2
    for i in range(k, len(skills)):
        weight_sum -= skills[i - k]
        weight_sum += skills[i]
        if i - k + 1 <= min_team and max_team <= i:
            answer = max(weight_sum * 2, answer)
        else:
            answer = max(weight_sum, answer)

    return answer


if __name__ == '__main__':
    skills = [3, 2, 4, 1]
    team = [2, 4]
    k = 3
    print(solution(skills, team, k))

    skills = [1, 1, 4, 2, 1, 1]
    team = [2, 1, 5]
    k = 4
    print(solution(skills, team, k))

    skills = [5, 8, 3, 1]
    team = [4, 3]
    k = 2
    print(solution(skills, team, k))

