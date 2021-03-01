n = int(input())
array = list(map(int,input().split()))


array.reverse()
dp = [1] * n

for i in range(1,n):
    for j in range(i):
        if array[j] <= array[i]:
            dp[i] = max(dp[j]+1, dp[i])
print(n - dp[n-1])
