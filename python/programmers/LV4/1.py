import sys


def solution(matrix_sizes):
    answer = 0
    size = len(matrix_sizes)

    dp = [[sys.maxsize] * size for _ in range(size)]

    dp[0][0] = 0
    for i in range(1, size):
        weight = matrix_sizes[i-1][0] * matrix_sizes[i][0] * matrix_sizes[i][1]
        dp[i][i] = 0
        dp[i-1][i] = weight
    for left in range(size - 1):
        for mid in range(left + 1, size):
            for right in range(mid + 1, size):
                dp[left][right] = min(dp[left][right],
                                      dp[left][mid] + dp[mid + 1][right] + matrix_sizes[left][0] * matrix_sizes[mid][1] * matrix_sizes[right][1])
    print(dp)


    return answer


if __name__ == '__main__':
    matrix_size = [[5,3], [3,10], [10,6]]
    print(solution(matrix_size))