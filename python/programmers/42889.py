


def solution(N, stages):

    stages.sort()
    size = len(stages)
    record = [None] + [[0, 0] for _ in range(N)]

    for stage in stages:
        if stage == N + 1:
            continue
        if record[stage][1] == 0:
            record[stage] = [1, size]
        else:
            record[stage][0] += 1
        size -= 1

    for i in range(1, N + 1):
        if record[i][1] == 0:
            record[i] = [0, i]
        else:
            record[i][0] = record[i][0] / record[i][1]
            record[i][1] = i
    record = record[1:]
    record.sort(key=lambda x: (-x[0], x[1]))
    answer = []
    for i in range(N):
        answer.append(record[i][1])
    return answer


if __name__ == "__main__":
    N = 5
    stages = [2, 1, 2, 6, 2, 4, 3, 3]
    print(solution(N, stages))

    N = 4
    stages = [4,4,4,4,4]
    print(solution(N, stages))