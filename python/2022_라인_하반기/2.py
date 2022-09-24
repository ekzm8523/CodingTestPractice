"""
알파벳 소문자, 특수문자로 이루어진 단어를 공백으로 분리
비속어와 일치하면 #으로 가림
.은 1이상 k 이하의 길이로 대체 가능
"""

from typing import List


def is_bad_word(k: int, bad_word: str, word: str) -> bool:
    _is_bad_word = False

    def dfs(bad_idx: int, idx: int, skip_cnt: int) -> None:

        nonlocal _is_bad_word
        if _is_bad_word:
            return
        if skip_cnt == k:
            return
        if bad_idx == len(bad_word) and idx == len(word):
            _is_bad_word = True
            return
        if bad_idx == len(bad_word) or idx == len(word):
            return

        if bad_word[bad_idx] == word[idx]:
            dfs(bad_idx + 1, idx + 1, 0)

        if word[idx] == '.':
            dfs(bad_idx + 1, idx + 1, 0)
            dfs(bad_idx + 1, idx, skip_cnt + 1)


    dfs(0, 0, 0)

    return _is_bad_word


def solution(k: int, dic: List[str], chat: str) -> str:
    answer = []

    for word in chat.split():

        for bad_word in dic:
            if is_bad_word(k, bad_word, word):
                answer.append('#' * len(word))
                break
        else:
            answer.append(word)

    return ' '.join(answer)


if __name__ == '__main__':
    # print(solution(3, ["abcdcfg"], "a.c."))
    print(solution(2, ["slang", "badword"], "badword ab.cd bad.ord .word sl.. bad.word"))
    # print(solution(2, ["badword"], ".word sl.. bad.word"))
    print(solution(3, ["abcde", "cdefg", "efgij"], ".. ab. cdefgh .gi. .z."))
