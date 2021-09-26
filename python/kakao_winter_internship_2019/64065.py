
def data_preprocessing(s):
    split_data = s[1:-1].split('},')
    for i, data in enumerate(split_data):
        split_data[i] = data[1:]
    split_data[-1] = split_data[-1][:-1]


    dic = {}
    for data in split_data:
        data = data.split(',')
        size = len(data)
        dic[size] = data
    return dic
def solution(s):
    answer = []
    result = data_preprocessing(s)
    tuple_size = max(result.keys())

    s = set()
    for i in range(1, tuple_size + 1):
        for v in result[i]:
            v = int(v)
            if v not in s:
                answer.append(v)
                s.add(v)

    return answer

# import re
# from collections import Counter
#
# def solution(s):
#
#     s = Counter(re.findall('\d+', s))
#     return list(map(int, [k for k, v in sorted(s.items(), key=lambda x: x[1], reverse=True)]))


if __name__ == "__main__":
    s = "{{2},{2,1},{2,1,3},{2,1,3,4}}"
    print(solution(s))

    s = "{{1,2,3},{2,1},{1,2,4,3},{2}}"
    print(solution(s))

    s = "{{20,111},{111}}"
    print(solution(s))

    s = "{{123}}"
    print(solution(s))

    s = "{{4,2,3},{3},{2,3,4,1},{2,3}}"
    print(solution(s))