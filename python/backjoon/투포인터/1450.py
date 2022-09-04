'''
https://www.acmicpc.net/problem/1450
중간에서 만나기라는 알고리즘을 사용해야함
문제를 절반으로 나눠 생각해 시간복잡도를 줄이는 방법
'''

import sys
from collections import defaultdict
from itertools import combinations

input = lambda: sys.stdin.readline().strip()

if __name__ == '__main__':

    item_count, weight_limit = map(int, input().split())
    item_weights = list(map(int, input().split()))

    left_weight_dict, right_weight_dict = defaultdict(int), defaultdict(int)
    left_weight_dict[0] = right_weight_dict[0] = 1

    left_item_weights, right_item_weights = item_weights[:item_count // 2], item_weights[item_count // 2:]

    for combination_size in range(1, len(left_item_weights) + 1):
        for combination in combinations(left_item_weights, combination_size):
            weight_sum = sum(combination)
            if weight_sum <= weight_limit:
                left_weight_dict[weight_sum] += 1

    for combination_size in range(1, len(right_item_weights) + 1):
        for combination in combinations(right_item_weights, combination_size):
            weight_sum = sum(combination)
            if weight_sum <= weight_limit:
                right_weight_dict[weight_sum] += 1

    sorted_keys = sorted(left_weight_dict)
    prefix_sum = [0]
    for key in sorted_keys:
        prefix_sum.append(prefix_sum[-1] + left_weight_dict[key])
    answer = 0
    # binary search
    for right_key in right_weight_dict.keys():
        start, end = 0, len(sorted_keys) - 1
        target = weight_limit - right_key
        search_key = None
        while start <= end:
            mid = (start + end) // 2
            if sorted_keys[mid] < target:
                search_key = mid
                start = mid + 1
            elif sorted_keys[mid] > target:
                end = mid - 1
            else:
                search_key = mid
                break
        if search_key is not None:  # while문 조건으로 탈출한게 아니라면
            answer += (right_weight_dict[right_key] * prefix_sum[search_key + 1])
    print(answer)
