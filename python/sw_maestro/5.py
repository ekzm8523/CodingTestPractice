"""
5번 문제 - 삼분값
[문제]
처음에 두 개의 수 a,b가 주어진다.
N번 새로운 수 3개가 추가된다.
3개의 수가 추가될 때마다 삼분값을 출력한다.
 - 삼분값(2개): 전체 개수의 1/3번째, 2/3번째로 큰 값.
 - 전체 개수는 항상 3*k+2이다

처음 수열에 속한 수 -10000<=a,b <=10000 (정수)
3개가 추가되는 횟수 1<=N<=100000
N줄에 걸쳐서 주어지는 3개의 정수 -10000<=x,y,z<=10000

"""

import sys
import math


class SegmentTree:
    """
    - 10000부터 시작
    - 리프노드갯수 20001개

    """
    def __init__(self):
        self.depth = math.ceil(math.log2(20001)) + 1
        self._tree = [0] * (2 ** self.depth)
        self.start_idx = 2 ** (self.depth - 1) + 10000  # -10000부터 시작하기 때문에

    def insert(self, nums: tuple):
        for num in nums:
            idx = self.start_idx + num
            while idx > 0:
                self._tree[idx] += 1
                idx //= 2

    def print(self, k):
        left_div_idx = self.find(k + 1)
        right_div_idx = self.find((k + 1) * 2)
        print(left_div_idx, right_div_idx)

    def find(self, rank):
        idx = 1
        # # 왼쪽 자식이 가진 count가 sorted_idx보다 크거나 같으면 왼쪽으로 이동 작으면 rank 빼주고 오른쪽으로 이동
        while idx < self.start_idx - 10000:
            if self._tree[idx * 2] >= rank:  # 왼쪽으로 이동
                idx *= 2
            else:
                rank -= self._tree[idx * 2]
                idx = idx * 2 + 1
        return idx - self.start_idx



if __name__ == "__main__":

    a, b = map(int, sys.stdin.readline().split())
    query_cnt = int(sys.stdin.readline())
    tree = SegmentTree()
    tree.insert((a, b))
    nums = [a, b]
    for k in range(1, query_cnt + 1):
        a, b, c = map(int, sys.stdin.readline().split())
        tree.insert((a, b, c))
        tree.print(k)
        nums.extend((a, b, c))
        nums.sort()
        print(nums[k+1], nums[k+2])