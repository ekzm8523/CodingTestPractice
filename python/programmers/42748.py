# https://programmers.co.kr/learn/courses/30/lessons/42748?language=python3

def check_answer(results, answers):
    for i, (result, answer) in enumerate(zip(results, answers)):
        if result == answer:
            print(f"{i + 1}번 정답")
        else:
            print(f"{'*' * 10} {i + 1}번 오답 {'*' * 10}\n 정답 -> {answer} \n 내꺼 -> {result}")


def solution(array, commands):
    answer = []

    for command in commands:
        l, r, idx = command
        answer.append(sorted(array[l-1:r])[idx-1])
    return answer


if __name__ == "__main__":
    array = [1, 5, 2, 6, 3, 7, 4]
    commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

    answers = [[5, 6, 3]]
    results = []
    results.append(solution(array, commands))
    check_answer(results, answers)
