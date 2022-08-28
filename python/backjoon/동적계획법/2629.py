# https://www.acmicpc.net/problem/2629
import sys

input = lambda: sys.stdin.readline().strip()

if __name__ == '__main__':
    balance_count = int(input())
    balance_weights = list(map(int, input().split()))

    marble_count = int(input())
    marble_weights = list(map(int, input().split()))

    enable = set()
    enable.add(0)
    next_buffer = []
    for balance_weight in balance_weights:
        for weight in enable:
            add_weight, sub_weight = weight + balance_weight, abs(weight - balance_weight)
            if add_weight not in enable:
                next_buffer.append(add_weight)
            if sub_weight not in enable:
                next_buffer.append(sub_weight)
        for weight in next_buffer:
            enable.add(weight)
        next_buffer.clear()

    answer = ["Y" if marble_weight in enable else "N" for marble_weight in marble_weights]

    print(' '.join(answer))
