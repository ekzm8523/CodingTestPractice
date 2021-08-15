
def solution(s):
    dic = {}
    s = s.lower()
    for ch in s:
        if ch in dic:
            dic[ch] += 1
        else:
            dic[ch] = 1
    sorted_dic = sorted(dic.items(), key=(lambda x:x[1]), reverse=True)

    max_value = sorted_dic[0][1]
    candidate = set()
    for k, v in sorted_dic:
        if max_value != v:
            break
        candidate.add(k)
    answer = []

    if 't' in candidate:
        answer.append('T')
        candidate.remove('t')
    if 'o' in candidate:
        answer.append('O')
        candidate.remove('o')
    if 's' in candidate:
        answer.append('SS')
        candidate.remove('s')
    candidate = sorted(list(candidate))
    answer += candidate

    return ''.join(answer)

if __name__ == "__main__":
    s1 = "aAb"  # "a"
    s2 = "BA"   # "b"
    s3 = "BbA"  # "b"
    s4 = "aaBBTtooSS"   #"TOSSab"

    print(solution(s1))
    print(solution(s2))
    print(solution(s3))
    print(solution(s4))

