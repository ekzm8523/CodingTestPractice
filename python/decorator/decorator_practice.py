def jw_decorator(func):
    def func_wrapper(*args, **kwargs):
        print("wrapper class")
        return func(*args, **kwargs)
    return func_wrapper

@jw_decorator
def printF(c1, c2, **kwargs):
    print(c1)
    print(c2)
    print(kwargs)
    return 1


if __name__ == "__main__":
    print(printF("hello", "hel", a=1, b=2, e=12))
