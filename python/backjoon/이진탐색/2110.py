# https://www.acmicpc.net/problem/2110

def is_settable(house_positions, router_cnt, interval_standard) -> bool:

    interval = 0
    for i in range(len(house_positions) - 1):
        interval += house_positions[i + 1] - house_positions[i]
        if interval >= interval_standard:
            interval = 0
            router_cnt -= 1
        if router_cnt == 1:  # 맨 앞에 하나 두고 시작하기 때문에 1개만 남으면 성공임
            return True
    return False




if __name__ == "__main__":
    house_cnt, router_cnt = map(int, input().split())
    house_positions = [int(input()) for _ in range(house_cnt)]
    house_positions.sort()

    left, right = 1, max(house_positions) // (router_cnt - 1)
    answer = 1
    while left <= right:
        mid = (left + right) // 2

        if is_settable(house_positions, router_cnt, mid):
            left = mid + 1
            answer = mid
        else:
            right = mid - 1
    print(answer)


"""
5 3
1
2
8
4
9
"""