from python.backjoon.세그먼트트리.tree import SegmentTree, FenwickTree


if __name__ == "__main__":
    num_cnt, change_cnt, interval_cnt = map(int, input().split())

    nums = [int(input()) for _ in range(num_cnt)]
    segment_tree = SegmentTree(nums)
    fenwick_tree = FenwickTree(nums)
    for _ in range(change_cnt + interval_cnt):
        query, a, b = map(int, input().split())
        if query == 1:
            segment_tree.update(a, b)
            fenwick_tree.update(a, b)
        elif query == 2:
            print(segment_tree.interval_sum(a, b))
            print(fenwick_tree.interval_sum(a, b))
