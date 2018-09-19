def zero_matrix(matrix):
    if len(matrix) == 0 or len(matrix[0]) == 0:
        return
    origin_zero = matrix[0][0] == 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0
    for i in range(1, len(matrix)):
        if matrix[i][0] == 0:
            for j in range(1, len(matrix[0])):
                matrix[i][j] = 0

    for j in range(1, len(matrix[0])):
        if matrix[0][j] == 0:
            for i in range(1, len(matrix)):
                matrix[i][j] = 0

    if origin_zero:
        for i in range(1, len(matrix)):
            matrix[i][0] = 0
        for j in range(1, len(matrix[0])):
            matrix[0][j] = 0


inputs = [[], [[]], [[1]], [[1, 2, 0], [0, 1, 1]], [[1, 1, 1], [0, 1, 1], [1, 0, 1]]]
for value in inputs:
    zero_matrix(value)
    print(value)


