
def in_cache(func):
    cache = {}

    def wrapper(n):
        print(cache)
        if n not in cache:
            cache[n] = func(n)
        return cache[n]

    return wrapper


def factorial(n):
    ret = 1
    for i in range(1, n+1):
        ret *= i
    return ret


if __name__ == '__main__':
    cache_factorial = in_cache(factorial)
    print(cache_factorial(5))
    print(cache_factorial(5))
    print(cache_factorial(10))
    print(cache_factorial(10))
