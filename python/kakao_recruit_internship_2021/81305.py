# https://programmers.co.kr/learn/courses/30/lessons/81305
import sys
from itertools import combinations
import copy

def calculate_traffic(start, links, num):
    traffic = 0
    nodes = [start]

    while nodes:
        node = nodes.pop()
        traffic += num[node]
        if links[node][0] != -1:
            nodes.append(links[node][0])
        if links[node][1] != -1:
            nodes.append(links[node][1])
    # print(f"start {start} node traffic is {traffic}")
    return traffic

def solution(k, num, links):

    edges = []
    for i, link in enumerate(links):
        if link[0] != -1:
            edges.append((i, link[0]))

        if link[1] != -1:
            edges.append((i, link[1]))

    combs = combinations(edges, k-1)    # remove combination
    answer = sys.maxsize
    all_traffic = sum(num)

    for i, comb in enumerate(combs):
        copy_links = copy.deepcopy(links)
        # print("*" * 50)
        # print(i, " ", comb)
        start_list = []
        for parent, child in comb:
            start_list.append(child)
            if copy_links[parent][0] == child:
                copy_links[parent][0] = -1
            elif copy_links[parent][1] == child:
                copy_links[parent][1] = -1
            else:
                assert "check remove link"

        # print(links)
        # print(copy_links)

        max_traffic = 0
        remain_traffic = all_traffic
        for start in start_list:
            traffic = calculate_traffic(start, copy_links, num)
            remain_traffic -= traffic
            max_traffic = max(max_traffic, traffic)
            if max_traffic >= answer:
                break
        max_traffic = max(max_traffic, remain_traffic)
        answer = min(max_traffic, answer)
        del copy_links

    return answer


if __name__ == '__main__':
    k = 3
    num = [12, 30, 1, 8, 8, 6, 20, 7, 5, 10, 4, 1]
    links = [[-1, -1], [-1, -1], [-1, -1], [-1, -1], [8, 5], [2, 10], [3, 0], [6, 1], [11, -1], [7, 4], [-1, -1], [-1, -1]]
    print(solution(k, num, links))

    k = 1
    num = [6, 9, 7, 5]
    links = [[-1, -1], [-1, -1], [-1, 0], [2, 1]]
    print(solution(k, num, links))

    k = 2
    num = [6, 9, 7, 5]
    links = [[-1, -1], [-1, -1], [-1, 0], [2, 1]]
    print(solution(k, num, links))

    k = 4
    num = [6, 9, 7, 5]
    links = [[-1, -1], [-1, -1], [-1, 0], [2, 1]]
    print(solution(k, num, links))