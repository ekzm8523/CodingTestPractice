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
import os

def insert(num):
    global start_leaf
    leaf = start_leaf + num
    while leaf > 0:
        tree[leaf] += 1
        leaf //= 2

def prefix_sum(start, end, node, num):

    if start > num:
        return 0
    if num >= end:
        return tree[node]
    elif num < end:
        mid = (start + end) // 2
        return prefix_sum(start, mid, node * 2, num) + prefix_sum(mid + 1, end, node * 2 + 1, num)


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
        runners[key] = rank + 1
    runners = list(runners.values())

    h = ceil(log2(n)) + 1 # n = 8 일때 h = 4, n = 9일때 h = 5
    tree_size = 2 ** h - 1  # h = 4 일때 size = 15, h = 5일때 size = 31
    tree = [None] + [0] * tree_size    # 인덱스는 1부터 시작
    start_leaf = tree_size - n  # tree[start_leaf + num] -> 실제 num 값이 되도록

    for i, runner in enumerate(runners):
        print("*"*50)
        print(f"insert the {runner}")
        print_tree()
        passable_person = prefix_sum(1, n, 1, runner)
        print(f"현재 등수 : {i + 1}  제낄만 한사람 : {passable_person}")
        # print(f"best rank is {i + 1 - passable_person}")
        # print(i + 1 - passable_person)
        insert(runner)
        print_tree()

