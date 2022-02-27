# https://programmers.co.kr/learn/courses/30/lessons/43165

def solution(numbers, target):
    end_depth = len(numbers)

    def dfs(depth, current_sum):
        if depth == end_depth:
            return 1 if current_sum == target else 0

        return dfs(depth+1, current_sum + numbers[depth]) + dfs(depth+1, current_sum - numbers[depth])
    return dfs(0, 0)



if __name__ == '__main__':
    numbers = [1, 1, 1, 1, 1]
    target = 3
    print(solution(numbers, target))

    numbers = [4, 1, 2, 1]
    target = 4
    print(solution(numbers, target))
