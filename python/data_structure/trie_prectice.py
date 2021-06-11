
class Node(object):
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}
        self.count = 0


class Trie():
    def __init__(self):
        self.head = Node(None)

    def insert(self, word):

        ptr = self.head

        for ch in word:
            if ch not in ptr.children:
                ptr.children[ch] = Node(ch)
            ptr = ptr.children[ch]
            ptr.count += 1
        ptr.data = word

    def search(self, word):

        ptr = self.head

        for ch in word:
            if ch not in ptr.children:
                return False
            ptr = ptr.children[ch]

        if ptr.data:
            return True
        return False

    def starts_with(self, prefix):

        cnt = 0
        if prefix == "":
            for val in self.head.children.values():
                cnt += val.count
            return cnt

        ptr = self.head
        for ch in prefix:
            if ch not in ptr.children:
                return 0
            ptr = ptr.children[ch]
            cnt = ptr.count

        return cnt


def check_answer(results, answers):
    for i, (result, answer) in enumerate(zip(results, answers)):
        if result == answer:
            print(f"{i + 1}번 정답")
        else:
            print(f"{'*' * 10} {i + 1}번 오답 {'*' * 10}\n 정답 -> {answer} \n 내꺼 -> {result}")


def solution(words, queries):
    answer = []

    trie = [Trie() for _ in range(10001)]
    reverse_trie = [Trie() for _ in range(10001)]

    for word in words:
        trie[len(word)].insert(word)
        reverse_trie[len(word)].insert(word[::-1])

    for querie in queries:
        if querie[0] == "?":
            q = querie.rsplit("?")[-1]
            answer.append(reverse_trie[len(querie)].starts_with(q[::-1]))
        else:
            q = querie.split("?")[0]
            answer.append(trie[len(querie)].starts_with(q))

    return answer

if __name__ == "__main__":
    words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
    queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
    answers = []
    results = []

    results.append(solution(words, queries))
    answers.append([3, 2, 4, 1, 0])
    check_answer(results, answers)