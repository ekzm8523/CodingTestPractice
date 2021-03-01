"""
# 하향식
# 상향식
# DP의 조건
# 1. 최적 부분 구조 : 큰 문제를 작은 문제로 나눌 수 있다.
# 2. 중복되는 부분 문제 : 동일한 작은 문제를 반복적으로 해결한다.
"""

"""
# top down DP
d = [0] * 100

def fibo(x):
    if x == 1 or x == 2:
        return 1
    if d[x] != 0:
        return d[x]

    d[x] = fibo(x-1) + fibo(x-2)
    return d[x]

print(fibo(99))

"""
'''
# bottom up DP
d = [0] * 100

d[1] = d[2] = 1
n = 99
for i in range(3, n+1):
    d[i] = d[i-1] + d[i-2]

print(d[n])

'''
