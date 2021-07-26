import sys

class Trie():
    def __init__(self):
        self.root = {}

    def add(self, foods):
        cur = self.root

        for food in foods:
            if food not in cur:
                cur[food] = {}
            cur = cur[food]
        cur[0] = True

    def travel(self, depth, cur):
        if 0 in cur:
            return

        children = sorted(cur)

        for child in children:
            print("--" * depth + child)
            self.travel(depth + 1, cur[child])


if __name__ == "__main__":

    n = int(sys.stdin.readline())
    trie = Trie()
    for _ in range(n):
        trie.add(list(sys.stdin.readline().split()[1:]))
    trie.travel(0, trie.root)
