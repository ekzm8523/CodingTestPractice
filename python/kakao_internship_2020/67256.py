"""
1. 엄지손가락은 상하좌우 4가지 방향으로만 이동할 수 있으며 키패드 이동 한 칸은 거리로 1에 해당합니다.
2. 왼쪽 열의 3개의 숫자 1, 4, 7을 입력할 때는 왼손 엄지손가락을 사용합니다.
3. 오른쪽 열의 3개의 숫자 3, 6, 9를 입력할 때는 오른손 엄지손가락을 사용합니다.
4. 가운데 열의 4개의 숫자 2, 5, 8, 0을 입력할 때는 두 엄지손가락의 현재 키패드의 위치에서 더 가까운 엄지손가락을 사용합니다.
4-1. 만약 두 엄지손가락의 거리가 같다면, 오른손잡이는 오른손 엄지손가락, 왼손잡이는 왼손 엄지손가락을 사용합니다.

position 왼쪽위 (0, 0) 부터 오른쪽 아래 (3, 2) 로 약속

"""


def calc_distance(A, B):
    return abs(A[0] - B[0]) + abs(A[1] - B[1])

def right_or_left(l_pos, r_pos, pos, hand):

    l_dis = calc_distance(l_pos, pos)
    r_dis = calc_distance(r_pos, pos)

    if l_dis > r_dis:
        return 'R'
    elif l_dis < r_dis:
        return 'L'
    else:
        if hand[0] == 'l':
            return 'L'
        else:
            return 'R'

def solution(numbers, hand):
    answer = []
    left_set = set((1, 4, 7))
    right_set = set((3, 6, 9))
    l_pos = [3, 0]
    r_pos = [3, 2]
    pos = [-1, -1]

    for number in numbers:
        if number in left_set:
            answer.append('L')
            l_pos[0], l_pos[1] = number // 3, 0
        elif number in right_set:
            answer.append('R')
            r_pos[0], r_pos[1] = (number - 1) // 3, 2
        else:   # 2, 5, 8, 0
            number = number if number != 0 else 10
            pos[0], pos[1] = number // 3, 1
            result = right_or_left(l_pos, r_pos, pos, hand)
            if result == 'L':
                l_pos[0], l_pos[1] = pos[0], pos[1]     # 새로운 배열로 계속 연결해주면 가비지가 너무 많이 남기때문에 할당
            else:
                r_pos[0], r_pos[1] = pos[0], pos[1]
            answer.append(result)

    return ''.join(answer)


if __name__ == '__main__':
    numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
    hand = "right"
    print(solution(numbers, hand))

    numbers = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
    hand = "left"
    print(solution(numbers, hand))

    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    hand = "right"
    print(solution(numbers, hand))