# https://programmers.co.kr/learn/courses/30/lessons/72416
import sys
from dataclasses import dataclass, field
from itertools import combinations
from typing import List


@dataclass
class Node:
    sales: int
    dp_include_self: int = field(default=sys.maxsize)
    dp_exclude_self: int = field(default=sys.maxsize)
    children: list = field(default_factory=list)
    parent: int = field(default=-1)


def calculation_sales(idx: int, sales: int, include_set: set, nodes: List[Node]) -> int:
    exclude_set = set(nodes[idx].children) - include_set
    for child in include_set:
        sales += nodes[child].dp_include_self
    for child in exclude_set:
        sales += nodes[child].dp_exclude_self

    return sales


def dfs(idx: int, nodes: List[Node]) -> None:
    # 리프노드인 경우
    if not nodes[idx].children:
        nodes[idx].dp_include_self = nodes[idx].sales
        nodes[idx].dp_exclude_self = 0
        return

    # 자식들 먼저 순회
    for child in nodes[idx].children:
        dfs(child, nodes)

    # leaf node인 child와 internal node인 child를 구별
    children = set(nodes[idx].children)
    leaf_children = set((child for child in children if not nodes[child].children))
    internal_children = children - leaf_children
    internal_child_count = len(internal_children)

    combs = []  # combination
    for i in range(internal_child_count + 1):
        combs += list(combinations(internal_children, i))

    # 자신을 포함하는 경우 (사실 이것도 한줄로 가능..)
    for comb in combs:
        _sales = calculation_sales(idx=idx, sales=nodes[idx].sales, include_set=set(comb), nodes=nodes)
        nodes[idx].dp_include_self = min(nodes[idx].dp_include_self, _sales)

    # 자신을 포함하지 않는 경우
    for comb in combs:
        if not comb:  # 최소 한개 자식은 포함되어 있어야 함
            continue
        _sales = calculation_sales(idx=idx, sales=0, include_set=set(comb), nodes=nodes)
        nodes[idx].dp_exclude_self = min(nodes[idx].dp_exclude_self, _sales)

    # 자신을 포함하지 않는 경우에서의 예외처리 (리프노드 하나만 포함하고 나머지는 포함하지 않는 경우)
    if leaf_children:
        leaf_children_min_sales = min((nodes[child].sales for child in leaf_children))
        _sales = sum(map(lambda child: nodes[child].dp_exclude_self, internal_children)) + leaf_children_min_sales
        nodes[idx].dp_exclude_self = min(nodes[idx].dp_exclude_self, _sales)


def solution(sales, links):
    nodes = [None] + [Node(sales=sale) for sale in sales]  # 구현 편의상 인덱스가 1부터 시작
    for parent, child in links:
        nodes[parent].children.append(child)
        nodes[child].parent = parent

    dfs(1, nodes)

    return min(nodes[1].dp_include_self, nodes[1].dp_exclude_self)


if __name__ == '__main__':
    sales = [14, 17, 15, 18, 19, 14, 13, 16, 28, 17]
    links = [[10, 8], [1, 9], [9, 7], [5, 4], [1, 5], [5, 10], [10, 6], [1, 3], [10, 2]]
    print(solution(sales, links))

    sales = [5, 6, 5, 3, 4]
    links = [[2, 3], [1, 4], [2, 5], [1, 2]]
    print(solution(sales, links))
    sales = [5, 6, 5, 1, 4]
    links = [[2, 3], [1, 4], [2, 5], [1, 2]]
    print(solution(sales, links))
    sales = [10, 10, 1, 1]
    links = [[3, 2], [4, 3], [1, 4]]
    print(solution(sales, links))
