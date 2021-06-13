"""
기둥과 보 설치
https://programmers.co.kr/learn/courses/30/lessons/60061
[x, y, a, b]
x,y -> 가로 좌표, 세로 좌표
a -> 설치할 구조물의 종류 0은 기둥 1은 보
b -> 구조물을 설치할 지 혹은 삭제할 지를 나타내며 0은 삭제, 1은 설치
바닥에 보 금지
out of index X
보는 오른쪽, 기둥은 위로만 설치


output
[x, y, a]
x,y는 위와 같음
a는 구조물의 종류로 위와 같음
마지막 쿼리까지 처리하고 남은 구조물들을 이런식으로 출력하면 된다.

"""

def check_answer(results, answers):
    for i, (result, answer) in enumerate(zip(results, answers)):
        if result == answer:
            print(f"{i + 1}번 정답")
        else:
            print(f"{'*' * 10} {i + 1}번 오답 {'*' * 10}\n 정답 -> {answer} \n 내꺼 -> {result}")

def impossible(result):
    COL, ROW = 0, 1
    for x, y, a in result:
        if a == COL:    # 기둥
            if y != 0 and (x, y-1, COL) not in result and \
                    (x-1, y, ROW) not in result and (x, y, ROW) not in result: # 밑에 기둥이 없고 왼쪽아래 보가 없고 아래 보가 없을때
                return True # 불가능하다
        else:   # 보
            if (x, y-1, COL) not in result and (x+1, y-1, COL) not in result and \
                not ((x-1, y, ROW) in result and (x+1, y, ROW) in result):
                return True
    return False

def solution(n, build_frame):
    result = set()

    for x, y, a, build in build_frame:
        item = (x, y, a)
        if build:   # add
            result.add(item)
            if impossible(result):
                result.remove(item)
        elif item in result:    # remove
            result.remove(item)
            if impossible(result):
                result.add(item)
    answer = map(list, result)

    return sorted(answer, key=lambda x: (x[0], x[1], x[2]))

if __name__ == "__main__":

    results = []
    answers = [[[1,0,0],[1,1,1],[2,1,0],[2,2,1],[3,2,1],[4,2,1],[5,0,0],[5,1,0]],
               [[0,0,0],[0,1,1],[1,1,1],[2,1,1],[3,1,1],[4,0,0]]]

    n = 5
    build_frame = [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 2, 1, 1], [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1],
                   [3, 2, 1, 1]]
    results.append(solution(n, build_frame))

    n = 5
    build_frame = [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]
    results.append(solution(n, build_frame))

    check_answer(results, answers)


