# 짝지어 제거하기
# https://programmers.co.kr/learn/courses/30/lessons/12973


def solution(s):
    i = 0
    stack = []
    for c in s:
        if stack:
            if stack[-1] == c:
                stack.pop()
            else:
                stack.append(c)
        else:
            stack.append(c)
        print(stack)
    if stack:
        return 0
    return 1



if __name__ == "__main__":
    s = "baabaa"
    print(solution(s))