
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


if __name__ == "__main__":
    s = "()[]{}"
    s2 = "([)]"

    print(solution(s))
    print(solution(s2))



if __name__ == "__main__":
    N = 311
    answer = True

    obj = N // 2 + 1
    for i in range(2, obj):
        if N % i == 0:
            answer = False
            break

    print(answer)