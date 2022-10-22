# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S, C):
    # write your code in Python 3.8.10

    required_dollar_range_set = set()
    ch_pos_dict = {}
    for i, ch in enumerate(S):
        if ch not in ch_pos_dict:
            ch_pos_dict[ch] = i
        else:
            required_dollar_range_set.add((ch_pos_dict[ch] + 1, i))
            ch_pos_dict[ch] = i
    answer = 0

    for dollar_pos in C:
        if not required_dollar_range_set:
            break
        remove_ranges = [r for r in required_dollar_range_set if r[0] <= dollar_pos <= r[1]]

        for remove_range in remove_ranges:
            required_dollar_range_set.remove(remove_range)
        answer += 1

    return answer if not required_dollar_range_set else -1


if __name__ == '__main__':
    print(solution('aabcba', [1, 3, 2]))
    print(solution('aaa', [1, 2]))
    print(solution('aabcddcb', [3, 5, 1, 4, 7]))
    print(solution('wkwk', [1]))
    print(solution('abcd', [1, 2]))