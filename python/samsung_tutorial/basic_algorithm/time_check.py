import time
from collections import defaultdict

if __name__ == "__main__":
    start = time.time()
    A = set()
    for i in range(100000):
        if i in A:
            A.add(i)
        else:
            A.add(i)
    check_point = time.time()
    print(check_point - start)

    for i in range(100000):
        if i in A:
            A.add(i)
        else:
            A.add(i)
    set.intersection()
    set.union()
    print(time.time() - check_point)
    d = {}
    start = time.time()
    for i in range(100000):
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    print(time.time() - start)

    d = defaultdict(int)
    start = time.time()
    for i in range(100000):
        d[i] += 1

    print(time.time() - start)
    #
    # d = {}
    # start = time.time()
    # for i in range(100000):
    #     if i in d.keys():
    #         d[i] += 1
    #     else:
    #         d[i] = 1
    # print(time.time() - start)
    #
    # d = {}  # 허승연
    # start = time.time()
    # for i in range(100000):
    #     try:
    #         d[i] += 1
    #     except KeyError:
    #         d[i] = 1
    # print(time.time() - start)
