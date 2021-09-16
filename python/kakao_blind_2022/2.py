"""
1. n을 k 진수로 변환
"""
import math
def convert_k_number(num, k):
    rev_base = ''
    while num > 0:
        num, mod = divmod(num, k)
        rev_base += str(mod)
    return rev_base[::-1]

def is_prime_number(x):
    if x <= 1:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

def find_candidate_number(num):
    candidate_number = []
    candidate = []
    for n in num:
        if n == '0':
            if candidate and candidate[-1] != '0':
                num = ''.join(candidate)
                if is_prime_number(int(num)):
                    candidate.append('0')
                    candidate_number.append(''.join(candidate))
                    candidate = ['0']
                else:
                    candidate = ['0']
        else:
            candidate.append(n)
    if candidate and candidate[-1] != '0':
        if is_prime_number(int(''.join(candidate))):
            candidate_number.append(''.join(candidate))
    return candidate_number


def process(candidate_number):
    answer = 0
    for num in candidate_number:
        if num[0] == '0' and num[-1] == '0':
            answer += 1
            continue
        if num[0] == '0':
            answer += 1
            continue
        if num[-1] == '0':
            answer += 1
            continue
        if num[0] != '0' and num[-1] != '0':
            answer += 1
    return answer

def solution(n, k):
    n = convert_k_number(n, k)

    candidate_number = find_candidate_number(n)

    return process(candidate_number)



if __name__ == "__main__":

    a = 1232310232021
    print(solution(437674, 3))
    print(solution(110011, 10))
    print(solution(1234234, 3))
    print(solution(101500126010, 10))
    print(solution(43648924, 3))
    print(solution(11309000801, 10))