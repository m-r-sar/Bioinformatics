import numpy as np

def function(s1, s2, match = -1, mismatch = -10, gap = -2):
    rows = len(s1) + 1
    cols = len(s2) + 1
    matrix = np.zeros((rows, cols))


    matrix[0, :] = [i*gap for i in range(len(matrix[0]))]
    matrix[:, 0] = [i*gap for i in range(len(matrix[:, 0]))]

    for row in range(1, rows):
        for col in range(1, cols):
            s_ij = match if s1[row - 1] == s2[col - 1] else mismatch

            matrix[row][col] = max(matrix[row-1][col-1] + s_ij,
                                    matrix[row-1][col] + gap,
                                    matrix[row][col-1] + gap)

    supersequence = ""
    i = rows - 1
    j = cols - 1

    while i > 0 or j > 0:
        current_score = matrix[i][j]

        if i > 0 and j > 0:
            s_ij = match if s1[i - 1] == s2[j - 1] else mismatch
            if current_score == matrix[i - 1][j - 1] + s_ij:
                supersequence += s1[i - 1]

                i -= 1
                j -= 1
                continue

        if i > 0 and current_score == matrix[i - 1][j] + gap:
            supersequence += s1[i - 1]
            i -= 1
            continue

        if j > 0 and current_score == matrix[i][j - 1] + gap:
            supersequence += s2[j - 1]
            j -= 1

    return supersequence[::-1]
