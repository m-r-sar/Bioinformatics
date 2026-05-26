class TreeNode:
    def __init__(self, key, positions):
        self.key = key
        self.positions = positions
        self.left = None
        self.right = None
    def find(self, value):
        if self.key == value:
            return self
        elif self.key > value:
            return self.left.find(value)
        else:
            return self.right.find(value)

def build_balanced_bst(nodes, data, left, right):
    if left > right:
        return None
    mid = left + (right - left) // 2

    key = nodes[mid]
    print(key)
    node = TreeNode(key, data[key])

    node.left = build_balanced_bst(nodes, data, left, mid - 1)
    node.right = build_balanced_bst(nodes, data, mid + 1, right)

    return node

data = {
    6: [3], 12: [16], 14: [12], 15: [7], 19: [11], 20: [10],
    26: [4], 33: [2], 35: [6, 15], 40: [1, 5, 14], 53: [9],
    58: [13], 61: [8]
}

nodes = list(data.keys())
nodes.sort()

tree = build_balanced_bst(nodes, data, 0, len(nodes) - 1)
print(tree.find(35).positions)