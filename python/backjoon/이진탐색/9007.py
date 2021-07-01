# https://www.acmicpc.net/problem/9007

"""
4명 1000m 대회 참가
각 클래스는 M명씩 동일
 k : 특정값 , n : 각 반에 있는 학생수
"""

from bisect import bisect_left, bisect_right

if __name__ == "__main__":
    num_test = int(input())

    for test in range(num_test):
        k, n = map(int, input().split())
        class_list = []
        answer = 0
        for i in range(4):
            class_list.append(list(map(int, input().split())))
        class12 = []
        class34 = []
        for i in range(n):
            for j in range(n):
                class12.append(class_list[0][i] + class_list[1][j])
        for i in range(n):
            for j in range(n):
                class34.append(class_list[2][i] + class_list[3][j])

        class34.sort()
        answer_list = []
        for s in class12:
            new_k = k - s
            if class34[-1] < new_k:
                new_v_idx = -1
            else:
                new_v_idx = bisect_left(class34, new_k)
            if abs(k - answer) >= abs(k - class34[new_v_idx] - s):
                if abs(k - answer) == abs(k - class34[new_v_idx] - s) and (k - answer) > (k - class34[new_v_idx] - s):
                    continue
                else:
                    answer = class34[new_v_idx] + s

            if new_v_idx > 0:
                if abs(k - answer) >= abs(k - class34[new_v_idx - 1] - s):
                    if abs(k - answer) == abs(k - class34[new_v_idx - 1] - s) and\
                            (k - answer) > (k - class34[new_v_idx-1] - s):
                        continue
                    else:
                        answer = class34[new_v_idx - 1] + s


        print(answer)

