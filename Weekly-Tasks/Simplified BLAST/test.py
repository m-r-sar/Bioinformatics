import random

def generate_mock_fasta(filename, alphabet, count=5000, min_len=100, max_len=500):
    """Generates a FASTA file with random sequences."""
    with open(filename, 'w') as f:
        for i in range(1, count + 1):
            # Pick a random length for this sequence
            seq_len = random.randint(min_len, max_len)
            # Generate the random string
            sequence = ''.join(random.choices(alphabet, k=seq_len))
            # Write in FASTA format
            f.write(f">mock_sequence_{i} length={seq_len}\n{sequence}\n")

# Standard Alphabets
DNA_ALPHABET = ['A', 'C', 'G', 'T']
PROTEIN_ALPHABET = ['A', 'R', 'N', 'D', 'C', 'E', 'Q', 'G', 'H', 'I',
                    'L', 'K', 'M', 'F', 'P', 'S', 'T', 'W', 'Y', 'V']

# Generate 100 of each
generate_mock_fasta('test_dna.fasta', DNA_ALPHABET)
generate_mock_fasta('test_protein.fasta', PROTEIN_ALPHABET)

print("✅ Generated test_dna.fasta and test_protein.fasta")

