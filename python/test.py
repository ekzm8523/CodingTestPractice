import random
import threading
import time
from collections import ChainMap
def working():
    max([random.random() for i in range(50000000)])

def foo():
    global x

    for i in range(100000000):
        x += 1


def bar():
    global x


    for i in range(100000000):
        x -= 1

if __name__ == '__main__':
    ...
    # start = time.time()
    # working()
    # working()
    # end = time.time()
    # print(f'{end - start}')
    #
    # start = time.time()
    # threads = []
    # for i in range(2):
    #     threads.append(threading.Thread(target=working))
    #     threads[-1].start()
    #
    # for t in threads:
    #     t.join()
    #
    # end = time.time()
    #
    # print(f'{end - start}')

    # multi thread test
    # x = 0  # A shared value
    #
    #
    #
    # t1 = threading.Thread(target=foo)
    # t2 = threading.Thread(target=bar)
    # t1.start()
    # t2.start()
    # t1.join()
    # t2.join()  # Wait for completion
    #
    # print(x)
from collections import deque
