# https://programmers.co.kr/learn/courses/30/lessons/92335
import math
from collections import Counter


def convert(n: int , k: int) -> str:
    converted_num = []
    while n > 0:
        div, mod = divmod(n, k)
        converted_num.append(str(mod))
        n = div
    converted_num.reverse()
    return ''.join(converted_num)


def is_prime_number(num: str) -> bool:
    if num == '' or num == '1':
        return False
    num = int(num)
    for i in range(2, int(math.sqrt(num) + 1)):
        if num % i == 0:
            return False
    return True


def solution(n, k):
    converted_num = convert(n, k)
    candidate_num = converted_num.split('0')
    c = Counter(map(is_prime_number, candidate_num))
    return c[True]


if __name__ == '__main__':
    n, k = 437674, 3
    print(solution(n, k))
    n, k = 110011, 10
    print(solution(n, k))