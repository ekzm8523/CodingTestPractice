# https://www.acmicpc.net/problem/1654

if __name__ == "__main__":

    cable_cnt, goal_cnt = map(int, input().split())
    cable_list = [int(input()) for _ in range(cable_cnt)]

    left, right = 1, max(cable_list)
    answer = 1

    while left <= right:
        mid = (left + right) // 2

        cnt = 0
        for cable in cable_list:
            cnt += cable // mid

        if cnt < goal_cnt:  # 갯수가 부족하면
            right = mid - 1  # 길이를 줄여야함
        else:
            left = mid + 1
            answer = mid

    print(answer)


"""
4 11
802
743
457
539

---

200
"""