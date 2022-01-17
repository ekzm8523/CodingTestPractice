# https://www.acmicpc.net/problem/11659
"""
이 문제는 update가 없기 때문에 세그먼트 트리가 더 느리다 그냥 prefix sum을 쓰면 됨
"""
import sys

if __name__ == '__main__':
    number_cnt, query_cnt = map(int, sys.stdin.readline().split())
    numbers = list(map(int, sys.stdin.readline().split()))
    answer = []

    pre_sum = [0]
    for i in range(number_cnt):
        pre_sum.append(pre_sum[i] + numbers[i])

    for _ in range(query_cnt):
        a, b = map(int, sys.stdin.readline().split())
        print(pre_sum[b] - pre_sum[a-1])




