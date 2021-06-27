# https://www.acmicpc.net/problem/14888
import sys

def dfs(num, idx, add, sub, multi, div):
    global n, min_num, max_num, num_list

    if idx == n:
        max_num = max(num, max_num)
        min_num = min(num, min_num)
        return

    if add:
        dfs(num + num_list[idx], idx + 1, add - 1, sub, multi, div)
    if sub:
        dfs(num - num_list[idx], idx + 1, add, sub - 1, multi, div)
    if multi:
        dfs(num * num_list[idx], idx + 1, add, sub, multi - 1, div)
    if div:
        dfs(int(num / num_list[idx]), idx + 1, add, sub, multi, div - 1)





if __name__ == "__main__":
    n = int(input())
    num_list = list(map(int, input().split()))
    oper_list = list(map(int, input().split()))
    min_num = sys.maxsize
    max_num = -sys.maxsize
    dfs(num_list[0], 1, *oper_list)

    print(max_num)
    print(min_num)