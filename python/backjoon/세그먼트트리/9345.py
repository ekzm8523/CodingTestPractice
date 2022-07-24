# https://www.acmicpc.net/problem/9345
"""
세그먼트트리 + 최댓값 최솟값
n ~ m 선반까지의 최솟값 최댓값을 구했을때
최소는 n이고 최대는 m이어야한다.
만약 아니라면 그 안에 시리즈는 잘못 된 것!
"""
import sys
from math import log2, ceil, inf

input = lambda: sys.stdin.readline().rstrip()


class SegmentTree:

    def __init__(self, node_count):
        self.depth = ceil(log2(node_count))
        self.tree_size = 2 ** (self.depth + 1)
        self.tree = [[inf, -inf] for _ in range(self.tree_size)]
        self._init_tree(1, node_count, 1)
        self.original_array = [i for i in range(node_count + 1)]

    def __len__(self):
        return self.tree_size

    def print_tree(self):
        for depth in range(self.depth+1):
            for i in range(2 ** depth, 2 ** (depth + 1)):
                print(self.tree[i], end=" ")
            print()
        print(f"depth : {self.depth}")

    def _init_tree(self, left, right, idx):
        self.tree[idx][:] = left, right

        if left < right:
            mid = (left + right) // 2
            self._init_tree(left, mid, idx * 2)
            self._init_tree(mid + 1, right, idx * 2 + 1)

    def change_node(self, change_left, change_right):
        self.original_array[change_left], self.original_array[change_right] =\
            self.original_array[change_right], self.original_array[change_left]
        self._change_node(1, len(self.original_array) - 1, change_left, change_right, 1)

    def _change_node(self, left, right, change_left, change_right, idx):

        if not left <= change_left <= right and not left <= change_right <= right:
            return
        if left == right:
            if right == change_left:
                self.tree[idx][0] = self.tree[idx][1] = self.original_array[change_left]
            elif right == change_right:
                self.tree[idx][0] = self.tree[idx][1] = self.original_array[change_right]
            return

        mid = (left + right) // 2
        self._change_node(left, mid, change_left, change_right, idx * 2)
        self._change_node(mid + 1, right, change_left, change_right, idx * 2 + 1)

        self.tree[idx][0] = min(self.tree[idx * 2][0], self.tree[idx * 2 + 1][0])
        self.tree[idx][1] = max(self.tree[idx * 2][1], self.tree[idx * 2 + 1][1])

    def get_min_max(self, left, right, target_left, target_right, idx) -> tuple:
        if target_right < left or target_left > right:
            return inf, -inf
        if target_left <= left and right <= target_right:
            return self.tree[idx][0], self.tree[idx][1]

        mid = (left + right) // 2
        target_left_min, target_left_max = self.get_min_max(left, mid, target_left, target_right, idx * 2)
        target_right_min, target_right_max = self.get_min_max(mid + 1, right, target_left, target_right, idx * 2 + 1)
        return min(target_left_min, target_right_min), max(target_left_max, target_right_max)


if __name__ == '__main__':
    test_case_count = int(input())
    for _ in range(test_case_count):
        dvd_count, event_count = map(int, input().split())
        tree = SegmentTree(dvd_count)
        # tree.print_tree()
        for _ in range(event_count):
            query, a, b = map(int, input().split())
            a, b = a + 1, b + 1
            if query == 0:
                # 진상 손님 진일이가 선반 a와 b의 dvd를 바꿔 끼운다.
                tree.change_node(a, b)
            else:
                # 손님이 선반 a부터 b에 있는 DVD를 카운터에 가져온다.
                target_min, target_max = tree.get_min_max(1, dvd_count, a, b, 1)
                print("YES" if target_min == a and target_max == b else "NO")
