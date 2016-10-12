import cbc_tools
import AES


def cbc_encrypt(iv, key, message):
    message = cbc_tools.add_padd(message)

    message_blocks = cbc_tools.get_message_blocks(message)

    cipher_text = iv
    pre_xor_variable = cbc_tools.get_4_by_4_matrix_from_16_bytes(iv)


if __name__ == '__main__':
    message = bytearray([1, 2, 3, 4, 5, 2, 3, 4, 5, 2, 3, 4, 5
                            , 2, 3, 4, 5, 2, 3, 4, 2, 3, 4, 5, 2, 3, 4, 5,
                         5, 2, 3, 4, 5, 2, 3, 4, 5])

    message = cbc_tools.add_padd(message)
    messages = cbc_tools.get_message_blocks(message)

    message = cbc_tools.get_4_by_4_matrix_from_16_bytes(messages[0])
