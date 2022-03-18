import random
from bisect import bisect_right


def main():
    meal_cnt = 8000

    meals = [random.randint(1, 2498) for _ in range(meal_cnt)]
    meals.sort()

    answer = 0
    for i in range(meal_cnt - 2):
        for j in range(i + 1, meal_cnt - 1):
            if meals[i] + meals[j] > 2500:
                break
            remain_sum = 2500 - (meals[i] + meals[j])

            idx = bisect_right(meals, remain_sum, lo=j + 1)  # 합이 처음으로 2500이 넘는 idx

            if idx == j + 1:  # 맞는게 하나도 없을 때
                break

            answer += (idx - j - 1)
    print(answer)


if __name__ == "__main__":
    main()