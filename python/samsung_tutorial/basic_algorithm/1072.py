# https://www.acmicpc.net/problem/1072
"""
게임 횟수 : X
이긴 게임 : Y
Z = int(Y / X * 100)
"""
import sys

def solution1():
    """
    바꾸고 변하는지 확인하는 알고리즘
    일단 X가 10억까지 있기 때문에 for문이 10억번까지도 돌 수 있어서 안된다.
    그리고 탈출조건도 없음 지금
    """
    init_z = int(y / x * 100)
    if init_z >= 99:
        return INF
    answer = 0
    while True:
        answer += 1
        next_z = int((y + answer) / (x + answer) * 100)
        if next_z != init_z:
            break
    print(answer)


def solution2(x, y):
    """
    확률이 바뀌는 다음을 계산하는 식이 필요할 듯 하다.
    나눗셈을 하고난 소수점을 버리지 않고 그 소수점이 1까지 향하려면 얼마나 더해줘야할까를 생각해보자
    이분탐색
    소수점 계산법은 X가 바뀔때마다 바뀐다.
    그러면 이분탐색으로 최적의 해를 찾아주자
    """
    top = INF
    bottom = 0
    # 여기가 중요하다 나누고 소숫점에 100을 곱해주는건 위험한 행위라고 한다. 확률을 원한다면 int에 100을 곱해주자!!
    # 확률의 오류이다. 29 / 50 -> 0.58 이지만 거기에 * 100을 하면 57.99999..가 나온다.
    init_rate = int(y * 100 / x)
    answer = INF
    while bottom <= top:
        mid = (bottom + top) // 2
        comp_rate = int((y + mid) * 100 / (x + mid))
        if comp_rate == init_rate:
            bottom = mid + 1
        else:
            top = mid - 1
            answer = min(answer, mid)
    return answer


if __name__ == "__main__":
    INF = int(1e10)
    x, y = map(int, sys.stdin.readline().split())
    answer = solution2(x, y)
    print(-1 if answer == INF else answer)
