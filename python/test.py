from pprint import pprint
def solution(w, e):
    answer = 0
    D = [[1 for _ in range(e)] for _ in range(w)]
    # eCw
    for i in range(1, w):
        for j in range(i+1, e):
            print(j, i, end="|")
        print()
if __name__ == "__main__":

    w, e = list(map(int, input().split()))
    solution(w, e)



