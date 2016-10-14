import cbc_tools
import AES


def cbc_encrypt(iv, key, message_text):
    plain_text = cbc_tools.add_padd(message_text)

    message_blocks = cbc_tools.get_message_blocks(plain_text)

    cbc_xor_variable = iv

    cipher_text = iv

    for message_block in message_blocks:
        m = cbc_tools.xor_16_bytes(message_block, cbc_xor_variable)

        cipher_text_matrix = AES.aes_encrypt(key, cbc_tools.get_4_by_4_matrix_from_16_bytes(m))
        cipher_text_block = cbc_tools.get_16byte_array_from_4by4(cipher_text_matrix)
        cipher_text += cipher_text_block
        cbc_xor_variable = cipher_text_block

    return cipher_text

if __name__ == '__main__':
    message = bytearray([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])

    print(len(message))
    message = cbc_tools.add_padd(message)
    print(message)
    messages = cbc_tools.get_message_blocks(message)

    print(messages)

    message = cbc_tools.get_4_by_4_matrix_from_16_bytes(messages[0])

    print(message)

    print(cbc_tools.get_16byte_array_from_4by4(message))