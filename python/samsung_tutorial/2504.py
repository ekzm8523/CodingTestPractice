import sys
if __name__ == "__main__":

    s = list(input())

    stack = []

    for ch in s:
        print(stack)
        if ch == '(' or ch == '[':
            stack.append(ch)
        elif ch == ']':
            w = 0
            while stack:
                top = stack.pop()
                if top.isdigit():
                    w += int(top)
                    continue

                if top == '[':
                    stack.append('3' if w == 0 else str(w * 3))
                    break
                else:
                    print(0)
                    sys.exit()
        elif ch == ')':
            w = 0
            while stack:
                top = stack.pop()
                if top.isdigit():
                    w += int(top)
                    continue
                else:
                    if top == '(':
                        stack.append('2' if w == 0 else str(w * 2))
                        break
                    else:
                        print(0)
                        sys.exit()
    answer = 0

    while stack:
        if not stack[-1].isdigit():
            print(0)
            sys.exit()
        answer += int(stack.pop())

    print(answer)