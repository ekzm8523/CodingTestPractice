# https://programmers.co.kr/learn/courses/30/lessons/43105?language=python3

def solution(triangle):

    triangle_height = len(triangle)

    for h in range(triangle_height -1 , 0, -1):
        for i in range(h):
            triangle[h-1][i] += max(triangle[h][i:i+2])
    return triangle[0][0]


if __name__ == '__main__':
    triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
    print(solution(triangle))
