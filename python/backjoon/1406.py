# https://www.acmicpc.net/problem/1406
import sys


class Node:
    def __init__(self, ch=None, before=None, next_=None):
        self.ch = ch
        self.before = before
        self.next = next_


class Editor:

    def __init__(self, s):
        # self.editor = {0: Node(s[0])}
        self.header = Node()
        self.ptr = self.header
        for ch in s:
            next_node = Node(ch, before=self.ptr)
            self.ptr.next = next_node
            self.ptr = next_node


    def move_left(self):
        if self.ptr != self.header:
            self.ptr = self.ptr.before

    def move_right(self):
        if self.ptr.next:
            self.ptr = self.ptr.next

    def delete(self):
        if self.ptr == self.header:
            return

        self.ptr.before.next = self.ptr.next
        if self.ptr.next:
            self.ptr.next.before = self.ptr.before
        buf = self.ptr
        self.ptr = self.ptr.before
        del buf

    def add(self, ch):
        new_node = Node(ch)
        if self.ptr.next:
            self.ptr.next.before = new_node
            new_node.next = self.ptr.next
        self.ptr.next = new_node
        new_node.before = self.ptr
        self.ptr = new_node


    def print(self):
        buf = []
        ptr = self.header
        while True:
            if ptr.ch:
                buf.append(ptr.ch)
            if ptr.next:
                ptr = ptr.next
            else:
                break
        print(''.join(buf))
        del buf


if __name__ == "__main__":

    init_str = sys.stdin.readline().rstrip()
    editor = Editor(init_str)
    query_cnt = int(sys.stdin.readline())
    for _ in range(query_cnt):
        query = sys.stdin.readline().split()
        if query[0] == 'L':
            editor.move_left()
        elif query[0] == "D":
            editor.move_right()
        elif query[0] == "B":
            editor.delete()
        elif query[0] == "P":
            editor.add(query[1])

    editor.print()