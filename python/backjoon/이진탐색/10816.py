# https://www.acmicpc.net/problem/10816
from bisect import bisect_left, bisect_right


if __name__ == "__main__":
    _ = int(input())
    card_list = list(map(int, input().split()))
    card_list.sort()
    _ = int(input())
    find_nums = list(map(int, input().split()))

    answer = []
    for num in find_nums:
        left_idx = bisect_left(card_list, num)
        right_idx = bisect_right(card_list, num)

        # 찾는 값이 list의 최댓값보다 크거나 없는경우
        if left_idx == len(card_list) or card_list[left_idx] != num:
            answer.append(0)
        else:
            answer.append(right_idx - left_idx)
    print(*answer)