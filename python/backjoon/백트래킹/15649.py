# https://www.acmicpc.net/problem/15649
import itertools


if __name__ == "__main__":
    N, M = map(int, input().split())
    N_list = [i for i in range(N)]

    permutation_list = list(itertools.permutations(N_list, M))
    for s in permutation_list:
        for i in range(len(s)):
            print(s[i]+1, end=" ")
        print()
