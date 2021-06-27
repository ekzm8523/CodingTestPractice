# https://www.acmicpc.net/problem/11729

def hanoi(start, sub, end, n):
    global answer

    if n == 1:
        answer.append((start, end))
        return

    hanoi(start, end, sub, n - 1)
    answer.append((start, end))
    hanoi(sub, start, end, n - 1)




if __name__ == "__main__":
    answer = []
    n = int(input())

    hanoi(1,2,3,n)
    print(len(answer))
    for x, y in answer:
        print(x, y)