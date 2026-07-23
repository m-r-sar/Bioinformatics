import numpy as np
from numba import njit
import argparse

BLOSUM62 = {'*': {'*': 1, 'A': -4, 'B': -4, 'C': -4, 'D': -4, 'E': -4, 'F': -4, 'G': -4, 'H': -4, 'I': -4, 'K': -4, 'L': -4, 'M': -4, 'N': -4, 'P': -4, 'Q': -4, 'R': -4, 'S': -4, 'T': -4, 'V': -4, 'W': -4, 'X': -4, 'Y': -4, 'Z': -4}, 'A': {'*': -4, 'A': 4, 'B': -2, 'C': 0, 'D': -2, 'E': -1, 'F': -2, 'G': 0, 'H': -2, 'I': -1, 'K': -1, 'L': -1, 'M': -1, 'N': -2, 'P': -1, 'Q': -1, 'R': -1, 'S': 1, 'T': 0, 'V': 0, 'W': -3, 'X': 0, 'Y': -2, 'Z': -1}, 'B': {'*': -4, 'A': -2, 'B': 4, 'C': -3, 'D': 4, 'E': 1, 'F': -3, 'G': -1, 'H': 0, 'I': -3, 'K': 0, 'L': -4, 'M': -3, 'N': 3, 'P': -2, 'Q': 0, 'R': -1, 'S': 0, 'T': -1, 'V': -3, 'W': -4, 'X': -1, 'Y': -3, 'Z': 1}, 'C': {'*': -4, 'A': 0, 'B': -3, 'C': 9, 'D': -3, 'E': -4, 'F': -2, 'G': -3, 'H': -3, 'I': -1, 'K': -3, 'L': -1, 'M': -1, 'N': -3, 'P': -3, 'Q': -3, 'R': -3, 'S': -1, 'T': -1, 'V': -1, 'W': -2, 'X': -2, 'Y': -2, 'Z': -3}, 'D': {'*': -4, 'A': -2, 'B': 4, 'C': -3, 'D': 6, 'E': 2, 'F': -3, 'G': -1, 'H': -1, 'I': -3, 'K': -1, 'L': -4, 'M': -3, 'N': 1, 'P': -1, 'Q': 0, 'R': -2, 'S': 0, 'T': -1, 'V': -3, 'W': -4, 'X': -1, 'Y': -3, 'Z': 1}, 'E': {'*': -4, 'A': -1, 'B': 1, 'C': -4, 'D': 2, 'E': 5, 'F': -3, 'G': -2, 'H': 0, 'I': -3, 'K': 1, 'L': -3, 'M': -2, 'N': 0, 'P': -1, 'Q': 2, 'R': 0, 'S': 0, 'T': -1, 'V': -2, 'W': -3, 'X': -1, 'Y': -2, 'Z': 4}, 'F': {'*': -4, 'A': -2, 'B': -3, 'C': -2, 'D': -3, 'E': -3, 'F': 6, 'G': -3, 'H': -1, 'I': 0, 'K': -3, 'L': 0, 'M': 0, 'N': -3, 'P': -4, 'Q': -3, 'R': -3, 'S': -2, 'T': -2, 'V': -1, 'W': 1, 'X': -1, 'Y': 3, 'Z': -3}, 'G': {'*': -4, 'A': 0, 'B': -1, 'C': -3, 'D': -1, 'E': -2, 'F': -3, 'G': 6, 'H': -2, 'I': -4, 'K': -2, 'L': -4, 'M': -3, 'N': 0, 'P': -2, 'Q': -2, 'R': -2, 'S': 0, 'T': -2, 'V': -3, 'W': -2, 'X': -1, 'Y': -3, 'Z': -2}, 'H': {'*': -4, 'A': -2, 'B': 0, 'C': -3, 'D': -1, 'E': 0, 'F': -1, 'G': -2, 'H': 8, 'I': -3, 'K': -1, 'L': -3, 'M': -2, 'N': 1, 'P': -2, 'Q': 0, 'R': 0, 'S': -1, 'T': -2, 'V': -3, 'W': -2, 'X': -1, 'Y': 2, 'Z': 0}, 'I': {'*': -4, 'A': -1, 'B': -3, 'C': -1, 'D': -3, 'E': -3, 'F': 0, 'G': -4, 'H': -3, 'I': 4, 'K': -3, 'L': 2, 'M': 1, 'N': -3, 'P': -3, 'Q': -3, 'R': -3, 'S': -2, 'T': -1, 'V': 3, 'W': -3, 'X': -1, 'Y': -1, 'Z': -3}, 'K': {'*': -4, 'A': -1, 'B': 0, 'C': -3, 'D': -1, 'E': 1, 'F': -3, 'G': -2, 'H': -1, 'I': -3, 'K': 5, 'L': -2, 'M': -1, 'N': 0, 'P': -1, 'Q': 1, 'R': 2, 'S': 0, 'T': -1, 'V': -2, 'W': -3, 'X': -1, 'Y': -2, 'Z': 1}, 'L': {'*': -4, 'A': -1, 'B': -4, 'C': -1, 'D': -4, 'E': -3, 'F': 0, 'G': -4, 'H': -3, 'I': 2, 'K': -2, 'L': 4, 'M': 2, 'N': -3, 'P': -3, 'Q': -2, 'R': -2, 'S': -2, 'T': -1, 'V': 1, 'W': -2, 'X': -1, 'Y': -1, 'Z': -3}, 'M': {'*': -4, 'A': -1, 'B': -3, 'C': -1, 'D': -3, 'E': -2, 'F': 0, 'G': -3, 'H': -2, 'I': 1, 'K': -1, 'L': 2, 'M': 5, 'N': -2, 'P': -2, 'Q': 0, 'R': -1, 'S': -1, 'T': -1, 'V': 1, 'W': -1, 'X': -1, 'Y': -1, 'Z': -1}, 'N': {'*': -4, 'A': -2, 'B': 3, 'C': -3, 'D': 1, 'E': 0, 'F': -3, 'G': 0, 'H': 1, 'I': -3, 'K': 0, 'L': -3, 'M': -2, 'N': 6, 'P': -2, 'Q': 0, 'R': 0, 'S': 1, 'T': 0, 'V': -3, 'W': -4, 'X': -1, 'Y': -2, 'Z': 0}, 'P': {'*': -4, 'A': -1, 'B': -2, 'C': -3, 'D': -1, 'E': -1, 'F': -4, 'G': -2, 'H': -2, 'I': -3, 'K': -1, 'L': -3, 'M': -2, 'N': -2, 'P': 7, 'Q': -1, 'R': -2, 'S': -1, 'T': -1, 'V': -2, 'W': -4, 'X': -2, 'Y': -3, 'Z': -1}, 'Q': {'*': -4, 'A': -1, 'B': 0, 'C': -3, 'D': 0, 'E': 2, 'F': -3, 'G': -2, 'H': 0, 'I': -3, 'K': 1, 'L': -2, 'M': 0, 'N': 0, 'P': -1, 'Q': 5, 'R': 1, 'S': 0, 'T': -1, 'V': -2, 'W': -2, 'X': -1, 'Y': -1, 'Z': 3}, 'R': {'*': -4, 'A': -1, 'B': -1, 'C': -3, 'D': -2, 'E': 0, 'F': -3, 'G': -2, 'H': 0, 'I': -3, 'K': 2, 'L': -2, 'M': -1, 'N': 0, 'P': -2, 'Q': 1, 'R': 5, 'S': -1, 'T': -1, 'V': -3, 'W': -3, 'X': -1, 'Y': -2, 'Z': 0}, 'S': {'*': -4, 'A': 1, 'B': 0, 'C': -1, 'D': 0, 'E': 0, 'F': -2, 'G': 0, 'H': -1, 'I': -2, 'K': 0, 'L': -2, 'M': -1, 'N': 1, 'P': -1, 'Q': 0, 'R': -1, 'S': 4, 'T': 1, 'V': -2, 'W': -3, 'X': 0, 'Y': -2, 'Z': 0}, 'T': {'*': -4, 'A': 0, 'B': -1, 'C': -1, 'D': -1, 'E': -1, 'F': -2, 'G': -2, 'H': -2, 'I': -1, 'K': -1, 'L': -1, 'M': -1, 'N': 0, 'P': -1, 'Q': -1, 'R': -1, 'S': 1, 'T': 5, 'V': 0, 'W': -2, 'X': 0, 'Y': -2, 'Z': -1}, 'V': {'*': -4, 'A': 0, 'B': -3, 'C': -1, 'D': -3, 'E': -2, 'F': -1, 'G': -3, 'H': -3, 'I': 3, 'K': -2, 'L': 1, 'M': 1, 'N': -3, 'P': -2, 'Q': -2, 'R': -3, 'S': -2, 'T': 0, 'V': 4, 'W': -3, 'X': -1, 'Y': -1, 'Z': -2}, 'W': {'*': -4, 'A': -3, 'B': -4, 'C': -2, 'D': -4, 'E': -3, 'F': 1, 'G': -2, 'H': -2, 'I': -3, 'K': -3, 'L': -2, 'M': -1, 'N': -4, 'P': -4, 'Q': -2, 'R': -3, 'S': -3, 'T': -2, 'V': -3, 'W': 11, 'X': -2, 'Y': 2, 'Z': -3}, 'X': {'*': -4, 'A': 0, 'B': -1, 'C': -2, 'D': -1, 'E': -1, 'F': -1, 'G': -1, 'H': -1, 'I': -1, 'K': -1, 'L': -1, 'M': -1, 'N': -1, 'P': -2, 'Q': -1, 'R': -1, 'S': 0, 'T': 0, 'V': -1, 'W': -2, 'X': -1, 'Y': -1, 'Z': -1}, 'Y': {'*': -4, 'A': -2, 'B': -3, 'C': -2, 'D': -3, 'E': -2, 'F': 3, 'G': -3, 'H': 2, 'I': -1, 'K': -2, 'L': -1, 'M': -1, 'N': -2, 'P': -3, 'Q': -1, 'R': -2, 'S': -2, 'T': -2, 'V': -1, 'W': 2, 'X': -1, 'Y': 7, 'Z': -2}, 'Z': {'*': -4, 'A': -1, 'B': 1, 'C': -3, 'D': 1, 'E': 4, 'F': -3, 'G': -2, 'H': 0, 'I': -3, 'K': 1, 'L': -3, 'M': -1, 'N': 0, 'P': -1, 'Q': 3, 'R': 0, 'S': 0, 'T': -1, 'V': -2, 'W': -3, 'X': -1, 'Y': -2, 'Z': 4}}
PAM250 = {'*': {'*': 1, 'A': -8, 'B': -8, 'C': -8, 'D': -8, 'E': -8, 'F': -8, 'G': -8, 'H': -8, 'I': -8, 'K': -8, 'L': -8, 'M': -8, 'N': -8, 'P': -8, 'Q': -8, 'R': -8, 'S': -8, 'T': -8, 'V': -8, 'W': -8, 'X': -8, 'Y': -8, 'Z': -8}, 'A': {'*': -8, 'A': 2, 'B': 0, 'C': -2, 'D': 0, 'E': 0, 'F': -3, 'G': 1, 'H': -1, 'I': -1, 'K': -1, 'L': -2, 'M': -1, 'N': 0, 'P': 1, 'Q': 0, 'R': -2, 'S': 1, 'T': 1, 'V': 0, 'W': -6, 'X': 0, 'Y': -3, 'Z': 0}, 'B': {'*': -8, 'A': 0, 'B': 3, 'C': -4, 'D': 3, 'E': 3, 'F': -4, 'G': 0, 'H': 1, 'I': -2, 'K': 1, 'L': -3, 'M': -2, 'N': 2, 'P': -1, 'Q': 1, 'R': -1, 'S': 0, 'T': 0, 'V': -2, 'W': -5, 'X': -1, 'Y': -3, 'Z': 2}, 'C': {'*': -8, 'A': -2, 'B': -4, 'C': 12, 'D': -5, 'E': -5, 'F': -4, 'G': -3, 'H': -3, 'I': -2, 'K': -5, 'L': -6, 'M': -5, 'N': -4, 'P': -3, 'Q': -5, 'R': -4, 'S': 0, 'T': -2, 'V': -2, 'W': -8, 'X': -3, 'Y': 0, 'Z': -5}, 'D': {'*': -8, 'A': 0, 'B': 3, 'C': -5, 'D': 4, 'E': 3, 'F': -6, 'G': 1, 'H': 1, 'I': -2, 'K': 0, 'L': -4, 'M': -3, 'N': 2, 'P': -1, 'Q': 2, 'R': -1, 'S': 0, 'T': 0, 'V': -2, 'W': -7, 'X': -1, 'Y': -4, 'Z': 3}, 'E': {'*': -8, 'A': 0, 'B': 3, 'C': -5, 'D': 3, 'E': 4, 'F': -5, 'G': 0, 'H': 1, 'I': -2, 'K': 0, 'L': -3, 'M': -2, 'N': 1, 'P': -1, 'Q': 2, 'R': -1, 'S': 0, 'T': 0, 'V': -2, 'W': -7, 'X': -1, 'Y': -4, 'Z': 3}, 'F': {'*': -8, 'A': -3, 'B': -4, 'C': -4, 'D': -6, 'E': -5, 'F': 9, 'G': -5, 'H': -2, 'I': 1, 'K': -5, 'L': 2, 'M': 0, 'N': -3, 'P': -5, 'Q': -5, 'R': -4, 'S': -3, 'T': -3, 'V': -1, 'W': 0, 'X': -2, 'Y': 7, 'Z': -5}, 'G': {'*': -8, 'A': 1, 'B': 0, 'C': -3, 'D': 1, 'E': 0, 'F': -5, 'G': 5, 'H': -2, 'I': -3, 'K': -2, 'L': -4, 'M': -3, 'N': 0, 'P': 0, 'Q': -1, 'R': -3, 'S': 1, 'T': 0, 'V': -1, 'W': -7, 'X': -1, 'Y': -5, 'Z': 0}, 'H': {'*': -8, 'A': -1, 'B': 1, 'C': -3, 'D': 1, 'E': 1, 'F': -2, 'G': -2, 'H': 6, 'I': -2, 'K': 0, 'L': -2, 'M': -2, 'N': 2, 'P': 0, 'Q': 3, 'R': 2, 'S': -1, 'T': -1, 'V': -2, 'W': -3, 'X': -1, 'Y': 0, 'Z': 2}, 'I': {'*': -8, 'A': -1, 'B': -2, 'C': -2, 'D': -2, 'E': -2, 'F': 1, 'G': -3, 'H': -2, 'I': 5, 'K': -2, 'L': 2, 'M': 2, 'N': -2, 'P': -2, 'Q': -2, 'R': -2, 'S': -1, 'T': 0, 'V': 4, 'W': -5, 'X': -1, 'Y': -1, 'Z': -2}, 'K': {'*': -8, 'A': -1, 'B': 1, 'C': -5, 'D': 0, 'E': 0, 'F': -5, 'G': -2, 'H': 0, 'I': -2, 'K': 5, 'L': -3, 'M': 0, 'N': 1, 'P': -1, 'Q': 1, 'R': 3, 'S': 0, 'T': 0, 'V': -2, 'W': -3, 'X': -1, 'Y': -4, 'Z': 0}, 'L': {'*': -8, 'A': -2, 'B': -3, 'C': -6, 'D': -4, 'E': -3, 'F': 2, 'G': -4, 'H': -2, 'I': 2, 'K': -3, 'L': 6, 'M': 4, 'N': -3, 'P': -3, 'Q': -2, 'R': -3, 'S': -3, 'T': -2, 'V': 2, 'W': -2, 'X': -1, 'Y': -1, 'Z': -3}, 'M': {'*': -8, 'A': -1, 'B': -2, 'C': -5, 'D': -3, 'E': -2, 'F': 0, 'G': -3, 'H': -2, 'I': 2, 'K': 0, 'L': 4, 'M': 6, 'N': -2, 'P': -2, 'Q': -1, 'R': 0, 'S': -2, 'T': -1, 'V': 2, 'W': -4, 'X': -1, 'Y': -2, 'Z': -2}, 'N': {'*': -8, 'A': 0, 'B': 2, 'C': -4, 'D': 2, 'E': 1, 'F': -3, 'G': 0, 'H': 2, 'I': -2, 'K': 1, 'L': -3, 'M': -2, 'N': 2, 'P': 0, 'Q': 1, 'R': 0, 'S': 1, 'T': 0, 'V': -2, 'W': -4, 'X': 0, 'Y': -2, 'Z': 1}, 'P': {'*': -8, 'A': 1, 'B': -1, 'C': -3, 'D': -1, 'E': -1, 'F': -5, 'G': 0, 'H': 0, 'I': -2, 'K': -1, 'L': -3, 'M': -2, 'N': 0, 'P': 6, 'Q': 0, 'R': 0, 'S': 1, 'T': 0, 'V': -1, 'W': -6, 'X': -1, 'Y': -5, 'Z': 0}, 'Q': {'*': -8, 'A': 0, 'B': 1, 'C': -5, 'D': 2, 'E': 2, 'F': -5, 'G': -1, 'H': 3, 'I': -2, 'K': 1, 'L': -2, 'M': -1, 'N': 1, 'P': 0, 'Q': 4, 'R': 1, 'S': -1, 'T': -1, 'V': -2, 'W': -5, 'X': -1, 'Y': -4, 'Z': 3}, 'R': {'*': -8, 'A': -2, 'B': -1, 'C': -4, 'D': -1, 'E': -1, 'F': -4, 'G': -3, 'H': 2, 'I': -2, 'K': 3, 'L': -3, 'M': 0, 'N': 0, 'P': 0, 'Q': 1, 'R': 6, 'S': 0, 'T': -1, 'V': -2, 'W': 2, 'X': -1, 'Y': -4, 'Z': 0}, 'S': {'*': -8, 'A': 1, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': -3, 'G': 1, 'H': -1, 'I': -1, 'K': 0, 'L': -3, 'M': -2, 'N': 1, 'P': 1, 'Q': -1, 'R': 0, 'S': 2, 'T': 1, 'V': -1, 'W': -2, 'X': 0, 'Y': -3, 'Z': 0}, 'T': {'*': -8, 'A': 1, 'B': 0, 'C': -2, 'D': 0, 'E': 0, 'F': -3, 'G': 0, 'H': -1, 'I': 0, 'K': 0, 'L': -2, 'M': -1, 'N': 0, 'P': 0, 'Q': -1, 'R': -1, 'S': 1, 'T': 3, 'V': 0, 'W': -5, 'X': 0, 'Y': -3, 'Z': -1}, 'V': {'*': -8, 'A': 0, 'B': -2, 'C': -2, 'D': -2, 'E': -2, 'F': -1, 'G': -1, 'H': -2, 'I': 4, 'K': -2, 'L': 2, 'M': 2, 'N': -2, 'P': -1, 'Q': -2, 'R': -2, 'S': -1, 'T': 0, 'V': 4, 'W': -6, 'X': -1, 'Y': -2, 'Z': -2}, 'W': {'*': -8, 'A': -6, 'B': -5, 'C': -8, 'D': -7, 'E': -7, 'F': 0, 'G': -7, 'H': -3, 'I': -5, 'K': -3, 'L': -2, 'M': -4, 'N': -4, 'P': -6, 'Q': -5, 'R': 2, 'S': -2, 'T': -5, 'V': -6, 'W': 17, 'X': -4, 'Y': 0, 'Z': -6}, 'X': {'*': -8, 'A': 0, 'B': -1, 'C': -3, 'D': -1, 'E': -1, 'F': -2, 'G': -1, 'H': -1, 'I': -1, 'K': -1, 'L': -1, 'M': -1, 'N': 0, 'P': -1, 'Q': -1, 'R': -1, 'S': 0, 'T': 0, 'V': -1, 'W': -4, 'X': -1, 'Y': -2, 'Z': -1}, 'Y': {'*': -8, 'A': -3, 'B': -3, 'C': 0, 'D': -4, 'E': -4, 'F': 7, 'G': -5, 'H': 0, 'I': -1, 'K': -4, 'L': -1, 'M': -2, 'N': -2, 'P': -5, 'Q': -4, 'R': -4, 'S': -3, 'T': -3, 'V': -2, 'W': 0, 'X': -2, 'Y': 10, 'Z': -4}, 'Z': {'*': -8, 'A': 0, 'B': 2, 'C': -5, 'D': 3, 'E': 3, 'F': -5, 'G': 0, 'H': 2, 'I': -2, 'K': 0, 'L': -3, 'M': -2, 'N': 1, 'P': 0, 'Q': 3, 'R': 0, 'S': 0, 'T': -1, 'V': -2, 'W': -6, 'X': -1, 'Y': -4, 'Z': 3}}


def parse_FASTA(filepaths):
    result = {}
    if type(filepaths) == list and len(filepaths) == 2:
        for filepath in filepaths:
            string = []
            with open(filepath, "r") as file:
                for line in file:
                    string.append(line)
            string = ''.join(string)
            string = string.split(">")[1].strip()
            seq_name = string.split("\n")[0]
            seq = "".join(string.split("\n")[1:])
            result[seq_name] = seq

    elif type(filepaths) == str:
        strings = []
        with open(filepaths, "r") as file:
            for line in file:
                strings.append(line)
            strings = ''.join(strings)
            strings = strings.split(">")
            seq_1_name = strings[1].split("\n")[0]
            seq_2_name = strings[2].split("\n")[0]
            seq_1 = "".join(strings[1].split("\n")[1:])
            seq_2 = "".join(strings[2].split("\n")[1:])

            result[seq_1_name] = seq_1
            result[seq_2_name] = seq_2
    else:
        raise TypeError("Failed to parse FASTA")

    return result


class Aligner:
    def __init__(self, sequences, seq_type="nucleotide", scoring_matrix="BLOSUM62",
                 constant_gap=None, linear_gap=None, gap_opening=None, gap_extension=None, mismatch=None, match=None,
                 to_CIGAR=False, to_visuals=True, to_file=None):

        self.seq_1, self.seq_2 = sequences.values()
        self.seq_1_name, self.seq_2_name = sequences.keys()
        self.seq_type = seq_type
        if self.seq_type == "nucleic":
            self.scoring_matrix = None
        else: self.scoring_matrix = scoring_matrix

        self.constant_gap = -5 if not constant_gap else constant_gap
        self.linear_gap = -5 if not linear_gap else linear_gap
        self.gap_opening = -11 if not gap_opening else gap_opening
        self.gap_extension = -1 if not gap_extension else gap_extension
        self.mismatch = -1 if not mismatch else mismatch
        self.match = 2 if not match else match
        self.to_C = to_CIGAR
        self.to_visuals = to_visuals if not to_file else False
        self.to_file = to_file



    def global_linear_align(self):
        s1 = self.seq_1
        s2 = self.seq_2
        gap = self.linear_gap
        rows = len(s1) + 1
        cols = len(s2) + 1

        if self.scoring_matrix == "BLOSUM62":
            scr_mat = BLOSUM62
        elif self.scoring_matrix == "PAM250":
            scr_mat = PAM250
        else:
            scr_mat = None

        score_grid = np.zeros((rows, cols))
        if scr_mat:
            for r in range(1, rows):
                char1 = s1[r - 1]
                for c in range(1, cols):
                    score_grid[r, c] = scr_mat[char1][s2[c - 1]]
        else:
            arr1 = np.array(list(s1))
            arr2 = np.array(list(s2))
            match_mask = arr1[:, None] == arr2[None, :]
            score_grid[1:, 1:] = np.where(match_mask, self.match, self.mismatch)

        @njit
        def compute_matrices(score_grid, gap, rows, cols):
            matrix = np.empty((rows, cols))

            matrix[0, :] = [i * gap for i in range(len(matrix[0]))]
            matrix[:, 0] = [i * gap for i in range(len(matrix[:, 0]))]

            for row in range(1, rows):
                for col in range(1, cols):
                    score = score_grid[row, col]

                    matrix[row][col] = max(matrix[row - 1, col - 1] + score,
                                           matrix[row - 1, col] + gap,
                                           matrix[row, col - 1] + gap)
            return matrix
        matrix = compute_matrices(score_grid, gap, rows, cols)
        final_score = matrix[len(matrix) - 1, len(matrix[0]) - 1]

        i = rows - 1
        j = cols - 1
        align1 = []
        align2 = []
        matching = []

        while i > 0 or j > 0:
            current_score = matrix[i, j]

            if i > 0 and j > 0:
                score = score_grid[i, j]
                if current_score == matrix[i - 1, j - 1] + score:
                    align1.append(s1[i - 1])
                    align2.append(s2[j - 1])

                    matching.append("|" if s1[i - 1] == s2[j - 1] else ".")

                    i -= 1
                    j -= 1

                    continue

            if i > 0 and current_score == matrix[i - 1, j] + gap:
                align1.append(s1[i - 1])
                align2.append("-")
                i -= 1
                matching.append("-")
                continue

            if j > 0 and current_score == matrix[i, j - 1] + gap:
                align1.append("-")
                align2.append(s2[j - 1])
                j -= 1
                matching.append("-")
        align1 = "".join(align1[::-1])
        align2 = "".join(align2[::-1])
        matching = "".join(matching[::-1])
        return align1, matching, align2, final_score

    def global_constant_align(self):
        s1 = self.seq_1
        s2 = self.seq_2
        gap = self.constant_gap
        rows = len(s1) + 1
        cols = len(s2) + 1
        if self.scoring_matrix == "BLOSUM62":
            scr_mat = BLOSUM62
        elif self.scoring_matrix == "PAM250":
            scr_mat = PAM250
        else:
            scr_mat = None

        score_grid = np.zeros((rows, cols))
        if scr_mat:
            for r in range(1, rows):
                char1 = s1[r - 1]
                for c in range(1, cols):
                    score_grid[r, c] = scr_mat[char1][s2[c - 1]]
        else:
            arr1 = np.array(list(s1))
            arr2 = np.array(list(s2))
            match_mask = arr1[:, None] == arr2[None, :]
            score_grid[1:, 1:] = np.where(match_mask, self.match, self.mismatch)

        @njit
        def compute_matrices(score_grid, gap, rows, cols):
            M = np.full((rows, cols), -np.inf)
            Gs1 = np.full((rows, cols), -np.inf)
            Gs2 = np.full((rows, cols), -np.inf)

            M[0, 0] = 0
            for j in range(1, cols):
                Gs1[0, j] = gap
            for i in range(1, rows):
                Gs2[i, 0] = gap

            for row in range(1, rows):
                for col in range(1, cols):
                    score = score_grid[row, col]
                    M[row][col] = score + max(M[row - 1, col - 1],
                                                   Gs1[row - 1, col - 1],
                                                   Gs2[row - 1, col - 1])
                    Gs2[row][col] = max(M[row - 1, col] + gap,
                                        Gs2[row - 1, col],
                                        Gs1[row - 1, col] + gap)
                    Gs1[row][col] = max(M[row, col - 1] + gap,
                                        Gs1[row, col - 1],
                                        Gs2[row, col - 1] + gap)
            return M, Gs1, Gs2

        M, Gs1, Gs2 = compute_matrices(score_grid, gap, rows, cols)
        matrices = ["M", "Gs1", "Gs2"]
        scores = [M[-1][-1], Gs1[-1][-1], Gs2[-1][-1]]
        best_score = max(scores)
        best_matrix = matrices[np.argmax(scores)]

        i = rows - 1
        j = cols - 1

        align1 = []
        align2 = []
        matching = []
        while i > 0 or j > 0:
            if best_matrix == 'M':
                score = score_grid[i, j]

                align1.append(s1[i - 1])
                align2.append(s2[j - 1])
                matching.append("|" if s1[i - 1] == s2[j - 1] else ".")

                if M[i, j] == M[i - 1, j - 1] + score:
                    best_matrix = 'M'
                elif M[i, j] == Gs1[i - 1, j - 1] + score:
                    best_matrix = 'Gs1'
                else:
                    best_matrix = 'Gs2'

                i -= 1
                j -= 1

            elif best_matrix == 'Gs1':
                align1.append("-")
                align2 += s2[j - 1]
                matching.append("-")

                if Gs1[i, j] == M[i, j - 1] + gap:
                    best_matrix = 'M'
                elif Gs1[i, j] == Gs1[i, j - 1]:
                    best_matrix = 'Gs1'
                else:
                    best_matrix = 'Gs2'

                j -= 1

            elif best_matrix == 'Gs2':
                align1.append(s1[i - 1])
                align2.append("-")
                matching.append("-")

                if Gs2[i, j] == M[i - 1, j] + gap:
                    best_matrix = 'M'
                elif Gs2[i, j] == Gs2[i - 1, j]:
                    best_matrix = 'Gs2'
                else:
                    best_matrix = 'Gs1'

                i -= 1
        align1 = "".join(align1[::-1])
        align2 = "".join(align2[::-1])
        matching = "".join(matching[::-1])
        return align1, matching, align2, best_score

    def global_affine_align(self):
        s1 = self.seq_1
        s2 = self.seq_2
        gap_opening = self.gap_opening
        gap_extension = self.gap_extension
        if self.scoring_matrix == "BLOSUM62":
            scr_mat = BLOSUM62
        elif self.scoring_matrix == "PAM250":
            scr_mat = PAM250
        else:
            scr_mat = None

        rows = len(s1) + 1
        cols = len(s2) + 1

        score_grid = np.zeros((rows, cols))
        if scr_mat:
            for r in range(1, rows):
                char1 = s1[r - 1]
                for c in range(1, cols):
                    score_grid[r, c] = scr_mat[char1][s2[c - 1]]
        else:
            arr1 = np.array(list(s1))
            arr2 = np.array(list(s2))
            match_mask = arr1[:, None] == arr2[None, :]
            score_grid[1:, 1:] = np.where(match_mask, self.match, self.mismatch)

        @njit
        def compute_matrices(score_grid, gap_opening, gap_extension, rows, cols):
            M = np.full((rows, cols), -np.inf)
            I = np.full((rows, cols), -np.inf)
            J = np.full((rows, cols), -np.inf)

            M[0, 0] = 0

            for i in range(1, rows):
                I[i, 0] = gap_opening + (i - 1) * gap_extension

            for j in range(1, cols):
                J[0, j] = gap_opening + (j - 1) * gap_extension

            for row in range(1, rows):
                for col in range(1, cols):
                    score = score_grid[row, col]

                    M[row][col] = score + max(M[row - 1, col - 1],
                                             I[row - 1, col - 1],
                                             J[row - 1, col - 1])
                    I[row][col] = max(I[row - 1, col] + gap_extension,
                                      J[row - 1, col] + gap_opening,
                                      M[row - 1, col] + gap_opening)
                    J[row][col] = max(J[row, col - 1] + gap_extension,
                                      I[row, col - 1] + gap_opening,
                                      M[row, col - 1] + gap_opening)
            return M, I, J

        M, I, J = compute_matrices(score_grid, gap_opening, gap_extension, rows, cols)
        matrices = ["M", "I", "J"]
        scores = [M[-1][-1], I[-1][-1], J[-1][-1]]
        best_score = max(scores)
        best_matrix = matrices[np.argmax(scores)]

        i = rows - 1
        j = cols - 1

        align1 = []
        align2 = []
        matching = []
        while i > 0 or j > 0:
            if best_matrix == 'M':
                score = score_grid[i, j]

                align1.append(s1[i - 1])
                align2.append(s2[j - 1])
                matching.append("|" if s1[i - 1] == s2[j - 1] else ".")

                if M[i, j] == M[i - 1, j - 1] + score:
                    best_matrix = 'M'
                elif M[i, j] == I[i - 1, j - 1] + score:
                    best_matrix = 'I'
                else:
                    best_matrix = 'J'

                i -= 1
                j -= 1

            elif best_matrix == 'I':
                align1.append(s1[i - 1])
                align2.append("-")
                matching.append("-")

                if I[i, j] == I[i - 1, j] + gap_extension:
                    best_matrix = 'I'
                elif I[i, j] == M[i - 1, j] + gap_opening:
                    best_matrix = 'M'
                else:
                    best_matrix = 'J'

                i -= 1

            elif best_matrix == 'J':
                align1.append("-")
                align2.append(s2[j - 1])
                matching.append("-")

                if J[i, j] == J[i, j - 1] + gap_extension:
                    best_matrix = 'J'
                elif J[i, j] == M[i, j - 1] + gap_opening:
                    best_matrix = 'M'
                else:
                    best_matrix = 'I'

                j -= 1

        align1 = "".join(align1[::-1])
        align2 = "".join(align2[::-1])
        matching = "".join(matching[::-1])
        return align1, matching, align2, best_score

    def local_linear_align(self):
        s1 = self.seq_1
        s2 = self.seq_2
        gap = self.linear_gap
        rows = len(s1) + 1
        cols = len(s2) + 1

        if self.scoring_matrix == "BLOSUM62":
            scr_mat = BLOSUM62
        elif self.scoring_matrix == "PAM250":
            scr_mat = PAM250
        else:
            scr_mat = None

        score_grid = np.zeros((rows, cols))
        if scr_mat:
            for r in range(1, rows):
                char1 = s1[r - 1]
                for c in range(1, cols):
                    score_grid[r, c] = scr_mat[char1][s2[c - 1]]
        else:
            arr1 = np.array(list(s1))
            arr2 = np.array(list(s2))
            match_mask = arr1[:, None] == arr2[None, :]
            score_grid[1:, 1:] = np.where(match_mask, self.match, self.mismatch)

        @njit
        def compute_matrices(score_grid, gap, rows, cols):
            matrix = np.full((rows, cols), 0, dtype=int)

            for row in range(1, rows):
                for col in range(1, cols):
                    score = score_grid[row, col]

                    matrix[row][col] = max(
                        matrix[row - 1, col - 1] + score,
                        matrix[row - 1, col] + gap,
                        matrix[row, col - 1] + gap,
                        0
                    )
            return matrix

        matrix = compute_matrices(score_grid, gap, rows, cols)
        best_score = np.max(matrix)
        m = np.argmax(matrix)

        i = m // len(matrix[0])
        j = m % len(matrix[0])

        align1 = []
        align2 = []
        matching = []
        while i > 0 or j > 0:
            current_score = matrix[i, j]
            if current_score > 0:
                score = score_grid[i, j]

                way = max(matrix[i - 1, j - 1] + score,
                          matrix[i - 1, j] + gap,
                          matrix[i, j - 1] + gap)

                if way == matrix[i - 1, j - 1] + score:
                    align1.append(s1[i - 1])
                    align2.append(s2[j - 1])
                    matching.append("|" if s1[i - 1] == s2[j - 1] else ".")
                    i -= 1
                    j -= 1

                elif way == matrix[i - 1, j] + gap:
                    align1.append(s1[i - 1])
                    matching.append("-")
                    align2.append("-")
                    i -= 1

                elif way == matrix[i, j - 1] + gap:
                    align2.append(s2[j - 1])
                    matching.append("-")
                    align1.append("-")
                    j -= 1
            else:
                break
        align1 = "".join(align1[::-1])
        align2 = "".join(align2[::-1])
        matching = "".join(matching[::-1])
        return align1, matching, align2, best_score

    def local_affine_align(self):
        s1 = self.seq_1
        s2 = self.seq_2
        gap_opening = self.gap_opening
        gap_extension = self.gap_extension
        if self.scoring_matrix == "BLOSUM62":
            scr_mat = BLOSUM62
        elif self.scoring_matrix == "PAM250":
            scr_mat = PAM250
        else:
            scr_mat = None

        rows = len(s1) + 1
        cols = len(s2) + 1

        score_grid = np.zeros((rows, cols))

        if scr_mat:
            for r in range(1, rows):
                char1 = s1[r - 1]
                for c in range(1, cols):
                    score_grid[r, c] = scr_mat[char1][s2[c - 1]]
        else:
            arr1 = np.array(list(s1))
            arr2 = np.array(list(s2))
            match_mask = arr1[:, None] == arr2[None, :]
            score_grid[1:, 1:] = np.where(match_mask, self.match, self.mismatch)

        @njit
        def compute_matrices(score_grid, gap_opening, gap_extension, rows, cols):
            M = np.full((rows, cols), -np.inf)
            I = np.full((rows, cols), -np.inf)
            J = np.full((rows, cols), -np.inf)

            M[0, 0] = 0
            for i in range(1, rows):
                I[i, 0] = 0
            for j in range(1, cols):
                J[0, j] = 0

            for row in range(1, rows):
                for col in range(1, cols):
                    score = score_grid[row, col]

                    M[row, col] = score + max(M[row - 1, col - 1],
                                              I[row - 1, col - 1],
                                              J[row - 1, col - 1], 0)

                    I[row, col] = max(I[row - 1, col] + gap_extension,
                                      J[row - 1, col] + gap_opening,
                                      M[row - 1, col] + gap_opening, 0)

                    J[row, col] = max(J[row, col - 1] + gap_extension,
                                      I[row, col - 1] + gap_opening,
                                      M[row, col - 1] + gap_opening, 0)

            return [M, I, J]

        M, I, J = matrices = compute_matrices(score_grid, self.gap_opening, self.gap_extension, rows, cols)
        scores = np.max(M), np.max(I), np.max(J)
        best_matrix = matrices[np.argmax(scores)]
        best_score = max(scores)
        m = np.argmax(best_matrix)

        i = m // len(best_matrix[0])
        j = m % len(best_matrix[0])

        matrices = ["M", "I", "J"]
        best_matrix = matrices[np.argmax(scores)]

        align1 = []
        align2 = []
        matching = []
        while i > 0 or j > 0:
            if best_matrix == 'M':
                if M[i][j] == 0:
                    break
                if scr_mat:
                    score = scr_mat[s1[i - 1]][s2[j - 1]]
                else:
                    score = self.match if s1[i - 1] == s2[j - 1] else self.mismatch

                align1.append(s1[i - 1])
                align2.append(s2[j - 1])
                matching.append("|" if s1[i - 1] == s2[j - 1] else ".")

                if M[i][j] == M[i - 1][j - 1] + score:
                    best_matrix = 'M'
                elif M[i][j] == I[i - 1][j - 1] + score:
                    best_matrix = 'I'
                else:
                    best_matrix = 'J'

                i -= 1
                j -= 1

            elif best_matrix == 'I':
                if I[i][j] == 0:
                    break
                align1.append(s1[i - 1])
                align2.append(s2[j - 1])
                matching.append("-")

                if I[i][j] == I[i - 1][j] + gap_extension:
                    best_matrix = 'I'
                elif I[i][j] == M[i - 1][j] + gap_opening:
                    best_matrix = 'M'
                else:
                    best_matrix = 'J'

                i -= 1

            elif best_matrix == 'J':
                if J[i][j] == 0:
                    break
                align1.append(s1[i - 1])
                align2.append(s2[j - 1])
                matching.append("-")

                if J[i][j] == J[i][j - 1] + gap_extension:
                    best_matrix = 'J'
                elif J[i][j] == M[i][j - 1] + gap_opening:
                    best_matrix = 'M'
                else:
                    best_matrix = 'I'

                j -= 1
        align1 = "".join(align1)
        align2 = "".join(align2)
        matching = "".join(matching)
        return align1[::-1], matching[::-1], align2[::-1], best_score

    def visualize_alignment(self, alignment_1, alignment_2, seq_1_name, seq_2_name, score, matching, line_length=120, alignment_type="global"):
        """
        Visualizes sequence alignment with colored matching strings and statistics.
        """
        # ANSI Color Codes
        GREEN = '\033[92m'
        GRAY = '\033[90m'
        RED = '\033[91m'
        RESET = '\033[0m'

        # Calculate lengths
        aln_len = len(alignment_1)
        seq1_len = len(alignment_1.replace("-", ""))
        seq2_len = len(alignment_2.replace("-", ""))

        matches = matching.count("|")
        mismatches = matching.count(".")
        gaps = matching.count("-")

        print(f"=== Alignment Results: {seq_1_name} vs {seq_2_name} ===")
        print(f"Alignment Score : {score}")
        print(f"Alignment Length: {aln_len}")
        if alignment_type == "local":
            seq_1_global_len = f"({len(self.seq_1)})"
            seq_2_global_len = f"({len(self.seq_2)})"
        else:
            seq_1_global_len = ""
            seq_2_global_len = ""
        print(f"Length {seq_1_name[:10]:<10}: {seq1_len}" + f"{seq_1_global_len}")
        print(f"Length {seq_2_name[:10]:<10}: {seq2_len}" + f"{seq_2_global_len}")
        print(f"Matches: {matches}({matches*100 // aln_len}%) | Mismatches: {mismatches}({mismatches*100 // aln_len}%) | Gaps: {gaps}({gaps*100 // aln_len}%)")
        print("=" * 50 + "\n")

        name_pad = max(len(seq_1_name), len(seq_2_name))
        name_pad = min(name_pad, 15)

        for i in range(0, aln_len, line_length):
            chunk_seq1 = alignment_1[i:i + line_length]
            chunk_match = matching[i:i + line_length]
            chunk_seq2 = alignment_2[i:i + line_length]

            colored_match = ""
            for char in chunk_match:
                if char == "|":
                    colored_match += f"{GREEN}{char}{RESET}"
                elif char == ".":
                    colored_match += f"{GRAY}{char}{RESET}"
                elif char == "-":
                    colored_match += f"{RED}{char}{RESET}"
                else:
                    colored_match += char

            print(f"{seq_1_name[:15]:>{name_pad}}  {chunk_seq1}")
            print(f"{'':>{name_pad}}  {colored_match}")
            print(f"{seq_2_name[:15]:>{name_pad}}  {chunk_seq2}\n")

    def to_CIGAR(self, alignment_1, alignment_2, seq_1_name, seq_2_name, score, matching, extended=False):
        aln_len = len(matching)
        CIGAR = ""
        i = 0
        matching += "P"
        while i < aln_len-1:
            match_count = 0
            mismatch_count = 0
            insertion_count = 0
            deletion_count = 0

            while matching[i] == "|":
                match_count += 1
                i += 1

            while matching[i] == ".":
                if extended:
                    mismatch_count += 1
                else:
                    match_count += 1
                i += 1


            while matching[i] == "-":
                if alignment_1[i] == "-":
                    insertion_count += 1
                elif alignment_2[i] == "-":
                    deletion_count += 1
                i += 1


            if match_count:
                char = "=" if extended else "M"
                CIGAR += f"{match_count}{char}"
            if mismatch_count:
                CIGAR += f"{mismatch_count}X"
            if insertion_count:
                CIGAR += f"{insertion_count}I"
            if deletion_count:
                CIGAR += f"{deletion_count}D"
        if not self.to_file:
            print(f"=== Alignment Results: {seq_1_name} vs {seq_2_name} ===")
            print(f"Alignment Score : {score}")
            print(f"Alignment Length: {aln_len}")
            print("CIGAR string:")
            print(CIGAR)
        else:
            return CIGAR

    def output_to_file(self, alignment_1, alignment_2, seq_1_name, seq_2_name, score, matching, alignment_type="global"):
        """
            Writes sequence alignment and statistics to a file.
        """

        aln_len = len(alignment_1)
        seq1_len = len(alignment_1.replace("-", ""))
        seq2_len = len(alignment_2.replace("-", ""))

        matches = matching.count("|")
        mismatches = matching.count(".")
        gaps = matching.count("-")

        name_pad = max(len(seq_1_name), len(seq_2_name))

        with open(self.to_file, "w") as f:
            f.write(f"=== Alignment Results: {seq_1_name} vs {seq_2_name} ===\n")
            f.write(f"Alignment Score : {score}\n")
            f.write(f"Alignment Length: {aln_len}\n")
            if not self.to_C:
                if alignment_type == "local":
                    seq_1_global_len = f"({len(self.seq_1)})"
                    seq_2_global_len = f"({len(self.seq_2)})"
                else:
                    seq_1_global_len = ""
                    seq_2_global_len = ""

                f.write(f"Length {seq_1_name:<{name_pad}}: {seq1_len}{seq_1_global_len}\n")
                f.write(f"Length {seq_2_name:<{name_pad}}: {seq2_len}{seq_2_global_len}\n")
                f.write(
                    f"Matches: {matches}({matches * 100 // aln_len}%) | Mismatches: {mismatches}({mismatches * 100 // aln_len}%) | Gaps: {gaps}({gaps * 100 // aln_len}%)\n")
                f.write("=" * 50 + "\n\n")

                f.write(f"{seq_1_name:>{name_pad}}  {alignment_1}\n")
                f.write(f"{'':>{name_pad}}  {matching}\n")
                f.write(f"{seq_2_name:>{name_pad}}  {alignment_2}\n")
            else:
                f.write("CIGAR string:")
                f.write(self.to_CIGAR(alignment_1, alignment_2, self.seq_1_name, self.seq_2_name, score, matching))

        print(f"Output written to {self.to_file}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="CLI Aligner")
    parser.add_argument("-seq1", "--sequence1", type=str, help="Path to reference sequence FASTA file")
    parser.add_argument("-seq2", "--sequence2", type=str, help="Path to query sequence FASTA file")
    parser.add_argument("-seqs", "--sequences", type=str, help="Path to FASTA file with at least to sequences to align")
    parser.add_argument("-al", "--alignment", type=str, required=True, help="Choose alignment type: global_linear, global_constant, global_affine(Default), local_linear, local_affine")
    parser.add_argument("-lg", "--linear_gap", type=int, help="Set linear gap penalty(Default=-5)")
    parser.add_argument("-cg", "--constant_gap", type=int, help="Set constant gap penalty(Default=-5)")
    parser.add_argument("-og", "--open_gap", type=int, help="Set open gap penalty(Default=-11)")
    parser.add_argument("-eg", "--extend_gap", type=int, help="Set extend gap penalty(Default=-1)")
    parser.add_argument("-m", "--match_score", type=int, help="Set match score for non-matrix alignment(Default=2)")
    parser.add_argument("-mm", "--mismatch_score", type=int, help="Set mismatch score for non-matrix alignment(Default=-1)")
    parser.add_argument("-b", "--use_blosum", action='store_true', help="Use BLOSUM62 matrix")
    parser.add_argument("-pam", "--use_pam250", action='store_true', help="Use PAM250 matrix")
    parser.add_argument("-to_c", "--to_cigar", action='store_true', help="Output in CIGAR string")
    parser.add_argument("-to_v", "--to_visuals", action='store_true', help="Output in matching visuals string")
    parser.add_argument("-to_f", "--to_file", type=str, help="Filepath to write output to")

    group = parser.add_mutually_exclusive_group()
    group.add_argument("-n", "--nucleic", action='store_true', help="Search nucleic acids")
    group.add_argument("-p", "--protein", action='store_true', help="Search proteins")

    args = parser.parse_args()

    if args.use_pam250:
        scoring_matrix = "PAM250"
    elif args.use_blosum:
        scoring_matrix = "BLOSUM62"
    else:
        scoring_matrix = None
    if "local" in args.alignment:
        al_type = "local"
    else:
        al_type = "global"

    if args.sequence1 and args.sequence2:
        seqs = parse_FASTA([args.sequence1, args.sequence2])
    elif args.sequences:
        seqs = parse_FASTA(args.sequences)
    else:
        print("Sequences required")
        seqs = None

    aligner = Aligner(
        sequences=seqs,
        seq_type = "protein" if args.protein else "nucleic",
        scoring_matrix = scoring_matrix,
        constant_gap = args.constant_gap,
        linear_gap = args.linear_gap,
        gap_opening = args.open_gap,
        gap_extension = args.extend_gap,
        mismatch = args.mismatch_score,
        match = args.match_score,
        to_CIGAR = args.to_cigar,
        to_visuals = args.to_visuals,
        to_file = args.to_file
    )

    if args.alignment == "global_linear":
        al1, m, al2, s = aligner.global_linear_align()
    elif args.alignment == "global_constant":
        al1, m, al2, s = aligner.global_constant_align()
    elif args.alignment == "local_affine":
        al1, m, al2, s = aligner.global_affine_align()
    elif args.alignment == "local_linear":
        al1, m, al2, s = aligner.local_linear_align()
    else:
        al1, m, al2, s = aligner.global_affine_align()

    if args.to_cigar and not args.to_file:
        aligner.to_CIGAR(al1, al2, aligner.seq_1_name, aligner.seq_2_name, s, m)
    elif args.to_visuals and not args.to_file:
        aligner.visualize_alignment(al1, al2, aligner.seq_1_name, aligner.seq_2_name, s, m)
    elif args.to_file:
        aligner.output_to_file(al1, al2, aligner.seq_1_name, aligner.seq_2_name, s, m)