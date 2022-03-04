# https://www.acmicpc.net/problem/1912
# num을 순회하며 처음부터 시작할지 아니면 이어 붙일지 결정
from collections import Counter
if __name__ == '__main__':
    n = int(input())
    nums = list(map(int, input().split()))
    current_sum = nums[0]
    answer = current_sum
    for num in nums[1:]:
        current_sum = max(current_sum + num, num)
        answer = max(answer, current_sum)
    print(answer)