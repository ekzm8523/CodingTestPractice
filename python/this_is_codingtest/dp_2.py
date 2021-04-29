
n = int(input())
food = list(map(int,input().split()))

d = [0] * n
d[0] = food[0]
size = len(food)
if food[0] < food[1]:
    d[1] = food[1]
else:
    d[1] = food[0]

for i in range(2,size):
    d[i] = max(d[i-1], d[i-2] + food[i])
    
print(d)
