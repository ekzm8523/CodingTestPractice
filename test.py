
def solution(s):
    stack = []

    for ch in s:
        if ch == "(" or ch == "{" or ch == "[":
            stack.append(ch)
        else:
            obj = stack.pop()
            if obj == "(":
                obj = ")"
            else:
                obj = chr(ord(obj) + 2)
            if obj != ch:
                return False
    return True


import threading


def foo():
    global x
    for i in range(1000000):
        x += 1
def bar():
    global x
    for i in range(1000000):
        x -= 1

if __name__ == '__main__':

    x = 0  # A shared value
    t1 = threading.Thread(target=foo)
    t2 = threading.Thread(target=bar)
    t1.start()
    t2.start()
    t1.join()
    t2.join() # Wait for completion

