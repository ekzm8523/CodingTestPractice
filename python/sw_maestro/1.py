from dataclasses import dataclass, field


@dataclass
class Node:
    cnt: int = 0
    children: dict = field(default_factory=dict)


class Trie:
    def __init__(self):
        self.head = Node()

    def insert(self, word) -> None:
        current_node = self.head
        for ch in word:
            if ch not in current_node.children:
                current_node.children[ch] = Node()
            current_node = current_node.children[ch]
            current_node.cnt += 1

    def find(self, word) -> int:
        current_node = self.head
        for ch in word:
            if ch not in current_node.children:
                return 0
            current_node = current_node.children[ch]
        return current_node.cnt


def main():
    keyword_cnt = int(input())
    keywords = [input() for _ in range(keyword_cnt)]
    trie = Trie()

    for keyword in keywords:
        trie.insert(keyword)

    word_cnt = int(input())
    for _ in range(word_cnt):
        word = input()
        print(trie.find(word))


if __name__ == "__main__":
    main()


"""
[입력예시]
4
smtp
smeea
smqzzfs
sefefefa
3
s
sm
software
[출력]
4
3
0
"""