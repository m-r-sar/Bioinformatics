# Global Sequence Alignment (Needleman-Wunsch)

A from-scratch Python implementation of the Needleman-Wunsch algorithm for global sequence alignment. This tool uses `numpy` to build the scoring matrix and performs a traceback to find the optimal mathematical alignment between two nucleotide or amino acid sequences.

## Description

This script aligns two sequences end-to-end, penalizing gaps and mismatches while rewarding matches. It successfully replicates the mathematical output of industry-standard libraries like BioPython's `PairwiseAligner`, providing a transparent look under the hood of how dynamic programming is used in bioinformatics.

## Features

* **Customizable Weights:** Easily adjust the scores for matches, mismatches, and gap penalties.
* **Traceback Visualization:** Outputs a visual matching string indicating exact matches (`|`), mismatches (`.`), and gaps (`-`).
* **Zero Dependencies:** Built entirely with standard Python logic and `numpy` for matrix operations.

## Prerequisites

* Python 3.x
* NumPy (`pip install numpy`)

## Usage

You can run the alignment by calling the `global_alignment` function with your two sequences and your chosen scoring parameters `(match, mismatch, gap)`. 

Note: Typically, mismatches and gaps are passed as negative integers.

```python

# --- Example Run ---
target = "GCATGCU"
query = "GATTACA"

# Parameters: Match = 1, Mismatch = -3, Gap = -2
r1, r2, score, matching = global_alignment(target, query, 1, -3, -2)

print("Target:  ", 0, r1, len(target))
print("Matching:", 0, matching, len(matching))
print("Query:   ", 0, r2, len(querry))
print("\nFinal score:", s)

# --- OUTPUT ---
# Target:   0 GCA-TGCU 7
# Matching: 0 |-|-|.|. 8
# Query:    0 G-ATTACA 7
# 
# Final score: -6.0
