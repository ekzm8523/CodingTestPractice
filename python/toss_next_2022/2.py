"""
운반을 위해 최대 M의 무게를 실으는 트럭을 고용
M = 10, W = [2, 3, 7, 8]일떄
트럭에 실을 수 있는 최대 무게 M
운반해야 하는 물건의 무게가 들어있는 배열 load
모든 물건을 운반하기 위해 필요한 트럭의 최솟값 return
1 <= M <= 40
1 <= load <= 12
1 <= load의 원소 <= 40
모든 물건을 옮길 수 없으면 -1 반환 -> 이건 물건중에 M보다 큰게 있을때?
"""
# https://www.acmicpc.net/problem/1480
from itertools import permutations

def solution(M, loads):
    """
    최대한 꽉꽉 채워서 보내는게 가장 좋다.
    그러면 정렬 후 투 포인터?
    하지만 이는 반례가 존재한다.
    M = 20, load = [19, 17, 16, 15, 5, 3, 3, 1 ,1]
    앞에서 가능한거 뒤에서 가능한거 합쳐가면서 하다보면 answer는 4지만 5가 나옴
    완전 탐색이 좋을 듯 하다. 왜냐하면 load가 크지 않기 때문에 정렬하는 방법은 12!정도 -> 4억번의 연산
    -> 무조건 시간 초과임
    ->
    """
    answer = 500
    max_load = max(loads)
    if max_load > M:
        return -1
    for comb_loads in permutations(loads):
        truck_count = 1
        weight = 0
        for load in comb_loads:
            weight += load
            if weight > M:
                truck_count += 1
                weight = load
        answer = min(answer, truck_count)

    return answer

if __name__ == '__main__':
    load = [2, 3, 7, 8]
    M = 10
    print(solution(M, load))

    load = [2, 2, 2, 2, 2]
    M = 5
    print(solution(M, load))

    load = [16, 15, 9, 17, 1, 3]
    M = 20
    print(solution(M, load))