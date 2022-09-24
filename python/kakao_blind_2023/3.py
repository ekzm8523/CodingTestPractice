from itertools import product


def solution(users, emoticons):

    best_join_cnt = 0
    best_sale_mount = 0
    for discount_rates in product([10, 20, 30, 40], repeat=len(emoticons)):
        purchases = [0] * len(users)
        join_cnt = 0
        sale_mount = 0
        for emo_idx, discount_rate in enumerate(discount_rates):
            for user_idx, (purchase_rate, _) in enumerate(users):
                if purchase_rate <= discount_rate:  # 할인율이 더 크면
                    purchases[user_idx] += emoticons[emo_idx] * (1 - (discount_rate / 100))

        for (_, join_price), price in zip(users, purchases):
            if join_price <= price:
                join_cnt += 1
            else:
                sale_mount += price
        if best_join_cnt < join_cnt:
            best_join_cnt, best_sale_mount = join_cnt, sale_mount
        elif best_join_cnt == join_cnt:
            if best_sale_mount < sale_mount:
                best_sale_mount = sale_mount

    return [best_join_cnt, int(best_sale_mount)]


if __name__ == '__main__':
    print(solution([[40, 10000], [25, 10000]], [7000, 9000]))
    print(solution([[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]], [1300, 1500, 1600, 4900]))