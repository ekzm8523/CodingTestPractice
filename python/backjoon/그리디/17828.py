# https://www.acmicpc.net/problem/17828

"""
A -> 1 , Z -> 26
HONGIK -> 8 + 15 + 14 + 7 + 9 + 11 = 64
길이가 N인 문자열 & value sum -> X
길이가 N이고 value sum이 X인 문자열들 중에 가장 사전 순으로 앞서는 문자열을 출력
존재하지 않으면 ! 출력
문자 중복 상관 없
"""
import sys

if __name__ == "__main__":

    N, X = map(int, sys.stdin.readline().split())

    if X < N or N * 26 < X:
        print("!")
    else:
        answer = ['A'] * N
        X -= N
        idx = N - 1
        while 26 < X:
            answer[idx] = 'Z'
            idx -= 1
            X -= 25
        answer[idx] = chr(X + 65)
        print(''.join(answer))
