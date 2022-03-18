from typing import List
import math


class SegmentTree:
    def __init__(self, nums: List = None):
        self.depth = math.ceil(math.log2(len(nums))) + 1
        self.start_idx = 2 ** (self.depth - 1) - 1
        self._tree = [0] * (2 ** self.depth)

        for idx, num in enumerate(nums):
            self.insert(idx + 1, num)

    def insert(self, idx, num) -> None:
        current_idx = self.start_idx + idx
        while current_idx > 0:
            self._tree[current_idx] += num
            current_idx //= 2

    def update(self, idx, num) -> None:
        current_idx = self.start_idx + idx
        dif = num - self._tree[current_idx]
        while current_idx > 0:
            self._tree[current_idx] += dif
            current_idx //= 2

    def interval_sum(self, left, right) -> int:
        return self._interval_sum(1, 1, len(self._tree) // 2, left, right)

    def _interval_sum(self, idx, current_left, current_right, left, right) -> int:
        if left > current_right or right < current_left:  # out of idx
            return 0

        if left <= current_left and current_right <= right:  # contain
            return self._tree[idx]

        mid = (current_left + current_right) // 2

        return self._interval_sum(idx * 2, current_left, mid, left, right) +\
               self._interval_sum(idx * 2 + 1, mid + 1, current_right, left, right)


class FenwickTree:

    def __init__(self, nums: List = None):
        self._tree = [0] * (len(nums) + 1)
        self.nums = [0] + nums
        self.size = len(nums)
        for idx, num in enumerate(nums):
            self.insert(idx + 1, num)  # idx는 1부터 시작

    def insert(self, idx, num) -> None:
        while idx <= self.size:
            self._tree[idx] += num
            idx += (idx & -idx)

    def update(self, idx, num) -> None:
        dif = num - self.nums[idx]
        self.nums[idx] = num
        while idx <= self.size:
            self._tree[idx] += dif
            idx += (idx & -idx)

    def interval_sum(self, a, b) -> int:  # a부터 b까지 sum
        return self.sum(b) - self.sum(a - 1)

    def sum(self, idx) -> int:
        sum_ = 0
        while idx > 0:
            sum_ += self._tree[idx]
            idx -= (idx & -idx)
        return sum_
