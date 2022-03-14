
def main():
    meal_cnt = int(input())

    meals = list(map(int, input().split()))
    meals.sort()
    answer = 0
    # 이분탐색?
    for i in range(meal_cnt - 2):
        if meals[i] > 2500:
            break
        for j in range(i + 1, meal_cnt - 1):
            if meals[i] + meals[j] > 2500:
                break
            for k in range(j + 1, meal_cnt):
                s = meals[i] + meals[j] + meals[k]
                if 2000 <= s <= 2500:
                    answer += 1
                elif 2500 < s:
                    break

    print(answer)


if __name__ == "__main__":
    main()