
from collections import deque

class Node:
    alphabet = None
    left = None
    right = None


class huffman_tree:
    def __init__(self, codes):
        self.codes = codes
        self.root = Node()
        self.make_tree()


    def make_tree(self):
        for code in codes:
            current_node = self.root
            alphabet, code = code.split('\t')
            for bit in code:
                if bit == '1':
                    if current_node.right is None:
                        current_node.right = Node()
                    current_node = current_node.right
                elif bit == '0':
                    if current_node.left is None:
                        current_node.left = Node()
                    current_node = current_node.left
                else:
                    print("이상한 bit가 들어왔어요 확인바람")
                    print(alphabet, code)
            current_node.alphabet = alphabet





def decode(codes, encoded):

    """
    1. codes를 보고 huffman tree를 만든다.
    2. 하나씩 tree를 타고 들어가면서 출력한다.
    """
    print(codes)
    print(encoded)

    tree = huffman_tree(codes)

    q = deque(encoded)
    # decode
    current_node = tree.root
    answer = []
    while q:
        bit = q.popleft()
        if bit == '1':
            current_node = current_node.right
        elif bit == '0':
            current_node = current_node.left
        else:
            print("이상한 bit가 들어왔어요 확인바람")
            print(bit, q)
        if current_node.alphabet:
            if current_node.alphabet == "[newline]":
                answer.append('\n')
            else:
                answer.append(current_node.alphabet)
            current_node = tree.root
    return ''.join(answer)

if __name__ == "__main__":
    codes = ['a\t100100', 'b\t100101', 'c\t110001', 'd\t100000', '[newline]\t111111', 'p\t111110', 'q\t000001']
    encoded = '111110000001100100111111100101110001111110'
    print(decode(codes, encoded))