# https://www.acmicpc.net/problem/10844

if __name__ == '__main__':
    n = int(input())
    cur_dp = [0] * 10

    for i in range(1, 10):
        cur_dp[i] = 1

    for i in range(2, n+1):
        pre_dp = cur_dp.copy()
        for j in range(10):
            if j == 0:
                cur_dp[j] = pre_dp[j+1]
            elif j == 9:
                cur_dp[j] = pre_dp[j-1]
            else:
                cur_dp[j] = pre_dp[j+1] + pre_dp[j-1]
    print(sum(cur_dp) % 1000000000)