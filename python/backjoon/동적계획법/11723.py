# https://www.acmicpc.net/problem/11723
import sys
def add(bit, num):
    return bit | (1 << (num - 1))

def remove(bit, num):
    return bit - (1 << (num-1))

def check(bit, num):
    return bit & (1 << (num - 1))

def all():
    return (1 << 20) - 1

def empty():
    return 0

if __name__ == "__main__":
    M = int(sys.stdin.readline())
    bit_mask = 0
    for i in range(M):

        query = sys.stdin.readline().strip()
        if query[-1].isdigit():
            query, num = query.split()
            num = int(num)
        # print(f"before : {bit_mask}")
        if query == "add":
            bit_mask = add(bit_mask, num)
        elif query == "remove":
            if check(bit_mask, num):
                bit_mask = remove(bit_mask, num)
        elif query == "check":
            if check(bit_mask, num):
                print("1")
            else:
                print("0")
        elif query == "toggle":
            if check(bit_mask, num):
                bit_mask = remove(bit_mask, num)
            else:
                bit_mask = add(bit_mask, num)
        elif query == "all":
            bit_mask = all()
        elif query == "empty":
            bit_mask = empty()
        # print(f"after : {bit_mask}")

