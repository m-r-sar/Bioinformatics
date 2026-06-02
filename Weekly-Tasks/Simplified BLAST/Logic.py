import pickle
from Bio import SeqIO
import contextlib
import os

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

def save_data(obj, filename):
    with open(filename, 'wb') as f:
        pickle.dump(obj, f)


def load_data(filename):
    with open(filename, 'rb') as f:
        return pickle.load(f)

def save_to_file_or_print(obj, hsps, name, save_to_file = False):
    if save_to_file:
        if not os.path.isdir(os.getcwd() + r"\results"):
            os.mkdir(os.getcwd() + r"\results")
        path = unique_file_name(os.getcwd() + fr"\results\Simplified_BLAST_result_{name}.txt")
        with open(path, 'w', encoding='utf-8') as f:
            with contextlib.redirect_stdout(f):
                obj.output(hsps)
        print(f"Results saved at: {path}")

    else:
        obj.output(hsps)

def unique_file_name(path):
    directory, filename = os.path.split(path)
    name, ext = os.path.splitext(filename)

    counter = 1
    new_path = path

    while os.path.exists(new_path):
        new_filename = f"{name}_{counter}{ext}"
        new_path = os.path.join(directory, new_filename)
        counter += 1

    return new_path
