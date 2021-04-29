
n = int(input())
list = list(map(int,input().split()))
list.sort()


cnt = 0
answer = 0
for i in list:
    cnt +=1
    if cnt >= i:
        cnt = 0
        answer+=1

print(answer)
