# https://programmers.co.kr/learn/courses/30/lessons/77486
from collections import defaultdict

def solution(enroll, referral, seller, amount):
    """
    :param enroll: 판매원의 이름을 담은 배열
    :param referral: 각 판매원을 다단계 조직에 참여시킨 다른 판매원의 이름을 담은 배열
    :param seller: 판매량 집계 데이터의 판매원 이름을 나열한 배열
    :param amount: 집계 데이터의 판매 수량을 나열한 배열
    :return: 각 판매원이 득한 이익금을 나열한 배
    """
    answer = []
    link_dic = defaultdict(str)
    price_dic = defaultdict(int)

    for i, name in enumerate(referral):
        if name == '-':
            name = "king_jw"
        link_dic[enroll[i]] = name

    for name, price in zip(seller, amount):
        price *= 100
        while price > 0:
            residual = price // 10
            price_dic[name] += price - residual
            price = residual
            if link_dic[name] == 'king_jw' or residual == 0:
                break
            name = link_dic[name]

    for name in enroll:
        answer.append(price_dic[name])

    return answer


if __name__ == "__main__":
    enroll1 = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
    enroll2 = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]

    referral1 = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
    referral2 = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]

    seller1 = ["young", "john", "tod", "emily", "mary"]
    seller2 = ["sam", "emily", "jaimie", "edward"]

    amount1 = [12, 4, 2, 5, 10]
    amount2 = [2, 3, 5, 4]

    result1 = [360, 958, 108, 0, 450, 18, 180, 1080]
    result2 = [0, 110, 378, 180, 270, 450, 0, 0]

    answer1 = solution(enroll1, referral1, seller1, amount1)
    answer2 = solution(enroll2, referral2, seller2, amount2)

    if answer1 == result1:
        print(f"1번 정답 { answer1 }")
    else:
        print(f"{'*'*10} 1번 오답 {'*'*10}\n 정답 -> {result1} \n 내꺼 -> {answer1}")
    if answer2 == result2:
        print(f"2번 정답 { answer2 }")
    else:
        print(f"{'*' * 10} 2번 오답 {'*' * 10}\n 정답 -> {result2} \n 내꺼 -> {answer2}")