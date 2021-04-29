
n, money = map(int,input().split())

coin_list = []
for i in range(n):
    coin_list.append(int(input()))

d = [10001] * (money+1)


d[0] = 0

for i in range(n):
    for j in range(coin_list[i], money+1):
        if d[j - coin_list[i]] != 10001:
            d[j] = min(d[j], d[j - coin_list[i]] + 1)

print(d)





