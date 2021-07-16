
from collections import deque

def maxEvents(arrival, duration):

    answer = 0
    bit_list = []
    for arr, dur in zip(arrival, duration):
        tmp = 0
        for i in range(arr, arr + dur):
            tmp = tmp | 1 << i
        bit_list.append(tmp)

    q = deque()
    q.append(bit_list)
    while q:
        bl = q.popleft()
        answer += 1
        next_bl = []
        for bit in bl:
            for check_bit in bit_list:
                if bit & check_bit == 0:
                    next_bl.append(bit | check_bit)
        if next_bl:
            q.append(next_bl)

    return answer


if __name__ == "__main__":
    n = 5
    arrival = [1, 3, 3, 5, 7]
    duration = [2, 2, 1, 2, 1]
    print(maxEvents(arrival, duration))


    # def maxEvents(arrival, duration):
    #     """
    #     sort를 해서 기간이 짧은 회사부터 예약하도록 하는건 최솟값을 보장하지 못한다.
    #     arrival = [1, 4, 5]
    #     duration = [4, 2, 4]
    #     일때 0번 2번 회사를 예약하는게 최댓값이다.
    #     dp와 함께 쓰면 솔루션이 나올듯
    #     """
    #     tie_arr = sorted([(arrival[i], duration[i]) for i in range(arrival_count)], key=lambda x: x[1])
    #
    #     bit_mask = 0
    #     answer = 0
    #
    #     for arr, dur in tie_arr:
    #         flag = True
    #         tmp = bit_mask
    #         for i in range(arr, arr + dur):
    #             if tmp & (1 << i) == 0:
    #                 tmp += (1 << i)
    #             else:
    #                 flag = False
    #         if flag:
    #             bit_mask = tmp
    #             answer += 1
    #
    #     return answer