from collections import defaultdict

def find_unique_numbers(numbers):
    dic = defaultdict(int)
    answer = []
    for number in numbers:
        dic[number] += 1

    for key, value in dic.items():
        if value == 1:
            answer.append(key)

    return answer


if __name__ == "__main__":
    print(find_unique_numbers([1, 2, 1, 3, 4, 8, 8]))