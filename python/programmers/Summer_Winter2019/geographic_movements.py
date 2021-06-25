# https://programmers.co.kr/learn/courses/30/lessons/62050

def solution(land, height):
    answer = 0
    return answer


if __name__ == "__main__":
    land = [[1, 4, 8, 10], [5, 5, 5, 5], [10, 10, 10, 10], [10, 10, 10, 20]]
    h = 3
    print(solution(land, h))    #15
    land = [[10, 11, 10, 11], [2, 21, 20, 10], [1, 20, 21, 11], [2, 1, 2, 1]]
    h = 1
    print(solution(land, h))    #18