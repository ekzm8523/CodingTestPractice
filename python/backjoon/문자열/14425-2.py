import sys
input = lambda: sys.stdin.readline().rstrip()


class Node:
    def __init__(self, data=None):
        self.children = {}
        self.data = data


class Trie:

    def __init__(self):
        self.head = Node()

    def insert(self, word) -> None:
        current = self.head

        for ch in word:
            if ch not in current.children:
                current.children[ch] = Node()
            current = current.children[ch]
        current.data = word

    def find(self, word) -> bool:
        current = self.head

        for ch in word:
            if ch not in current.children:
                return False
            current = current.children[ch]
        return current.data is not None


if __name__ == "__main__":
    word_cnt, query_cnt = map(int, input().split())
    trie = Trie()
    for _ in range(word_cnt):
        trie.insert(input())

    answer = 0

    for _ in range(query_cnt):
        if trie.find(input()):
            answer += 1

    print(answer)