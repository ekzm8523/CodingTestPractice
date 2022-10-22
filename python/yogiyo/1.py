# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(stack1, stack2, stack3):
    # write your code in Python 3.8.10
    memory = [stack1, stack2, stack3]
    answer = []
    while stack1 or stack2 or stack3:
        for pc, stack in enumerate(memory):
            if stack:
                break

        max_pc = start_pc = pc
        register = memory[start_pc][-1]
        for pc in range(start_pc, 3):
            if memory[pc] and register < memory[pc][-1]:
                max_pc = pc
        memory[max_pc].pop()
        answer.append(str(max_pc + 1))
    return ''.join(answer)


if __name__ == '__main__':
    print(solution([2, 7], [4, 5], [1]))
    print(solution([10, 20, 30], [8], [1]))
    print(solution([7], [], [9]))