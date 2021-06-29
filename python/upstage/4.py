def count_internal_nodes(tree):
    internal_node = set()
    for parent in tree:
        internal_node.add(parent)
    return len(internal_node) - 1

if __name__ == "__main__":
    tree = [1, 3, 1, -1, 3]
    print(count_internal_nodes(tree)) # should print 2