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
