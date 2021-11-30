##
def in_cache(func):
    cache = {}
    a = 3
    def wrapper(n):
        print(cache)
        if n in cache:
            return cache[n]
        else:
            cache[n] = func(n)
            return cache[n]

    return wrapper

def factorial(n):
    num = 1
    for i in range(1, n+1):
        num *= i
    return num


if __name__ == '__main__':
    f = in_cache(factorial)
    f2 = in_cache(factorial)

    print(f(3))
    print(f2(2))
    print(f(5))
    print(f2(3))
    print(f(10))
    print(f(10))
    print(f(10))
    print(f(11))

