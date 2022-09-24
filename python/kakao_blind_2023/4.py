import math


def have_children(idx, height, tree):
    if tree[idx - 1] == '1':
        return True
    if height > 0:  # 짝수는 리프가 아님
        idx_weight = 2 ** (height - 1)
        return have_children(idx - idx_weight, height - 1, tree) or have_children(idx + idx_weight, height - 1, tree)
    return False


def search_tree(idx, height, tree):
    if tree[idx - 1] == '0':
        return not have_children(idx, height, tree)
    if height > 0:
        idx_weight = 2 ** (height - 1)
        return search_tree(idx - idx_weight, height - 1, tree) and search_tree(idx + idx_weight, height - 1, tree)
    return True


def solution(numbers):
    answer = []

    for number in numbers:
        binary_str = bin(number).split('b')[1]
        dummy_binary_str = '0' * (2 ** (math.floor(math.log2(len(binary_str))) + 1) - 1 - len(binary_str))
        binary_tree = dummy_binary_str + binary_str
        positive = 0
        height = int(math.log2(len(binary_str)))
        if search_tree(2**height, height, binary_tree):
            positive = 1
        answer.append(positive)
    return answer


if __name__ == '__main__':
    print(solution([7, 5]))
    print(solution([63, 111, 95]))
    print(solution(list(range(1, 100))))
