"""
라이언이 가장 큰 점수 차이로 우승할 수 있는 방법이 여러 가지 일 경우, 가장 낮은 점수를 더 많이 맞힌 경우를 return 해주세요.

"""

def calculate_score_dif(A, B):
    dif = 0
    for i in range(10):
        score = 10 - i
        if A[i] == 0 and B[i] == 0:
            continue

        if A[i] < B[i]:
            dif += score
        else:
            dif -= score
    return dif

def solution(n, info):
    answer = [0] * 11

    weight = {}
    for i, cnt in enumerate(info):
        score = 10 - i
        if cnt == 0:
            weight[score] = (score, 1)
        else:
            weight[score] = ((score * 2) / (cnt + 1), cnt + 1)

    priority = sorted(weight.items(), key=lambda x: (x[1], -cnt, -x[0]), reverse=True) #weight가 같으면 더 낮은 점수가 우선순위로 오도록

    remain_arrow = n
    for obj_num, (_, cnt) in priority:
        if cnt <= remain_arrow:
            answer[10 - obj_num] = cnt
            remain_arrow -= cnt
        if remain_arrow == 0:
            break

    if remain_arrow != 0:
        answer[-1] = remain_arrow

    if calculate_score_dif(info, answer) <= 0:
        return [-1]

    return answer


if __name__ == "__main__":
    n = 5
    info = [2,1,1,1,0,0,0,0,0,0,0]
    result = [0,2,2,0,1,0,0,0,0,0,0]
    print("my_result     = ", solution(n, info))
    print("answer_result = ", result)

    n = 1
    info = [1,0,0,0,0,0,0,0,0,0,0]
    result =[-1]
    print("my_result     = ", solution(n, info))
    print("answer_result = ", result)

    n = 9
    info =[0,0,1,2,0,1,1,1,1,1,1]
    result =[1,1,2,0,1,2,2,0,0,0,0]
    print("my_result     = ", solution(n, info))
    print("answer_result = ", result)

    n = 10
    info = [0,0,0,0,0,0,0,0,3,4,3]
    result = [1,1,1,1,1,1,1,1,0,0,2]
    print("my_result     = ", solution(n, info))
    print("answer_result = ", result)