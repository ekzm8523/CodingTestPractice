import sys
input = lambda: sys.stdin.readline().strip()

if __name__ == '__main__':
    n = int(input())
    tree = list(map(int, input().split()))

    cur_idx = tree.index(-1, 1)
    change_num = int(input())
    tree[cur_idx] = change_num
    def is_balance():
        # 균형 맞음, 왼쪽 자식, 오른쪽 자식, 부모 -> 0, 1, 2, 3
        left_child, right_child, parent = cur_idx * 2, cur_idx * 2 + 1, cur_idx // 2
        if 1 <= left_child <= n:
            if tree[left_child] > tree[cur_idx]:
                tree[left_child], tree[cur_idx] = tree[cur_idx], tree[left_child]
                return left_child


        if 1 <= right_child <= n:
            if tree[right_child] < tree[cur_idx]:
                tree[right_child], tree[cur_idx] = tree[cur_idx], tree[right_child]
                return right_child

        if 1 <= parent <= n:
            if cur_idx % 2 == 1:  # 오른쪽 자식
                if tree[parent] < tree[cur_idx]:
                    tree[parent], tree[cur_idx] = tree[cur_idx], tree[parent]
                    return parent

            else:  # 왼쪽 자식
                if tree[parent] > tree[cur_idx]:
                    tree[parent], tree[cur_idx] = tree[cur_idx], tree[parent]
                    return parent
        return cur_idx

    while True:
        result = is_balance()
        print(tree)
        if result == cur_idx:
            break