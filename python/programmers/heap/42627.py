# # https://programmers.co.kr/learn/courses/30/lessons/42627?language=python3

from heapq import heappop as pop, heappush as push


def solution(jobs):

    idx, current_time, taken_time = 0, 0, 0

    jobs.sort(key=lambda x: (x[0], x[1]))
    for job in jobs:
        job.reverse()

    hq = []
    size = len(jobs)
    while hq or idx < size:
        if idx < size:
            if current_time >= jobs[idx][1]:
                push(hq, jobs[idx])
                idx += 1
                continue
            elif not hq:
                push(hq, jobs[idx])
                current_time = jobs[idx][1]
                idx += 1
                continue
        processing_time, req_in_time = pop(hq)
        current_time += processing_time
        taken_time += current_time - req_in_time
    return taken_time // size


if __name__ == "__main__":
    jobs = [[0, 3], [1, 9], [2, 6]]
    print(solution(jobs))
    jobs = [[24, 10], [28, 39], [43, 20], [37, 5], [47, 22], [20, 47], [15, 34], [15, 2], [35, 43], [26, 1]]
    print(solution(jobs))
    jobs = [[24, 10], [28, 39], [43, 20], [37, 5], [47, 22], [20, 47], [15, 2], [15, 34], [35, 43], [26, 1]]
    print(solution(jobs))
    jobs = [[0, 3], [1, 9], [2, 6]]
    print(solution(jobs))
    jobs = [[0, 10], [2, 10], [9, 10], [15, 2]]
    print(solution(jobs))
    jobs = [[0, 10], [2, 12], [9, 19], [15, 17]]
    print(solution(jobs))
    jobs = [[0, 1]]
    print(solution(jobs))
    jobs = [[1000, 1000]]
    print(solution(jobs))
    jobs = [[0, 1], [0, 1], [0, 1]]
    print(solution(jobs))
    jobs = [[0, 3], [1, 9], [2, 6], [30, 3]]
    print(solution(jobs))
    jobs = [[0, 10], [4, 10], [15, 2], [5, 11]]
    print(solution(jobs))
    jobs = [[10, 10], [30, 10], [50, 2], [51, 2]]
    print(solution(jobs))
    jobs = [[1, 9], [1, 4], [1, 5], [1, 7], [1, 3]]
    print(solution(jobs))
