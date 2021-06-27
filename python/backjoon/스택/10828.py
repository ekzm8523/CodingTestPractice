# https://www.acmicpc.net/problem/10828

import sys

if __name__ == "__main__":
    N = int(input())
    stack = []

    for i in range(N):
        # command = list(input().split())
        command = sys.stdin.readline().split()
        if command[0] == "push":
            stack.append(command[1])
        elif command[0] == "pop":
            if stack:
                print(stack.pop())
            else:
                print(-1)
        elif command[0] == "size":
            print(len(stack))
        elif command[0] == "empty":
            if stack:
                print(0)
            else:
                print(1)
        elif command[0] == "top":
            if stack:
                print(stack[-1])
            else:
                print(-1)
