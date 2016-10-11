import tools

"""
    This function takes 4X4 bytes matrix, and substitutes
    each byte by S-boxes.
"""


def bytes_ubstitution(byte_matrix):
    for i in range(0, 4):
        for j in range(0, 4):
            byte_matrix[i][j] = tools.s_box[byte_matrix[i][j]]

    return byte_matrix


''' This function takes 4X4 bytes matrix, and shifts
    the rows by row num: 0th row by 0, first by 1 and etc.
'''


def shift_row(byte_matrix):
    for i in range(1, 4):
        for j in range(0, i):
            keep = byte_matrix[i][0]
            byte_matrix[i].pop(0)
            byte_matrix[i].append(keep)

    return byte_matrix


def get_column(byte_matrix, col):
    result = []

    for i in range(0, 4):
        result.append(byte_matrix[i][col])

    return result


def mix_columns(byte_matrix):
    for i in range(0, 4):
        column = get_column(byte_matrix, i)

        column = tools.matrix_multiply_vector(tools.mix_columns_matrix, column)

        for j in range(0, 4):
            byte_matrix[j][i] = column[j]

    return byte_matrix


if __name__ == '__main__':
    pass
