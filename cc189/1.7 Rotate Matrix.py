def clock_wise_rotate(matrix):
    if len(matrix) == 0 or len(matrix[0]) == 0:
        return
    for i in range(len(matrix)):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    i = 0
    j = len(matrix[0]) - 1
    while i < j:
        for k in range(len(matrix)):
            matrix[k][i], matrix[k][j] = matrix[k][j], matrix[k][i]
        i += 1
        j -= 1


def anti_clock_wise_rotate(matrix):
    if len(matrix) == 0 or len(matrix[0]) == 0:
        return
    for i in range(len(matrix)):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    i = 0
    j = len(matrix) - 1
    while i < j:
        matrix[i], matrix[j] = matrix[j], matrix[i]
        i += 1
        j -= 1


inputs = [[], [[1]], [[1, 2, 3], [4, 5, 6], [7, 8, 9]]]
outputs = [[], [[1]], [[7, 4, 1], [8, 5, 2], [9, 6, 3]]]
for i, value in enumerate(inputs):
    clock_wise_rotate(value)
    assert value == outputs[i]


inputs = [[], [[1]], [[1, 2, 3], [4, 5, 6], [7, 8, 9]]]
outputs2 = [[], [[1]], [[3, 6, 9], [2, 5, 8], [1, 4, 7]]]
for i, value in enumerate(inputs):
    anti_clock_wise_rotate(value)
    assert value == outputs2[i]

