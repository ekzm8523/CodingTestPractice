# https://www.acmicpc.net/problem/1480
"""
냅색문제랑 다른점
냅색은 물건당 weight와 value가 따로 존재했다.
여기는 가치가 같고 최대한 많이 담는게 중요함
이전에 메모이제이션을 해야된다고 했던 것 같은데?
dp[a][b][c]
a (bit)보석을 사용한 상태 (1001 -> 1번째 4번쨰 보석 사용)
b번째 가방 사용중
c만큼의 용량이 남아있을때
담을 수 있는 최대의 보석 개수
"""
import sys

input = lambda: sys.stdin.readline().strip()


def solution(gems, bag_idx, current_capacity):
    if gems >= 1 << gem_cnt or bag_idx >= bag_cnt:
        return 0

    if dp[gems][bag_idx][current_capacity] != 0:
        return dp[gems][bag_idx][current_capacity]

    now_answer = 0

    for i in range(gem_cnt):
        if gems & (1 << i) > 0 or gem_weights[i] > bag_max_weight:
            continue
        if current_capacity >= gem_weights[i]:  # 현재 가방에 넣을 수 있을 때
            now_answer = max(
                now_answer,
                solution(gems | (1 << i), bag_idx, current_capacity - gem_weights[i]) + 1
            )
        else:  # 현재 가방에 못 넣을 때
            now_answer = max(
                now_answer,
                solution(gems, bag_idx + 1, bag_max_weight)
            )

    dp[gems][bag_idx][current_capacity] = now_answer
    return now_answer


if __name__ == '__main__':
    gem_cnt, bag_cnt, bag_max_weight = map(int, input().split())
    gem_weights = list(map(int, input().split()))
    dp = [[[0] * (bag_max_weight + 1) for _ in range(bag_cnt)] for _ in range(1 << gem_cnt)]
    print(solution(0, 0, bag_max_weight))





