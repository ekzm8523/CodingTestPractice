import math

def init_segment_tree(start, end, node):
    """
    :param start: 시작 인덱스
    :param end: 끝 인덱스
    :param node: 구간합 트리의 노드 번호
    :return: 노드 번호를 인덱스로 갖는 구간합
    """
    if start == end:
        tree[node] = l[start]
    else:
        mid = (start + end) // 2
        tree[node] = init_segment_tree(start, mid, node * 2) + init_segment_tree(mid + 1, end, node * 2 + 1)
    return tree[node]


def sum_segment_tree(start, end, node, left, right):
    """
    :param start: 시작 인덱스
    :param end: 끝 인덱스
    :param node: 구간합 트리의 노드 번호
    :param left: 구간합을 찾고자 하는 범위의 왼쪽
    :param right: 구간합을 찾고자 하는 범위의 오른쪽
    :return: out of range -> return 0, 범위 안에 있는경우 -> return tree[node], 섞여있는 경우 -> 나눠서 sum
    """
    if left > end or right < start:
        return 0
    if left <= start and end <= right:
        print(f"sum to {tree[node]}")
        return tree[node]
    mid = (start + end) // 2
    return sum_segment_tree(start, mid, node * 2, left, right) + sum_segment_tree(mid + 1, end, node * 2 + 1, left, right)


def update_segment_tree(start, end, node, index, dif):
    """
    :param start: 시작 인덱스
    :param end: 끝 인덱스
    :param node: 구간합 트리의 노드 번호
    :param index: 바꾸려는 index
    :param dif: 이전 값과의 차이값
    """
    if index < start or index > end:
        return
    tree[node] += dif
    if start == end:
        return
    mid = (start + end) // 2
    update_segment_tree(start, mid, node * 2, index, dif)
    update_segment_tree(mid + 1, end, node * 2 + 1, index, dif)


if __name__ == "__main__":

    l = [1, 9, 3, 8, 4, 5, 5, 9, 10, 3, 4, 5]
    N = len(l)
    h = math.ceil(math.log2(N))
    size = 2 ** (h + 1)
    tree = [-1] * size
    init_segment_tree(0, N-1, 1)
    print(sum_segment_tree(0, N - 1, 1, 4, 8))
    print()