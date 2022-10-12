from multiprocessing import Pool
import time
import os


def f(x):
    print('값', x, '에 대한 작업 pid : ', os.getpid())
    time.sleep(1)
    return x * x


if __name__ == '__main__':
    p = Pool(10)
    start_time = int(time.time())

    # for i in range(10):
    #     print(f(i))
    print(f"main process id : {os.getpid()}")
    print(p.map(f, range(10)))

    end_time = int(time.time())
    print(f"총 작업 시간 : {end_time - start_time}")
