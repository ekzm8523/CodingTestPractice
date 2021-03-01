def fac(n):
    if n == 1:
        return 1
    return n * fac(n-1)

print(fac(6))


def GCD(A,B):
    print(A,B)
    if A < B:
        tmp = B
        B = A
        A = tmp
    R = A % B
    if R == 0:
        return B
    
    return GCD(B,R)

print(GCD(192,162))


