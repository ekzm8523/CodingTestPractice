# https://programmers.co.kr/learn/courses/30/lessons/60058
"""
균형잡힌 괄호 문자열 -> ())(
올바른 괄호 문자열 -> (( ))
1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다.
2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다. 단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며, v는 빈 문자열이 될 수 있습니다.
3. 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행합니다.
  3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환합니다.
4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다.
  4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다.
  4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다.
  4-3. ')'를 다시 붙입니다.
  4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다.
  4-5. 생성된 문자열을 반환합니다.
"""
def check_answer(results, answers):
    for i, (result, answer) in enumerate(zip(results, answers)):
        if result == answer:
            print(f"{i + 1}번 정답")
        else:
            print(f"{'*' * 10} {i + 1}번 오답 {'*' * 10}\n 정답 -> {answer} \n 내꺼 -> {result}")


def check_correct_str(u):
    if not u:
        print("u가 비었어요 확인좀요 !")
        return False
    stack = u[0]
    for i in range(1, len(u)):
        if (stack == "" or stack[-1] == ')') and u[i] == ')':
            return False
        if stack[-1] == '(' and u[i] == ')':
            stack = stack[:-1]
        if u[i] == '(':
            stack += u[i]

    return stack == ""


def magic_box(w):
    if not w:
        return ""
    oppo_dic = {"(": ")", ")": "("}
    u = w[0]
    v = ""
    stack_size = 1
    for i in range(1, len(w)):
        u += w[i]
        if w[0] == w[i]:
            stack_size += 1
        else:
            stack_size -= 1
        if stack_size == 0:
            v = w[i+1:]
            break
    print("u -> " + u)
    print("v -> " + v)
    print(check_correct_str(u))

    if check_correct_str(u):
        v = magic_box(v)
        return u + v
    else:
        new_str = "(" + magic_box(v) + ")"
        if len(u) < 2:
            "u의 사이즈가 너무 작아요 확인해주세요"
            return ""
        u = list(u)
        u = u[1:-1]

        for i, ch in enumerate(u):
            u[i] = oppo_dic[ch]
        new_str += "".join(u)
        u = new_str
    return u


def solution(p):
    if not p:
        return ''
    return magic_box(p)


if __name__ == "__main__":

    result = []
    result.append(solution("(()())()"))
    result.append(solution(")("))
    result.append(solution("()))((()"))

    answer = ["(()())()", "()", "()(())()"]

    check_answer(result, answer)

