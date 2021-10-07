"""
 연산자의 우선순위를 새로 정의할 때, 같은 순위의 연산자는 없어야 합니다.
 계산된 결과가 음수라면 해당 숫자의 절댓값으로 변환
"""
import re
from itertools import permutations

def calculate_expression(pr_op, operator, numbers):

    stack = [numbers[0]]

    for op, num in zip(operator, numbers[1:]):
        if op == pr_op:
            num = str(eval(stack.pop() + op + num))
        else:
            stack.append(op)
        stack.append(num)

    return stack[::2], stack[1::2]

def solution(expression):
    answer = []

    operators = re.findall(r'[\D]', expression)
    numbers = re.split(r'[-,+,*]', expression)

    for priority in permutations('-+*'):
        copy_numbers = numbers.copy()
        copy_operators = operators.copy()
        for pr_op in priority:
            copy_numbers, copy_operators = calculate_expression(pr_op, copy_operators, copy_numbers)
        answer.append(abs(int(copy_numbers[0])))

    return max(answer)


if __name__ == '__main__':
    expression = "100-200*300-500+20"
    print(solution(expression))

    expression = "50*6-3*2"
    print(solution(expression))