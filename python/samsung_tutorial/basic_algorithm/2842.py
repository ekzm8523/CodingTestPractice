# https://www.acmicpc.net/problem/2842
import sys
"""
일단 가장 고도차이가 덜나는 곳으로 간다는게 최적의 해를 보장해주지 않는다 -> 그리디 X
"""

if __name__ == "__main__":

    n = int(sys.stdin.readline())

    table = [list(sys.stdin.readline().rstrip()) for _ in range(n)]

    print(table)
