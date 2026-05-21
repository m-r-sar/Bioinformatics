import numpy as np

def function(s1, s2):
    match = 0
    mismatch = 1
    gap = 1

    rows = len(s1) + 1
    cols = len(s2) + 1

    matrix = np.zeros((rows, cols), dtype=int)
    matrix[0, :] = [j * gap for j in range(cols)]
    matrix[:, 0] = [i * gap for i in range(rows)]

    count_matrix = np.zeros((rows, cols), dtype=int)
    count_matrix[0, :] = [1 for _ in range(cols)]
    count_matrix[:, 0] = [1 for _ in range(rows)]

    for row in range(1, rows):
        for col in range(1, cols):
            s_ij = match if s1[row - 1] == s2[col - 1] else mismatch

            matrix[row][col] = min(
                matrix[row - 1][col - 1] + s_ij,
                matrix[row - 1][col] + gap,
                matrix[row][col - 1] + gap
            )
            if matrix[row][col] == matrix[row - 1][col - 1] + s_ij:
                count_matrix[row][col] = (count_matrix[row][col] + count_matrix[row - 1][col - 1]) % 134217727
            if matrix[row][col] == matrix[row - 1][col] + gap:
                count_matrix[row][col] = (count_matrix[row][col] + count_matrix[row - 1][col]) % 134217727
            if matrix[row][col] == matrix[row][col - 1] + gap:
                count_matrix[row][col] = (count_matrix[row][col] + count_matrix[row][col - 1]) % 134217727

    return count_matrix[-1][-1]