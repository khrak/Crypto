def mult(a, b):
    p = 0

    while b != 0:

        if b % 2 == 1:
            p ^= a

        if a >= 128:
            a = (a << 1) ^ 0x11b
        else:
            a <<= 1

        b >>= 1

    return p


def xor_4_by_4(A, B):
    result = [[0] * 4] * 4

    for i in range(0, 4):
        for j in range(0, 4):
            result[i][j] = A[i][j] ^ B[i][j]

    return result


def vector_multiple(row, v):
    result = 0

    for i in range(0, len(v)):
        result ^= mult(row[i], v[i])

    return result


def matrix_multiply_vector(m, v):
    result = []

    for row in m:
        result.append(vector_multiple(row, v))

    return result
