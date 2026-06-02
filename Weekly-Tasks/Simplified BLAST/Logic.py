from Bio import SeqIO
import contextlib
import os
import pickle
import json

def get_sequences(path):
    """ Parse FASTA """
    sequences = {}
    for record in SeqIO.parse(path, "fasta"):
        sequences[record.id] = str(record.seq)
    return sequences

def get_kmers(sequences, k):
    """ Generates dicts with k-mers connected to their appearances """
    kmers = {}
    for sequence_id, sequence in sequences.items():
        for i in range(0, len(sequence) - k + 1):
            if sequence[i:i + k] in kmers:
                kmers[sequence[i:i + k]].append((sequence_id, i))
            else:
                kmers[sequence[i:i + k]] = [(sequence_id, i)]
    return kmers

def save_data(obj, filename):
    """ Saves indexed database """
    with open(filename, 'wb') as f:
        pickle.dump(obj, f)

def load_data(filename):
    """ Loads indexed database """
    with open(filename, 'rb') as f:
        return pickle.load(f)

def load_options(filename):
    """ Loads options (wow) """
    with open(f"{filename}", 'r') as f:
        return json.load(f)

def save_to_file_or_print(obj, hsps, name, save_to_file = False):
    """ Selects whether to output to a file or to the console depending on input method """
    if save_to_file:
        results_dir = os.path.join(os.getcwd(), "results")
        if not os.path.isdir(results_dir):
            os.mkdir(results_dir)
        path = unique_file_name(os.path.join(results_dir, f"Simplified_BLAST_result_{name}.txt"))
        with open(path, 'w', encoding='utf-8') as f:
            with contextlib.redirect_stdout(f):
                obj.output(hsps)
        print(f"Results saved at: {path}")

    else:
        obj.output(hsps)

def unique_file_name(path):
    """ Provides unique file names """
    directory, filename = os.path.split(path)
    name, ext = os.path.splitext(filename)

    counter = 1
    new_path = path

    while os.path.exists(new_path):
        new_filename = f"{name}_{counter}{ext}"
        new_path = os.path.join(directory, new_filename)
        counter += 1

    return new_path
