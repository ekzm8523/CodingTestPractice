# https://programmers.co.kr/learn/courses/30/lessons/67256


def calc_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def solution(numbers, hand):
    answer = ''
    l_pos = (3, 0)
    r_pos = (3, 2)

    for number in numbers:
        pos = (3, 1) if number == 0 else divmod(number-1, 3)

        if pos[1] == 0:
            answer += "L"
            l_pos = pos
        elif pos[1] == 2:
            answer += "R"
            r_pos = pos
        else:
            l_dis = calc_distance(l_pos, pos)
            r_dis = calc_distance(r_pos, pos)
            if l_dis > r_dis:
                answer += "R"
                r_pos = pos
            elif l_dis < r_dis:
                answer += "L"
                l_pos = pos
            else:
                if hand == "right":
                    answer += "R"
                    r_pos = pos
                else:
                    answer += "L"
                    l_pos = pos
        # print(number, pos, answer, hand, l_pos, r_pos)
    return answer

if __name__ == "__main__":
    numbers1 = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
    hand1 = "right"
    print("LRLLLRLLRRL" == solution(numbers1, hand1))


    numbers2 = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
    hand2 = "left"
    print("LRLLRRLLLRR" == solution(numbers2, hand2))

    numbers3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    hand3 = "right"
    print("LLRLLRLLRL" == solution(numbers3, hand3))

