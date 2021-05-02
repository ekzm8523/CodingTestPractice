# https://programmers.co.kr/learn/courses/30/lessons/12899

def solution(n):
    answer = ''
    num = ['1', '2', '4']

    while n > 0:
        n -= 1 # 0을 포함하지 않는 삼진
        answer = num[n % 3] + answer
        n //= 3

    return answer


if __name__ == '__main__':
    print(solution(int(input())))