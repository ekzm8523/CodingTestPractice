# https://programmers.co.kr/learn/courses/30/lessons/17681
from math import log2

# def int2bit(size, num):
#
#     bits = [' ' for _ in range(size)]
#
#     while num:
#         idx = num & -num
#         bits[int(log2(idx))] = '#'
#         num -= idx
#
#     bits.reverse()
#     return ''.join(bits)



def solution(n, arr1, arr2):
    answer = []

    for row1, row2 in zip(arr1, arr2):
        bit = bin(row1 | row2)[2:].rjust(n, '0')
        bit = bit.replace('1', '#')
        bit = bit.replace('0', ' ')
        answer.append(bit)

    return answer


if __name__ == '__main__':
    n = 5
    arr1 = [9, 20, 28, 18, 11]
    arr2 = [30, 1, 21, 17, 28]
    print(solution(n, arr1, arr2))

    n = 6
    arr1 = [46, 33, 33 ,22, 31, 50]
    arr2 = [27 ,56, 19, 14, 14, 10]
    print(solution(n, arr1, arr2))
