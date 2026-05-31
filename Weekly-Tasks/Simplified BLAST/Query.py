from Indexing import get_kmers, hash_sequence
import Indexing


def main():

    query = input('Enter a query to BLAST: ')
    isNucleic = bool(input('Nucleic sequence? (True/False): '))
    k = 11 if isNucleic else 3
    path = r"test_dna.fasta" if isNucleic else r"test_protein.fasta"

    kmers = get_kmers(query, k)
    hashed_kmers = hash_sequence(kmers, k, isNucleic)
    kmer_to_hash = dict(zip(kmers, hashed_kmers))

    db = Indexing.main(path, isNucleic, k)

    matches = [] # Example: (Sequence_1, [1, 23], [3])
    for target in db:
        tree = db[target]

        for kmer in hashed_kmers:
            target_positions = tree.find(kmer)
            query_positions = hashed_kmers[kmer]

            if target_positions:
                matches.append((target, target_positions.positions, query_positions))

    print(matches)

main()
