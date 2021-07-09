
"""
1. 2진수로 바꿨을때 1의 갯수를 기준으로 오름차순
2. 1번을 한뒤 겹치는 친구들을 10진수를 기준으로 오름차순
"""



def solution(nums):
    answer = []

    car_list = []
    for num in nums:
        car_list.append([bin(num).count('1'), num])

    car_list.sort(key=lambda x: (x[0], x[1]))

    for _, value in car_list:
        answer.append(value)
    return answer
if __name__ == "__main__":

    test1 = [31, 15, 7, 3, 2]
    test2 = [1, 2, 4, 3, 5]
    print(solution(test1))
    print(solution(test2))
