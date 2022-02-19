# https://programmers.co.kr/learn/courses/30/lessons/92343
from collections import deque


def bfs(graph, info, start_node, final_node) -> set:

    q = deque()
    q.append((start_node, []))
    visit = set()
    visit.add(start_node)
    while q:
        current_node, current_path = q.popleft()
        for next_node in graph[current_node]:
            if next_node not in visit:
                if next_node == final_node:
                    current_path.append(current_node)
                    q.clear()
                    break
                q.append((next_node, current_path + [current_node]))
                visit.add(next_node)

    wolf_set = set((animal for animal in current_path if info[animal] == 1))
    return wolf_set

def solution(info, edges):
    size = len(info)
    wolf_set = [i for i, animal in enumerate(info) if animal]
    sheep_set = [i for i, animal in enumerate(info) if animal == 0]

    graph = [[] for _ in range(size)]
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)

    load_map = [[] for _ in range(size)]
    for sheep in sheep_set:
        for next_sheep in sheep_set:
            if sheep != next_sheep:
                path_wolf_set = bfs(graph, info, sheep, next_sheep)
                load_map[sheep].append((next_sheep, path_wolf_set))

    answer = 1
    current_sheep_set = set()
    current_wolf_set = set()
    current_sheep_set.add(0)
    for i in range(len(sheep_set)):
        next_node, additional_wolf_set = -1, set(wolf_set) - current_wolf_set
        remain_size = len(current_sheep_set) - len(current_wolf_set) - 1
        flag = False
        for candidate_sheep in current_sheep_set:
            if flag:
                break
            for next_sheep, next_wolf_set in load_map[candidate_sheep]:
                if next_sheep not in current_sheep_set:
                    compare_additional_wolf_set = next_wolf_set - current_wolf_set
                    if not compare_additional_wolf_set:
                        additional_wolf_set = compare_additional_wolf_set
                        next_node = next_sheep
                        flag = True
                        break
                    if len(compare_additional_wolf_set) < len(additional_wolf_set) and\
                            len(compare_additional_wolf_set) <= remain_size:
                        additional_wolf_set = compare_additional_wolf_set
                        next_node = next_sheep
        if next_node == -1:
            break
        answer += 1
        current_sheep_set.add(next_node)
        current_wolf_set |= additional_wolf_set

    return answer


if __name__ == '__main__':
    # input_info = [0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1]
    # input_edges = [[0, 1], [1, 2], [1, 4], [0, 8], [8, 7], [9, 10], [9, 11], [4, 3], [6, 5], [4, 6], [8, 9]]
    # print(solution(input_info, input_edges))

    input_info = [0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0]
    input_edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 8], [6, 9], [9, 10]]
    print(solution(input_info, input_edges))
