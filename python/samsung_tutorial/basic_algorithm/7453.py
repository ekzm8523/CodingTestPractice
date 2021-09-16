import sys
"""
dict를 사용할때 가장 빠른방법은 keys를 찾는 방법이다.
실험한 결과는 time_check.py 파일을 확인할 것
"""
if __name__ == "__main__":

    n = int(sys.stdin.readline())
    A = []
    B = []
    C = []
    D = []
    for _ in range(n):
        a, b, c, d = map(int, sys.stdin.readline().split())
        A.append(a)
        B.append(b)
        C.append(c)
        D.append(d)

    comb_dic = {}
    for i in range(n):
        for j in range(n):
            v = A[i] + B[j]
            if v in comb_dic.keys():
                comb_dic[v] += 1
            else:
                comb_dic[v] = 1

    answer = 0
    for i in range(n):
        for j in range(n):
            wanted_value = -(C[i] + D[j])
            if wanted_value in comb_dic.keys():
                answer += comb_dic[wanted_value]


    print(answer)
