# https://www.acmicpc.net/problem/4195
import sys
input = lambda: sys.stdin.readline().strip()


def find(parents: list, idx: int):
    if parents[idx] != idx:
        parents[idx] = find(parents, parents[idx])
    return parents[idx]


def union(parents: list, counter: list, idx1: int, idx2: int):
    p1, p2 = find(parents, idx1), find(parents, idx2)
    cnt1, cnt2 = counter[p1], counter[p2]
    if p1 < p2:
        parents[p2] = p1
        counter[p1] = cnt1 + cnt2
        counter[p2] = 0
        # if p1 != idx1:
        #     counter[idx1] = 0
    elif p1 > p2:
        parents[p1] = p2
        counter[p2] = cnt1 + cnt2
        counter[p1] = 0
    return min(p1, p2)


if __name__ == '__main__':
    test_size = int(input())
    for _ in range(test_size):
        edge_size = int(input())
        friend_dict = {}
        parents = []
        counter = []

        for _ in range(edge_size):
            person1, person2 = input().split()
            idx1 = friend_dict.get(person1)
            if idx1 is None:  # 새로운 친구
                idx1 = len(parents)
                friend_dict[person1] = idx1
                parents.append(idx1)
                counter.append(1)

            idx2 = friend_dict.get(person2)
            if idx2 is None:
                idx2 = len(parents)
                friend_dict[person2] = idx2
                parents.append(idx2)
                counter.append(1)
            group_idx = union(parents, counter, idx1, idx2)

            print(counter[group_idx])