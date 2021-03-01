
n, k = map(int, input().split())
answer = 0
while(n != 1):
    target = (n // k) * k
    answer += (n - target)
    n = target
    if n < k:
        break
    answer += 1
    n //= k
answer += (n-1)
print(answer)
