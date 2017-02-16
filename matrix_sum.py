def matrix_sum(ROC):
    sum = 0
    min = 0
    for i in range(len(ROC)):
        for k in range(len(ROC)):
            sum += ROC[k][i]
        if sum < min or min == 0:
            min = sum
        sum = 0

    return min

rows = [[1, 2, 3],
       [9, 9, 6],
       [9, 8, 9]]

print(matrix_sum(rows))