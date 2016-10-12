def add_padd(message):
    size = len(message)
    remaining = 16 - (size % 16)

    message += bytearray([remaining] * remaining)

    return message


def get_message_blocks(message):
    i = 0
    result = []

    while i < len(message):
        result.append(message[i: i + 16])
        i += 16

    return result


def xor_16_bytes(bytes_a, bytes_b):
    result = [bytes_a[i] ^ bytes_b[i] for i in range(0, 16)]
    return result


def get_4_by_4_matrix_from_16_bytes(bytes_16):

    result = [[bytes_16[i * 4 + j] for j in range(0, 4)] for i in range(0, 4)]

    return result
