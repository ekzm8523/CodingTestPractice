# https://programmers.co.kr/learn/courses/30/lessons/43165
def dfs(numbers, target, depth, sum):
    if depth == len(numbers):
        if sum == target:
            return 1
        else:
            return 0

    return dfs(numbers, target, depth+1, sum + numbers[depth])\
           + dfs(numbers, target, depth+1, sum - numbers[depth])

def solution(numbers, target):
    answer = 0

    return dfs(numbers, target, 1, numbers[0]) + dfs(numbers, target, 1, -numbers[0])




if __name__ == '__main__':
    numbers = [1,1,1,1,1]
    target = 3
    print(solution(numbers, target))
