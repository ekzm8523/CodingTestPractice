# https://www.acmicpc.net/problem/9372
"""
이번 방학 동안의 비행 스케줄이 주어졌을 때, 상근이가 가장 적은 종류의 비행기를 타고 모든 국가들을 여행할 수 있도록 도와주자. -> MST
비행기 -> 간선
"""
import sys

if __name__ == "__main__":
    test = int(input())

    for _ in range(test):
        N, M = map(int, sys.stdin.readline().split())
        edges = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
        print(N-1)





