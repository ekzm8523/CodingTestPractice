
_input = input()
len = len(_input)
answer = 0
for i in range(len):
    if answer + int(_input[i]) < answer * int(_input[i]):
        answer *= int(_input[i])
    else:
        answer += int(_input[i])

print(answer)
