import matplotlib.pyplot as plt
import numpy as np
from itertools import islice

def load_data(filename):
    with open(filename, "r") as f:
        return [line.strip() for line in islice(f, 3, None, 4)]

def build_quality_matrix(reads):
    max_len = len(max(reads, key=len))
    num_reads = len(reads)

    matrix = np.full((num_reads, max_len), -1, dtype=np.int8)

    for i, read in enumerate(reads):
        row_data = np.frombuffer(read.encode('ascii'), dtype=np.int8) - 33
        matrix[i, :len(read)] = row_data

    return matrix

def get_mean_quality(matrix):
    mask = matrix >= 0
    total_mean = np.mean(matrix[mask])
    mean_quality = np.mean(matrix, axis=0, where=mask)

    return mean_quality, total_mean


if __name__ == "__main__":
    filenames = ["SRR39135629_1.fastq", "SRR39135629_1_clear.fastq"]
    for filename in filenames:
        reads_quality = load_data(filename)

        matrix = build_quality_matrix(reads_quality)

        mean_quality, total_mean = get_mean_quality(matrix)

        possible_lengths = range(0, len(max(reads_quality, key=len)))

        plt.plot(possible_lengths, mean_quality)
        plt.xlabel('Length')
        plt.ylabel('Mean Quality')
        plt.title(f'Quality Scores across all bases for {filename}')
        plt.axhline(
            y = total_mean,
            color = 'r',
            linestyle = 'dashed',
            label = 'Overall Mean Quality',
            linewidth = 2
        )
        plt.savefig(fname=f"{filename}.png")