# https://programmers.co.kr/learn/courses/30/lessons/62048
import math


def solution(w,h):
    g = math.gcd(w, h)
    return w * h - (w + h - g)


if __name__ == "__main__":
    w = 8
    h = 12
    print(solution(w, h))

