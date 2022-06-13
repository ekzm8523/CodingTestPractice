import sys
# import math
input = lambda: sys.stdin.readline().strip()

# def is_prime(num):
#     for i in range(2, int(math.sqrt(num)) + 1):
#         if num % i == 0:
#             return False
#     return True

if __name__ == '__main__':
    N = int(input())
    prime_list = []
    candidate = set(range(2, N + 1))

    for i in range(2, N + 1):
        if i in candidate:
            prime_list.append(i)
            num = i
            while num <= N:
                if num in candidate:
                    candidate.remove(num)
                num += i
    # for prime in prime_list:
    #     assert is_prime(prime), "error"

    # 예외처리
    if len(prime_list) == 0:  # 소수가 없는경우 N == 1
        print(0)
        exit()
    elif len(prime_list) == 1:  # 하나인경우 N == 2
        if prime_list[0] == N:
            print(1)
        else:
            print(0)
        exit()

    answer = 0
    left, right = 0, 1
    _sum = prime_list[left] + prime_list[right]
    last_idx = len(prime_list) - 1
    while True:
        if _sum < N:
            if right == last_idx:
                break
            right += 1
            _sum += prime_list[right]
        elif _sum >= N:
            if _sum == N:
                answer += 1
            if left == right:
                break
            _sum -= prime_list[left]
            left += 1

    print(answer)