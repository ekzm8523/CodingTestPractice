# https://www.acmicpc.net/problem/3273

if __name__ == "__main__":
    n = int(input())
    nums = sorted(list(map(int, input().split())))
    target = int(input())
    answer = 0
    l, r = 0, n-1

    while l < r:
        s = nums[l] + nums[r]
        if s == target:
            answer += 1
            l += 1
        elif s < target:
            l += 1
        else:
            r -= 1

    print(answer if n > 1 else 0)
