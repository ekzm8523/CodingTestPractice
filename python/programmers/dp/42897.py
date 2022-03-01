# https://programmers.co.kr/learn/courses/30/lessons/42897

def solution(money):
    house_cnt = len(money)

    dp = [[0] * 2 for _ in range(house_cnt)]
    dp[0][1], dp[1][1] = money[0], max(money[:1])
    dp[1][0] = money[1]
    for i in range(2, house_cnt - 1):
        dp[i][1] = max(dp[i - 2][1] + money[i], dp[i - 1][1])  # 1번째를 포함한 dp
        dp[i][0] = max(dp[i - 2][0] + money[i], dp[i - 1][0])  # 1번째를 뺀 dp

    dp[-1][0] = max(dp[-3][0] + money[-1], dp[-2][0])
    dp[-1][1] = max(dp[-3][1], dp[-2][1])

    return max(dp[-1])


if __name__ == '__main__':
    money = [1, 2, 3, 1]
    print(solution(money))
