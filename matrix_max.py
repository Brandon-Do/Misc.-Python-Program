def matrix_max(ROC):

    max = 0
    row_prod = 1
    col_prod = 1

    for i in range(len(ROC)):
        for k in range(len(ROC)):
            row_prod *= ROC[i][k]
            col_prod *= ROC[k][i]

        if row_prod > max:
            max = row_prod
        if col_prod > max:
            max = col_prod

        row_prod = 1
        col_prod = 1

    return max

rows = [[1, 8, 3],
       [2, 9, 4],
       [6, 7, 5]]

print(matrix_max(rows))