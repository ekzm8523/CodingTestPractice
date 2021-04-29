# https://www.acmicpc.net/problem/2358
from collections import defaultdict

n = int(input())
l = []

for i in range(n):
    x, y = map(int, input().split())
    l.append((x,y))

size = len(l)
answer = 0

sorted_x = sorted(l, key=lambda x: x[0])
sorted_y = sorted(l, key=lambda x: x[1])

dic_x = defaultdict(int)
dic_y = defaultdict(int)

for (x,y) in sorted_x:
    dic_x[x] += 1
    if dic_x[x] == 2:
        answer += 1
for (x,y) in sorted_y:
    dic_y[y] += 1
    if dic_y[y] == 2:
        answer += 1

print(answer)
