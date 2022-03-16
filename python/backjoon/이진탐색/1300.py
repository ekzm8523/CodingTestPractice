# https://www.acmicpc.net/problem/1300

if __name__ == "__main__":

    n = int(input())
    k = int(input())

    start, end = 1, k
    answer = 0
    while start <= end:
        mid = (start + end) // 2

        cnt = 0
        for i in range(1, n + 1):
            cnt += min(n, mid // i)
            if cnt >= k:
                break
        if cnt >= k:
            end = mid - 1
            answer = mid
        elif cnt < k:
            start = mid + 1


    print(answer)