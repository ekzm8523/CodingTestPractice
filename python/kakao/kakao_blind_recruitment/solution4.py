
"""
https://programmers.co.kr/learn/courses/30/lessons/60060
1. 길이가 같아야함
두가지로 나누기
?가 접미사로 나올떄 word[0] == '?'
?가 점두사로 나올
간단한 문제인줄 알았으나 trie라는 새로운 자료구조가 등장한다.

"""


class Node:
    def __init__(self):
        self.alpha = {}
        self.count = 0


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        temp = self.root

        for w in word:
            if temp.alpha.get(w):
                temp = temp.alpha[w]
            else:
                temp.alpha[w] = Node()
                temp = temp.alpha[w]
            temp.count += 1

    def search(self, que):
        cnt = 0
        if que == '':
            for val in self.root.alpha.values():
                cnt += val.count
            return cnt
        temp = self.root
        for w in que:
            if temp.alpha.get(w):
                temp = temp.alpha[w]
                cnt = temp.count
            else:
                return 0
        return cnt


def solution(words, queries):
    t_a = [Trie() for i in range(10001)]
    r_a = [Trie() for i in range(10001)]

    # words => Tries
    for word in words:
        t_a[len(word)].insert(word)
        r_a[len(word)].insert(word[::-1])

    # Search => queries
    answer = [0 for _ in range(len(queries))]
    for idx, que in enumerate(queries):
        if que[0] != '?':  # queries => t_a
            s_que = que.split('?')[0]
            answer[idx] = t_a[len(que)].search(s_que)
        else:  # queries => r_a
            s_que = que.split('?')[-1]
            answer[idx] = r_a[len(que)].search(s_que[::-1])

    return answer


def check_answer(results, answers):
    for i, (result, answer) in enumerate(zip(results, answers)):
        if result == answer:
            print(f"{i + 1}번 정답")
        else:
            print(f"{'*' * 10} {i + 1}번 오답 {'*' * 10}\n 정답 -> {answer} \n 내꺼 -> {result}")


if __name__ == "__main__":
    words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
    queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
    answers = []
    results = []

    results.append(solution(words, queries))
    answers.append([3, 2, 4, 1, 0])
    check_answer(results, answers)
