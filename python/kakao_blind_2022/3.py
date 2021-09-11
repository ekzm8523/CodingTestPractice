"""
어떤 차량이 입차된 후에 출차된 내역이 없다면, 23:59에 출차된 것으로 간주합니다.
    - 0000번 차량은 18:59에 입차된 이후, 출차된 내역이 없습니다. 따라서, 23:59에 출차된 것으로 간주합니다.
00:00부터 23:59까지의 입/출차 내역을 바탕으로 차량별 누적 주차 시간을 계산하여 요금을 일괄로 정산합니다.
누적 주차 시간이 기본 시간이하라면, 기본 요금을 청구합니다.
누적 주차 시간이 기본 시간을 초과하면, 기본 요금에 더해서, 초과한 시간에 대해서 단위 시간 마다 단위 요금을 청구합니다.
    - 초과한 시간이 단위 시간으로 나누어 떨어지지 않으면, 올림합니다.
    - ⌈a⌉ : a보다 작지 않은 최소의 정수를 의미합니다. 즉, 올림을 의미합니다.
차량 번호가 작은 자동차부터 청구할 주차 요금을 차례대로 정수 배열에 담아서 return 하도록 solution 함수를 완성해주세요.
"""

from math import ceil

def get_time(time):
    s = int(time[:2])
    m = int(time[3:])
    return s * 60 + m

def calculate_fee(fees, parking_time):
    default_time, default_fee, unit_time, unit_fee = fees

    if parking_time <= default_time:
        return default_fee
    parking_time -= default_time
    fee = default_fee
    fee += ceil(parking_time / unit_time) * unit_fee
    return fee

def solution(fees, records):
    answer = []


    record_by_car = {}
    for record in records:
        record_time, car_number, query = record.split()
        if car_number in record_by_car.keys():
            record_by_car[car_number].append((record_time, query))
        else:
            record_by_car[car_number] = [(record_time, query)]

    parking_time_dic = {}
    for car_number, log in record_by_car.items():
        in_time = None
        parking_time_dic[car_number] = 0
        for record_time, query in log:
            if query == "IN":
                in_time = get_time(record_time)
            elif query == "OUT":
                out_time = get_time(record_time)
                parking_time_dic[car_number] += (out_time - in_time)
                in_time = None
        if in_time != None:
            out_time = get_time("23:59")
            parking_time_dic[car_number] += (out_time - in_time)

    for car_number in sorted(parking_time_dic):
        parking_time = parking_time_dic[car_number]
        answer.append(calculate_fee(fees, parking_time))

    return answer


if __name__ == "__main__":
    fees = [180, 5000, 10, 600]
    record = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN",
                    "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
    print(solution(fees, record))

    fees = [120, 0, 60, 591]
    record = ["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]
    print(solution(fees, record))

    fees = [1, 461, 1, 10]
    record = ["00:00 1234 IN"]
    print(solution(fees, record))