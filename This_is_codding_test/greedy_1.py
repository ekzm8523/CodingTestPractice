#
# n, k = map(int, input().split())
# answer = 0
# while(n != 1):
#     target = (n // k) * k
#     answer += (n - target)
#     n = target
#     if n < k:
#         break
#     answer += 1
#     n //= k
# answer += (n-1)
# print(answer)

def fun(a,b,c,n,sum):
    if sum == n:
        answer = 1
    if answer == 1 or sum > n:
        return
    fun(a,b,c,n,sum+a)
    fun(a,b,c,n,sum+b)
    fun(a,b,c,n,sum+c)


a,b,c,n = map(int, input().split())

answer = 0
fun(a,b,c,n,0)

print(answer)
