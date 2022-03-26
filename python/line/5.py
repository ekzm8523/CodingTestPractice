"""
능력치 sorting 하고
두개씩 묶어서 gap을 계산한다
gap 차이가 가장 큰 순서대로 우선권을 사용한다.
"""

def solution(abilities, k):
    answer = 0
    abilities.sort(key=lambda x: -x)

    round_cnt = (len(abilities) + 1) // 2
    gap_list = []
    for i in range(round_cnt - 1):
        gap_list.append(abilities[i * 2] - abilities[i * 2 + 1])

    if len(abilities) % 2 == 1:
        gap_list.append(abilities[-1])
    else:
        gap_list.append(abilities[-2] - abilities[-1])
    idx2gap = {idx: gap for idx, gap in enumerate(gap_list)}
    using_priority_key = set(sorted(idx2gap, key=lambda x: -idx2gap[x])[:k])

    for round_num in range(round_cnt - 1):
        if round_num in using_priority_key:
            answer += abilities[round_num * 2]
        else:
            answer += abilities[round_num * 2 + 1]

    if len(abilities) % 2 == 1:
        if round_num + 1 in using_priority_key:
            answer += abilities[-1]
    else:
        if round_num + 1 in using_priority_key:
            answer += abilities[-2]
        else:
            answer += abilities[-1]


    return answer


if __name__ == '__main__':
    abilities = [2, 8, 3, 6, 1, 9, 1, 9]
    k = 2
    print(solution(abilities, k))
    abilities = [7, 6, 8, 9, 10]
    k = 1
    print(solution(abilities, k))

