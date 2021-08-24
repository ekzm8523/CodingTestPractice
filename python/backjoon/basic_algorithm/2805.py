# https://www.acmicpc.net/problem/2805

def cutting_tree(h):
    get_tree = 0

    for tree in trees:
        if tree <= h:
            break
        get_tree += (tree - h)

    return get_tree


if __name__ == "__main__":

    n, m = map(int, input().split())
    trees = sorted(list(map(int, input().split())), reverse=True)

    bottom = 0
    top = trees[0]
    answer = 0
    while bottom <= top:
        h = (bottom + top) // 2
        get_tree = cutting_tree(h)
        if get_tree < m:    # 높이가 너무 높다면 (잘린 나무가 부족하다면) 높이를 낮춰 더 자르자
            top = h - 1
        elif get_tree >= m:  # 높이가 너무 낮다면 (잘린 나무가 많다면) 높이를 높여 덜 자르자
            answer = h
            bottom = h + 1
        # else:   # 딱 맞으면 그대로 가져가기
        #     answer = h
        #     break
    print(answer)


