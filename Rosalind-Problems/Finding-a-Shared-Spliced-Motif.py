def function(s1, s2):
    matrix = [[0 for i in range(len(s2)+1)] for _ in range(len(s1)+1)]
    result = ""
    for row in range(1, len(matrix)):
        for col in range(1, len(matrix[row])):
            if s1[row-1] == s2[col-1]:
                matrix[row][col] = matrix[row-1][col-1] + 1
            else:
                matrix[row][col] = max([matrix[row][col-1],matrix[row-1][col]])

    row = len(matrix)-1
    col = len(matrix[0])-1
    while matrix[row][col] != 0:
        if s1[row-1] == s2[col-1]:
            result += s1[row-1]
            row -= 1
            col -= 1
        else:
            if matrix[row-1][col] >= matrix[row][col-1]:
                row-=1
            else:
                col-=1

    return result[::-1]
