
from pprint import pprint

def solution(maps, p, r):
    answer = 0
    pprint(maps)
    return answer

if __name__ == "__main__":
    maps = [[1, 28, 41, 22, 25, 79, 4], [39, 20, 10, 17, 19, 18, 8], [21, 4, 13, 12, 9, 29, 19], [58, 1, 20, 5, 8, 16, 9], [5, 6, 15, 2, 39, 8, 29],[39, 7, 17, 5, 4, 49, 5], [74, 46, 8, 11, 25, 2, 11]]
    p, r = 19, 6
    print(solution(maps, p, r))
    # maps = [[47, 8, 99, 9, 85, 3, 8], [90, 93, 8, 25, 98, 15, 97], [9, 95, 91, 87, 8, 81, 9], [98, 88, 82, 89, 79, 81, 97], [97, 35, 31, 97, 81, 2, 92], [32, 16, 49, 9, 91, 89, 17], [53, 6, 35, 12, 13, 98, 5]]
    # maps = [[9, 8, 17, 55, 19, 7], [1, 25, 5, 39, 28, 8], [88, 19, 28, 3, 2, 9], [76, 73, 7, 18, 16, 14], [99, 8, 8, 7, 11, 9], [1, 18, 4, 10, 3, 6]]
    # maps = [[6, 3, 2, 7, 3], [7, 2, 1, 6, 8], [8, 9, 8, 4, 9], [7, 9, 2, 7, 1], [6, 3, 6, 8, 4]]
