# https://www.acmicpc.net/problem/1541
# -가 있는곳부터 뒤에 모든 +에 괄호를 걸쳐야 최소가 될듯

if __name__ == '__main__':
    input_str = input()
    numbers = []
    expression = []
    buffer = []
    if input_str[0].isnumeric():
        expression.append('+')
    for ch in input_str:
        if ch.isnumeric():
            buffer.append(ch)
        else:
            numbers.append(int(''.join(buffer)))
            buffer.clear()
            expression.append(ch)
    numbers.append(int(''.join(buffer)))
    idx = ''.join(expression).find('-')
    print(sum(numbers) if idx == -1 else sum(numbers[:idx])-sum(numbers[idx:]))






