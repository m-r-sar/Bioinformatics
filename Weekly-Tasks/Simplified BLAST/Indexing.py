import Logic as logic

class DataBase:
    def __init__(self, path, isNucleic, k):
        self.path = path
        self.isNucleic = isNucleic
        self.k = k

        self.sequences = logic.get_sequences(self.path)
        self.length = sum(len(seq) for seq in self.sequences.values())

        self.hash_table = logic.get_kmers(self.sequences, self.k)