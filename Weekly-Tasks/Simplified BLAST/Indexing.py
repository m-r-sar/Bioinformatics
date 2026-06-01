from Bio import SeqIO

NUCLEOTIDE_HASH = {
    'A': 0,  # Adenine
    'C': 1,  # Cytosine
    'G': 2,  # Guanine
    'T': 3,  # Thymine
    'U': 4,  # Uracil
    'N': 5   # Unknown nucleotide
}

AMINO_ACID_HASH = {
    'A': 0,  # Alanine (Ala)
    'R': 1,  # Arginine (Arg)
    'N': 2,  # Asparagine (Asn)
    'D': 3,  # Aspartic acid (Asp)
    'C': 4,  # Cysteine (Cys)
    'Q': 5,  # Glutamine (Gln)
    'E': 6,  # Glutamic acid (Glu)
    'G': 7,  # Glycine (Gly)
    'H': 8,  # Histidine (His)
    'I': 9,  # Isoleucine (Ile)
    'L': 10, # Leucine (Leu)
    'K': 11, # Lysine (Lys)
    'M': 12, # Methionine (Met)
    'F': 13, # Phenylalanine (Phe)
    'P': 14, # Proline (Pro)
    'S': 15, # Serine (Ser)
    'T': 16, # Threonine (Thr)
    'W': 17, # Tryptophan (Trp)
    'Y': 18, # Tyrosine (Tyr)
    'V': 19, # Valine (Val)
    'X': 20  # Unknown amino acid
}

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
        self.sequences = get_sequences(self.path)
        self.k = 11 if isNucleic else 3

        self.id_to_kmers = {}
        self.id_to_hashes = {}
        self.id_to_trees = {}

        self.length = self.get_full_length()

        for seq_id, sequence in self.sequences.items():
            kmers = get_kmers(sequence, self.k)
            self.id_to_kmers[seq_id] = kmers

            hashed_sequence = hash_sequence(kmers, self.k, self.isNucleic)
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


def get_sequences(path):
    sequences = {}
    for record in SeqIO.parse(path, "fasta"):
        sequences[record.id] = str(record.seq)
    return sequences


def get_kmers(sequence, k):
    kmers = {}
    for i in range(0, len(sequence) - k + 1):
        if sequence[i:i + k] not in kmers:
            kmers[sequence[i:i + k]] = [i]
        else:
            kmers[sequence[i:i + k]].append(i)
    return kmers


def hash_sequence(kmers, k, isNucleic):
    hashed_sequence = {}
    hash_table = NUCLEOTIDE_HASH if isNucleic else AMINO_ACID_HASH
    base = 5 if isNucleic else 21

    for kmer in kmers:
        code = 0
        for i in range(1, k+1):
            code += hash_table[kmer[i-1]] * (base ** (k-i))
        hashed_sequence[code] = kmers[kmer]
    return hashed_sequence
