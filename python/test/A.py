# from python.test import B_test
from python.test.B import B_test1

def A_fun1():
    print("func1 실행")


def A_fun2():
    print("func2 실행")

def A_fun3():
    print("func3 실행")

def A_test():

    print("test A")
    B_test1()

if __name__ == '__main__':
    A_test()