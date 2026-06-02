import Logic as logic

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
            if self.left is None:
                return None
            else:
                return self.left.find(value)
        else:
            if self.right is None:
                return None
            else:
                return self.right.find(value)

class DataBase:
    def __init__(self, path, isNucleic):
        self.path = path
        self.isNucleic = isNucleic
        self.sequences = logic.get_sequences(self.path)
        self.k = 11 if isNucleic else 3

        self.id_to_kmers = {}
        self.id_to_hashes = {}
        self.id_to_trees = {}

        self.length = self.get_full_length()

        for seq_id, sequence in self.sequences.items():
            kmers = logic.get_kmers(sequence, self.k)
            self.id_to_kmers[seq_id] = kmers

            hashed_sequence = logic.hash_sequence(kmers, self.k, self.isNucleic)
            self.id_to_hashes[seq_id] = hashed_sequence

            tree = build_balanced_bst(hashed_sequence, 0, len(hashed_sequence) - 1)
            self.id_to_trees[seq_id] = tree

    def get_full_length(self):
        length = 0
        with open(self.path, "r") as f:
            for line in f:
                if not line.startswith(">"):
                    length += len(line.strip())
        return length

def build_balanced_bst(data, left, right):
    nodes = list(data.keys())
    nodes.sort()

    if left > right:
        return None
    mid = left + (right - left) // 2

    key = nodes[mid]
    node = TreeNode(key, data[key])

    node.left = build_balanced_bst(data, left, mid - 1)
    node.right = build_balanced_bst(data, mid + 1, right)

    return node
