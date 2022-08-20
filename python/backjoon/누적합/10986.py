# https://www.acmicpc.net/problem/10986
import sys
from collections import Counter

input = lambda: sys.stdin.readline().strip()

if __name__ == '__main__':
    size, divide_num = map(int, input().split())
    array = list(map(int, input().split()))
    prefix_sum = []
    tmp = 0
    for i in range(size):
        prefix_sum.append((tmp + array[i]) % divide_num)
        tmp = prefix_sum[-1]

    counter = Counter(prefix_sum)
    answer = counter[0]
    counter[prefix_sum[0]] -= 1
    for start_idx in range(1, size):
        answer += counter[prefix_sum[start_idx-1]]
        counter[prefix_sum[start_idx]] -= 1
    print(answer)
