# https://www.acmicpc.net/problem/2517
"""
h -> 1 leaf -> 1 node -> 1
h -> 2 leaf -> 2 node -> 3
h -> 3 leaf -> 4 node -> 7
h -> 4 leaf -> 8 node -> 15
leaf -> 2 ** (h-1)
h -> log2(leaf) + 1
리프노드 -> n개일때 h -> log_2(n + 1)
node -> 2 ** h - 1
1. 실력으로 정렬후 등수로 변환 -> 경로 압축
2. 등수로 세그먼트 트리를 만든 후 입력하면서 자기보다 큰 노드의 개수 + 1을 출력
"""
import sys
from math import log2, ceil

def insert(num):
    global start_leaf
    leaf = start_leaf + num - 1
    while leaf > 0:
        tree[leaf] += num
        leaf //= 2

def print_tree():
    for i in range(1, h+1):
        for node in range(2 ** (i-1), 2 ** i):
            print(tree[node], end=" ")
        print()

if __name__ == "__main__":

    n = int(sys.stdin.readline())

    runners = {}
    for i in range(n):
        s = int(sys.stdin.readline())
        runners[s] = i

    for rank, key in enumerate(sorted(runners)):
        runners[key] = rank

    # runners = [int(sys.stdin.readline()) for _ in range(n)]
    #
    # sorted_runners = sorted(runners)
    # runner_dic = {}
    # for i, runner in enumerate(runners):
    #     runner_dic[runner] = [None, i]
    # for rank, runner in enumerate(sorted_runners):
    #     runner_dic[runner][0] = rank
    # rank_runners = []
    # for runner in runners:
    #     rank_runners.append(runner_dic[runner][0])
    # print(runners)
    # print(rank_runners)
    # print()
    # sorted_runners = []
    #
    # for i in range(n):
    #     runners.append([None, s])   # [순위, 실력]
    # sorted_runners = sorted(runners, key=lambda x: x[1])
    # print(runners)


    best_runner = max(runners)
    h = ceil(log2(best_runner)) + 1
    tree_size = 2 ** h - 1
    tree = [0] * (tree_size + 1)
    start_leaf = 2 ** (h - 1)

    for runner in runners:
        print(f"insert the {runner}")
        insert(runner)
        print_tree()



    print()

