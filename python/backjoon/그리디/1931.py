# https://www.acmicpc.net/problem/1931

if __name__ == "__main__":
    N = int(input())
    book_list = [list(map(int, input().split())) for _ in range(N)]
    book_list.sort(key=lambda x: (x[1], x[0]))

    cnt = 0
    end_time = 0

    for book in book_list:
        if end_time <= book[0]:
            end_time = book[1]
            cnt += 1

    print(cnt)