from dataclasses import dataclass, field
from typing import Dict
import sys

@dataclass
class Node:
    data: str = None
    children: Dict = field(default_factory=dict)


class Trie:
    def __init__(self):
        self.head = Node()

    def insert(self, s):
        current_node = self.head

        for ch in s:
            if ch not in current_node.children:
                current_node.children[ch] = Node()
            current_node = current_node.children[ch]
        current_node.data = s


    def search(self, s) -> bool:
        current_node = self.head

        for ch in s:
            if ch in current_node.children:
                current_node = current_node.children[ch]
            else:
                return False
        if current_node.data and current_node.data == s:
            return True
        return False


if __name__ == '__main__':
    n, m = map(int, sys.stdin.readline().split())
    trie = Trie()

    for _ in range(n):
        trie.insert(sys.stdin.readline())
    answer = 0
    for _ in range(m):
        if trie.search(sys.stdin.readline()):
            answer += 1

    print(answer)





