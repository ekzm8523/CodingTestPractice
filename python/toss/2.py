"""
순자산이 10억원 이상이 되었을 때 모두 판매
처음 구매한 가격의 50%이상 떨어졌을 경우에만, 토스뱅크에서 5천만원을 추가로 대출 받아 주식을 추가 구매
대출은 한번만 받을 수 있으며, 5천만원 한도입니다. 이후 추가 구매는 하지 않습니다

"""

def stock(start_day, prices):

    size = len(prices)
    # print(f'day {start_day} : ', end=" ")
    my_asset = int(1e8)
    is_loan = False
    stock_cnt = my_asset // prices[start_day]
    my_asset -= stock_cnt * prices[start_day]

    for day in range(start_day + 1, size):
        # print(f'day {day} : ', end=" ")
        # print(f" buy price : {prices[start_day]} today price : {prices[day]} ")
        # print(f" having stock : {stock_cnt} my_asset : {my_asset} sum : {prices[day] * stock_cnt + my_asset}")

        if prices[day] * stock_cnt + my_asset >= int(1e9):
            return day - start_day


        if prices[day] * 2 < prices[start_day] and not is_loan:
            is_loan = True
            my_asset += 5 * int(1e7)
            added_stock = my_asset // prices[day]
            stock_cnt += added_stock
            my_asset -= added_stock * prices[day]
            my_asset -= 5 * int(1e7)
            # print(f" having stock : {stock_cnt} my_asset : {my_asset} sum : {prices[day] * stock_cnt + my_asset}")

        # print(prices[day], end=' ')

    return -1




def solution(prices):
    answer = []
    for day in range(len(prices)):
        answer.append(stock(day, prices))

    return answer


if __name__ == "__main__":

    price1 = [78000, 48000, 27000, 285000, 320000, 335100]   # [5, -1, 1, -1, -1, -1]
    price2 = [34000,78000, 48000, 27000, 11000, 285000, 320000, 335100]	    # [5, 6, 3, 2, 1, -1, -1, -1]

    print(solution(price1))
    print(solution(price2))
    print(solution([]))