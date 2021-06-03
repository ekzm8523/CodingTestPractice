from queue import PriorityQueue

def solution(t, r):
    answer = []
    print(t,r)

    max_time = max(t)
    min_time = min(t)
    t_id = [] # 도착 시간 : [id]
    i_r = {} # 아이디 : 우선순위
    pq = PriorityQueue()
    for i in range(max_time + 1):
        t_id.append([])
    for i in range(len(t)):
        i_r[i] = r[i]
        t_id[t[i]].append(i)
    print(t_id)
    print(i_r)

    for i in range(max_time + 1):
        if t_id[i]:
            for id in t_id[i]:
                pq.put((i_r[id], id))
        if pq.queue:
            _, id = pq.get()
            answer.append(id)

    return answer

if __name__ == "__main__":
    t = [0, 1, 3, 0]
    r = [0, 1, 2, 3]
    print(solution(t, r))

    t = [7, 6, 8, 1]
    r = [0, 1, 2, 3]
    print(solution(t, r))