class TrieNode:
    def __init__(self):
        self.children = {}


def build_suffix_trie(s):
    root = TrieNode()
    for i in range(len(s)):
        current = root
        for char in s[i:]:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
    return root


def get_suffix_tree_edges(root):
    edges = []

    for char, child in root.children.items():
        current_string = char
        current_node = child

        while len(current_node.children) == 1:
            next_char, next_node = list(current_node.children.items())[0]
            current_string += next_char
            current_node = next_node

        edges.append(current_string)

        edges.extend(get_suffix_tree_edges(current_node))

    return edges


def solve_suffix_tree(dataset):
    s = "".join(dataset.split())

    if not s.endswith('$'):
        s += '$'

    root = build_suffix_trie(s)
    edges = get_suffix_tree_edges(root)
    return edges

