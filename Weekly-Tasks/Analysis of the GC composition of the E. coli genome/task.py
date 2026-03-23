import numpy as np
import matplotlib.pyplot as plt
from Bio import SeqIO

FILENAME = "GCA_000005845.2_ASM584v2_genomic.fna"
FILE_FORMAT = "fasta"
WINDOW_SIZE = 10000
STEP = 10000


def parse_FASTA(filename, format):
    """ Function for parsing first sequence in FASTA file into one string """
    record = next(SeqIO.parse(filename, format))
    return record.upper()


def counting_nucleotides(seq, w, s):
    """ Function for counting G, C nucleotides in sliding window, their % and skew """
    gc_percentages = []
    gc_skews = []
    positions = []
    seq_length = len(seq)
    for i in range(0, seq_length, s):

        if seq_length - i >= w:
            window = seq[i:i + w]
            actual_w = len(window)

            g_count = window.count('G')
            c_count = window.count('C')

            gc_percent = ((g_count + c_count) / actual_w) * 100
            gc_percentages.append(gc_percent)

            if (g_count + c_count) > 0:
                skew = (g_count - c_count) / (g_count + c_count)
            else:
                skew = 0.0
            gc_skews.append(skew)

            positions.append((i + actual_w / 2) / 1_000_000)

    return gc_percentages, gc_skews, positions


def vizualize(data, skew_data, positions):
    """ Function for visualizing data """
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8))
    ax1.plot(positions, data)
    ax1.set_xlabel("Mb")
    ax1.set_ylabel("GC%")
    ax1.set_title("GC% in E. Coli genome")
    ax1.axhline(float(np.mean(data)), color='r', linestyle='--')

    ax2.fill_between(positions, skew_data, 0, where=np.array(skew_data) >= 0, facecolor='#27ae60', interpolate=True,
                     alpha=0.4)
    ax2.fill_between(positions, skew_data, 0, where=np.array(skew_data) < 0, facecolor='#c0392b', interpolate=True,
                     alpha=0.4)
    ax2.plot(positions, skew_data, linewidth=0.5)
    ax2.set_xlabel("Mb")
    ax2.set_ylabel("Skewness")
    ax2.set_title("Skewness in E. Coli genome")
    ax2.axhline(0, color='r')
    plt.tight_layout()
    plt.show()


data, skew_data, positions = counting_nucleotides(parse_FASTA(FILENAME, FILE_FORMAT), WINDOW_SIZE, STEP)
vizualize(data, skew_data, positions)
