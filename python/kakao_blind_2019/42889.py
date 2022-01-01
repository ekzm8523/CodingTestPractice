
"""
https://programmers.co.kr/learn/courses/30/lessons/42889
실패율 : 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수
efficient : 22번 케이스 기준
8856.57 ms -> 22.27ms로 대폭 하향
"""
from collections import Counter


def solution(N, stages):
    # test 22: 통과 (8856.57ms, 18.3MB)
    answer = {key: [0, 0] for key in range(1, N+1)}
    for stage in stages:
        if stage == N+1:
            for i in range(1, N+1):
                answer[i][1] += 1
            continue
        for i in range(1, stage+1):
            answer[i][1] += 1
        answer[i][0] += 1
    for i in range(1, N+1):
        answer[i] = answer[i][0] / answer[i][1] if answer[i][1] else 0

    answer = [key for key, _ in sorted(answer.items(), key=lambda x: (-x[1], x[0]))]
    return answer


def efficient_solution(N, stages):
    # test 22: 통과 (22.27ms, 18.4MB)
    counter = Counter(stages)
    visits = [0 for _ in range(N+1)]
    for key, value in counter.items():
        if key == N+1:
            for i in range(1, N+1):
                visits[i] += value
            continue
        for i in range(1, key+1):
            visits[i] += value

    fail_rates = []
    for i in range(1, N+1):
        stay = counter.get(i)
        fail_rates.append(stay / visits[i] if stay else 0)

    return [i+1 for i, _ in sorted(enumerate(fail_rates), key=lambda x: (-x[1], x[0]))]


if __name__ == '__main__':
    n = 5
    stages = [2, 1, 2, 6, 2, 4, 3, 3]
    print(efficient_solution(n, stages))

    n = 4
    stages = [4,4,4,4,4]
    print(efficient_solution(n, stages))
