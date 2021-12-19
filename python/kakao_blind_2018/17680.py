# https://programmers.co.kr/learn/courses/30/lessons/17680
import sys

# ===========================================
# 일반적인 dict를 이용한 구현
# 이 방법이 효율은 더 좋다.
# ===========================================

def solution1(cache_size, cities):
    answer = 0
    cache = {}
    for city in cities:
        city = city.lower()
        if city in cache:
            answer += 1
            cache[city] = answer
        elif len(cache) < cache_size:
            answer += 5
            cache[city] = answer
        else:
            answer += 5
            lru_key, lru_value = None, sys.maxsize
            for k, v in cache.items():
                if v < lru_value:
                    lru_value, lru_key = v, k
            if lru_key:
                cache.pop(lru_key)
                cache[city] = answer

    return answer


# ===========================================
# Closure를 이용한 구현
# ===========================================


def find_lru(cache):
    lru_key, lru_value = None, sys.maxsize
    for k, v in cache.items():
        if v < lru_value:
            lru_value, lru_key = v, k

    return lru_key


def city_cache(func, cache_size):
    cache = {}
    time = 0

    def wrapper(city):
        nonlocal time
        if city in cache:
            cache[city] = time
            time += 1

        else:
            if len(cache) < cache_size:
                cache[city] = time
            else:
                key = func(cache)
                if key:
                    cache.pop(key)
                    cache[city] = time
            time += 5

    return wrapper


def solution2(cache_size, cities):
    closure = city_cache(find_lru, cache_size=cache_size)

    for city in cities:
        closure(city.lower())

    return closure.__closure__[3].cell_contents

if __name__ == '__main__':
    cache_size = 3
    cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]
    print(solution1(cache_size, cities))

    cache_size = 3
    cities = ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]
    print(solution1(cache_size, cities))

    cache_size = 2
    cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]
    print(solution1(cache_size, cities))

    cache_size = 5
    cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]
    print(solution2(cache_size, cities))

    cache_size = 2
    cities = ["Jeju", "Pangyo", "NewYork", "newyork"]
    print(solution2(cache_size, cities))

    cache_size = 0
    cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]
    print(solution2(cache_size, cities))


