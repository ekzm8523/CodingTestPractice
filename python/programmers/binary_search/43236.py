# https://programmers.co.kr/learn/courses/30/lessons/43236


def solution(distance, rocks, n):
    answer = 0

    left, right = 1, distance
    rocks.sort()
    while left <= right:
        remove_standard = (left + right) // 2
        current_pos = 0
        remove_cnt = 0
        min_dis = distance
        for rock_pos in rocks:
            dis = rock_pos - current_pos
            if dis <= remove_standard:
                remove_cnt += 1
            else:
                current_pos = rock_pos
                min_dis = min(min_dis, dis)

        dis = distance - current_pos
        if dis <= remove_standard:  # 마지막 위치에서 도착지점까지 거리 재는거 잊지 말기
            remove_cnt += 1

        if remove_cnt > n:  # 너무 많이 치웠을 때
            right = remove_standard - 1
        else:  # 덜 치웠으니 치우는 기준을 조금 높여도 되겠다!
            left = remove_standard + 1
            answer = min_dis

    return answer


if __name__ == "__main__":
    distance = 25
    rocks = [2, 14, 11, 21, 17]
    n = 2

    print(solution(distance, rocks, n))

