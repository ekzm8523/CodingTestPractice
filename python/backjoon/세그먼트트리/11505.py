# https://www.acmicpc.net/problem/11505
import sys
from typing import List
import math

DIVISION_BASE = 1000000007


# class FenwickTree:
#
#     def __init__(self, nums: List = None):
#         self.nums = nums
#         self.size = len(nums)
#         self._tree = [1] * (self.size + 1)
#
#         for idx, num in enumerate(nums):
#             self.insert(idx + 1, num)
#
#     def insert(self, idx, num):
#         while idx <= self.size:
#             self._tree[idx] = (self._tree[idx] * num) % DIVISION_BASE
#             idx += (idx & -idx)
#
#     def update(self, idx, num):
#         pre_num = self.nums[idx - 1]
#         if pre_num == 0:  # 기존 num이 0일때
#             if num == 0:  # 다음도 0이면 pass
#                 return
#             # 원상복구 해야함 0된거
#             self.nums[idx - 1] = num
#             while idx <= self.size:
#                 interval_size = (idx & -idx)
#                 self._tree[idx] = (self.interval_product(idx - interval_size + 1, idx - 1) * self.nums[idx - 1]) % DIVISION_BASE
#                 idx += (idx & -idx)
#         else:
#             self.nums[idx - 1] = num
#
#             while idx <= self.size:
#                 self._tree[idx] = (self._tree[idx] // pre_num * num) % DIVISION_BASE
#                 idx += (idx & -idx)
#
#     def interval_product(self, a, b) -> int:
#         if a == b:
#             return self.nums[a-1]
#         left_prefix_product = self.prefix_product(a-1)
#         right_prefix_product = self.prefix_product(b)
#         if left_prefix_product == 0:
#             return 0
#         return right_prefix_product // left_prefix_product
#
#     def prefix_product(self, idx) -> int:
#         result = 1
#         while idx > 0:
#             result = (result * self._tree[idx]) % DIVISION_BASE
#             idx -= (idx & -idx)
#         return result

class SegmentTree:

    def __init__(self, nums: List = None):
        self.depth = math.ceil(math.log2(len(nums))) + 1
        self.start_idx = 2 ** (self.depth - 1) - 1
        self._tree = [1] * (2 ** self.depth)
        self.size = (2 ** self.depth)

        if nums:
            for idx, num in enumerate(nums):
                self.insert(idx + 1, num)

    def insert(self, idx, num):
        idx = self.start_idx + idx
        while idx > 0:
            self._tree[idx] = (self._tree[idx] * num) % DIVISION_BASE
            idx //= 2

    def update(self, idx, num):
        idx = self.start_idx + idx
        pre_num = self._tree[idx]
        if pre_num == 0:
            if num == 0:
                return
            self._tree[idx] = num
            while idx > 1:
                if idx % 2 == 0:
                    self._tree[idx // 2] = (self._tree[idx + 1] * self._tree[idx]) % DIVISION_BASE
                else:
                    self._tree[idx // 2] = (self._tree[idx - 1] * self._tree[idx]) % DIVISION_BASE
                idx //= 2
        else:
            while idx > 0:

                self._tree[idx] = (self._tree[idx] // pre_num * num) % DIVISION_BASE
                idx //= 2



    def interval_product(self, left_idx, right_idx) -> int:
        return self._interval_product(1, 1, self.size // 2, left_idx, right_idx)


    def _interval_product(self, node, current_left_idx, current_right_idx, left_idx, right_idx) -> int:
        if current_left_idx > right_idx or current_right_idx < left_idx:  # out of idx
            return 1

        if left_idx <= current_left_idx <= current_right_idx <= right_idx:
            return self._tree[node]

        mid = (current_left_idx + current_right_idx) // 2
        left_product = self._interval_product(node * 2, current_left_idx, mid, left_idx, right_idx)
        right_product = self._interval_product(node * 2 + 1, mid + 1, current_right_idx, left_idx, right_idx)
        return (left_product * right_product) % DIVISION_BASE



if __name__ == "__main__":
    num_cnt, update_cnt, interval_product = map(int, sys.stdin.readline().split())

    nums = [int(sys.stdin.readline()) for _ in range(num_cnt)]
    tree = SegmentTree(nums)
    for _ in range(update_cnt + interval_product):
        query, a, b = map(int, sys.stdin.readline().split())

        if query == 1:
            tree.update(a, b)

        elif query == 2:
            print(tree.interval_product(a, b))


"""
4 2 1
1
3
4
5
1 1 2
2 1 3
2 1 4
"""