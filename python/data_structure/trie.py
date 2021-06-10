"""
입력되는 문자열을 Tree 형식으로 만들어 진행되어 보다 빠르게 문자열 검색이 가능한 자료구조
빠른 시간복잡도 덕분에 검색엔진 사이트에서 제공하는 자동 완성 및 검색어 추천 기능에서 Trie 알고리즘을 사용
"""


class Node(object):
    def __init__(self, key, data=None):
        self.key = key  # 값으로 입력될 문자
        self.data = data    # 문자열의 종료를 알리는 flag
        self.children = {}  # 자식노드를 저장


class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, word):
        """
        입력된 문자열의 문자를 하나씩 children에 확인 후 저장하고
        문자열을 다 돌면 마지막 노드의 data에 문자열을 저장
        """
        current_node = self.head

        for ch in word:
            if ch not in current_node.children:
                current_node.children[ch] = Node(ch)
            current_node = current_node.children[ch]
        current_node.data = word


    def search(self, word):
        current_node = self.head

        for ch in word:
            if ch in current_node.children:
                current_node = current_node.children[ch]
            else:
                return False

        if current_node.data:
            return True
        else:
            return False


    def starts_with(self, prefix):
        """
        prefix로 시작하는 단어를 찾고 배열로 return하는 함수
        prefix단어까지 tree를 순회한 후 그 다음부터 data가 존재하는 것들만 배열에 저장하여 리
        """
        current_node = self.head
        words = []

        for ch in prefix:
            if ch in current_node.children:
                current_node = current_node.children[ch]
            else:
                return None

        current_node = [current_node]
        next_node = []
        while True:
            for node in current_node:
                if node.data:
                    words.append(node.data)
                next_node.extend(list(node.children.values()))
            if len(next_node) != 0:
                current_node = next_node
                next_node = []
            else:
                break
        return words


if __name__ == "__main__":
    trie = Trie()
    word_list = ["frodo", "front", "firefox", "fire"]
    for word in word_list:
        trie.insert(word)

    print(trie.search("friend"))

    print(trie.search("frodo"))
    print(trie.search("fire"))
    print(trie.starts_with("fire"))
    print(trie.starts_with("fro"))
    print(trie.starts_with("jimmy"))
    print(trie.starts_with("f"))