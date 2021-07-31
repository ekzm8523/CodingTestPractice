import sys

class Trie:

    def __init__(self):
        self.root = {}

    def add(self, foods):
        cur = self.root

        for food in foods:
            if food not in cur:
                cur[food] = {}
            cur = cur[food]
        cur[0] = True

    def travel(self, cur, depth):

        children = sorted(cur)

        if 0 in children:
            return

        for child in children:
            print('--' * depth + child)
            self.travel(cur[child], depth + 1)


if __name__ == "__main__":

    n = int(sys.stdin.readline())
    foods = []
    trie = Trie()

    for _ in range(n):
        trie.add(list(sys.stdin.readline().split())[1:])

    trie.travel(trie.root, 0)
    print()

