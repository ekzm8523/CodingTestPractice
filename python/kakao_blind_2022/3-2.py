# https://programmers.co.kr/learn/courses/30/lessons/92341
import math


def solution(fees, records):
    fee_info = {}

    for record in records:
        record_time, car_number, query = record.split()
        hour, minute = map(int, record_time.split(':'))
        timestamp = hour * 60 + minute

        if car_number not in fee_info:
            fee_info[car_number] = [0, timestamp]  # 사용시간, 쿼리시간, 쿼리
        else:
            if query == "IN":
                fee_info[car_number][1] = timestamp

            elif query == "OUT":
                fee_info[car_number][0] += timestamp - fee_info[car_number][1]
                fee_info[car_number][1] = -1

    final_timestamp = 60 * 23 + 59
    for key in fee_info:
        if fee_info[key][1] >= 0:
            fee_info[key][0] += final_timestamp - fee_info[key][1]

    answer = []
    for key in sorted(fee_info):
        fee = fees[1]
        if fee_info[key][0] > fees[0]:
            remain_time = fee_info[key][0] - fees[0]
            fee += math.ceil(remain_time / fees[2]) * fees[3]
        answer.append(fee)
    return answer


if __name__ == '__main__':
    fees = [180, 5000, 10, 600]  # 기본 시간(분), 기본 요금(원), 단위 시간(분)
    records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN",
               "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
    print(solution(fees, records))

    fees = [120, 0, 60, 591]
    records = ["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]
    print(solution(fees, records))

    fees = [1, 461, 1, 10]
    records = ["00:00 1234 IN"]
    print(solution(fees, records))