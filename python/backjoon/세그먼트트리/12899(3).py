import sys
import math

MAX = 2_000_001


class SegmentTree:
    def __init__(self):
        self.depth = math.ceil(math.log2(MAX)) + 1  # if 7 -> 2.xx -> 3 -> 4
        self._tree = [0] * (2 ** self.depth)  # if depth : 4 -> 16
        self.start_idx = 2 ** (self.depth - 1) - 1  # if depth : 4 -> 8 -> 7

    def add(self, num) -> None:
        idx = self.start_idx + num
        while idx > 0:
            self._tree[idx] += 1
            idx //= 2

    def delete(self, idx) -> int:
        """
        왼쪽노드 확인 -> 현재 idx보다 작거나 같으면 왼쪽이동
        위에 경우 아니면 -> 오른쪽 이동하면서 idx 왼쪽 노드값만큼 감소
        """
        node = 1

        while node <= self.start_idx:
            if self._tree[node * 2] >= idx:
                node *= 2
            else:
                idx -= self._tree[node * 2]
                node = node * 2 + 1

        num = node - self.start_idx
        while node > 0:
            self._tree[node] -= 1
            node //= 2
        return num

if __name__ == "__main__":
    query_cnt = int(sys.stdin.readline())
    tree = SegmentTree()
    for _ in range(query_cnt):
        query, num = map(int, sys.stdin.readline().split())
        if query == 1:
            tree.add(num)
        elif query == 2:
            print(tree.delete(num))


