# https://www.acmicpc.net/problem/1786

"""
n > m
n: word T의 길이
m: word P의 길이

"""

def get_pi(p):
    m = len(p)
    j = 0
    pi = [0] * m
    for i in range(1, m):
        while j > 0 and p[i] != p[j]:
            j = pi[j-1]  # 가속점프
        if p[i] == p[j]:
            j += 1
            pi[i] = j
    return pi


def kmp(t, p):
    answer_list = []
    pi = get_pi(p)

    n = len(t)
    m = len(p)
    j = 0
    for i in range(n):
        while j > 0 and t[i] != p[j]:
            j = pi[j-1]
        if t[i] == p[j]:
            if j == (m - 1):
                answer_list.append(i - m + 1)
                j = pi[j]
            else:
                j += 1
    return answer_list

if __name__ == "__main__":
    T = input()
    P = input()

    answer_list = kmp(T, P)
    print(len(answer_list))

    for answer in answer_list:
        print(answer+1, end=" ")