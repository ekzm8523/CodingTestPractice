# https://programmers.co.kr/learn/courses/30/lessons/43163
"""
1. 한 번에 한 개의 알파벳만 바꿀 수 있습니다.
2. words에 있는 단어로만 변환할 수 있습니다.
"""
def dif_cnt(str1, str2):
    cnt = 0
    for a, b in zip(str1, str2):
        if a == b:
            cnt += 1
    return cnt


def solution(begin, target, words):
    if target not in words:
        return 0

    answer = 0
    visit = [False] * len(words)
    word_len = len(begin)

    def dfs(current_word, depth):
        nonlocal visit, answer
        if answer != 0 and depth >= answer:
            return

        if current_word == target:
            answer = depth
            return

        for i, word in enumerate(words):
            if not visit[i] and dif_cnt(current_word, word) == word_len - 1:
                visit[i] = True
                dfs(word, depth + 1)
                visit[i] = False
    dfs(begin, 0)

    return answer


if __name__ == '__main__':
    begin = "hit"
    target = "cog"
    words = ["hot", "dot", "dog", "lot", "log", "cog"]
    print(solution(begin, target, words))

    begin = "hit"
    target = "cog"
    words = ["hot", "dot", "dog", "lot", "log"]
    print(solution(begin, target, words))
