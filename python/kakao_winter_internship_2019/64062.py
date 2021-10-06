"""
1. 징검다리는 일렬로 놓여 있고 각 징검다리의 디딤돌에는 모두 숫자가 적혀 있으며 디딤돌의 숫자는 한 번 밟을 때마다 1씩 줄어듭니다.
2. 디딤돌의 숫자가 0이 되면 더 이상 밟을 수 없으며 이때는 그 다음 디딤돌로 한번에 여러 칸을 건너 뛸 수 있습니다.
3. 단, 다음으로 밟을 수 있는 디딤돌이 여러 개인 경우 무조건 가장 가까운 디딤돌로만 건너뛸 수 있습니다.

마지막으로 건넌 친구를 찾으면 된다.
how?
이진탐색으로 trevel
"""

def stepping_stone(stones, k, num):

    k_cnt = 0
    for i, stone in enumerate(stones):
        if stone - num < 0:
            k_cnt += 1
        else:
            k_cnt = 0

        if k_cnt == k:
            return False
    return True

def solution(stones, k):
    answer = 0

    left = 0
    right = 2 * int(1e9)
    while left <= right:
        mid = (left + right) // 2
        is_cross = stepping_stone(stones, k, mid)
        if is_cross:
            left = mid + 1
            answer = mid
        else:
            right = mid - 1

    return answer

if __name__ == '__main__':
    stones = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
    k = 3
    print(solution(stones, k))
    result = 3


