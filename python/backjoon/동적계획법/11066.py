# https://www.acmicpc.net/problem/11066
# dp[i][j] -> i부터 j까지 weight의 최소값
import sys

if __name__ == '__main__':
    test_cnt = int(input())

    for _ in range(test_cnt):
        chapter_cnt = int(input())
        chapters = tuple(map(int, input().split()))
        prefix_sum = [0]
        for chapter in chapters:
            prefix_sum.append(prefix_sum[-1] + chapter)
        # i부터 j까지 누적합 -> prefix_sum[j+1] - prefix[i] ( i < j )
        size = len(chapters)

        dp = [[sys.maxsize] * size for _ in range(size)]
        for i in range(size):
            dp[i][i] = chapters[i]
        for i in range(size-1):
            dp[i][i+1] = chapters[i] + chapters[i+1]

        for length in range(2, size):
            for left in range(size-length):
                right = left + length
                for mid in range(left, right):
                    left_sum = 0 if left == mid else dp[left][mid]
                    right_sum = 0 if mid + 1 == right else dp[mid+1][right]
                    dp[left][right] = min(dp[left][right], left_sum + right_sum)
                dp[left][right] += prefix_sum[right + 1] - prefix_sum[left]

        print(dp[0][-1])



"""
1
4
40 30 30 50

2
4
40 30 30 50
15
1 21 3 4 5 35 5 4 3 5 98 21 14 17 32





"""

