import time
from collections import defaultdict

if __name__ == "__main__":
    # 1. in
    # 2. defaultdict
    # 3. keys()
    # 4. try catch
    d = {}  # 이주오
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

    d = {}
    start = time.time()
    for i in range(100000):
        if i in d.keys():
            d[i] += 1
        else:
            d[i] = 1
    print(time.time() - start)

    d = {}  # 허승연
    start = time.time()
    for i in range(100000):
        try:
            d[i] += 1
        except KeyError:
            d[i] = 1
    print(time.time() - start)
