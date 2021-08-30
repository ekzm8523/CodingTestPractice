# https://www.acmicpc.net/problem/2143
"""
B[1] -> 1
B[2] -> 3
B[3] -> 1
B[1] + B[2] -> 4
set -> (1, 4)
1 -> sum(A) == 4 이어야 함
A[1] + A[2]
A[2] + A[3]

4 -> sum(A) == 1 이어야 함
A[1], A[3]

"""
import sys

def find_comb(sequence, size, max_value):
    prefix_seq = [0]
    for i in range(size):
        prefix_seq.append(prefix_seq[i] + sequence[i])
    comb = {}

    # comb = set()
    left = 0
    while left < size:
        for right in range(left + 1, size + 1):
            seq_sum = prefix_seq[right] - prefix_seq[left]
            # if seq_sum < max_value:
            if seq_sum in comb:
                comb[seq_sum] += 1
            else:
                comb[seq_sum] = 1

        left += 1
    return comb
    # while l < n:
    #     if r == l:
    #         r += 1
    #         continue
    #     seq_sum = prefix_seq[r] - prefix_seq[l]
    #     if seq_sum < max_value:
    #         comb.add(seq_sum)
    #         if r == n:
    #             break
    #         r += 1
    #     else:   # 값을 줄여야함
    #         l += 1



def numbers_summation(sequence, size, sum_value):
    prefix_seq = [0]
    for i in range(size):
        prefix_seq.append(prefix_seq[i] + sequence[i])

    l = r = 0
    cnt = 0
    while l < size:
        if l == r:
            r += 1
            continue
        seq_sum = prefix_seq[r] - prefix_seq[l]

        if seq_sum < sum_value:
            if r == size:
                l += 1
            else:
                r += 1
        elif seq_sum > sum_value:
            l += 1
        else:
            cnt += 1
            l += 1

    return cnt
if __name__ == "__main__":

    t = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    A = list(map(int, sys.stdin.readline().split()))
    m = int(sys.stdin.readline())
    B = list(map(int, sys.stdin.readline().split()))

    combination = find_comb(A, n, t)
    answer = 0
    for num, weight in combination.items():

        cnt = numbers_summation(B, m, t - num)
        # print(f"A : find {num}, cnt {weight} \nB : find {t - num}, cnt {cnt}")
        # print(weight * cnt)
        answer += (cnt * weight)

    print(answer)

"""
5
4
1 3 -1 2
3
1 3 2
"""