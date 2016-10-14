import cbc_tools
import AES


def cbc_encrypt(iv, key, message_text):
    plain_text = cbc_tools.add_padd(message_text)

    message_blocks = cbc_tools.get_message_blocks(plain_text)

    cbc_xor_variable = iv

    cipher_text = iv

    for message_block in message_blocks:
        m = cbc_tools.xor_16_bytes(message_block, cbc_xor_variable)

        cipher_text_matrix = AES.aes_encrypt(cbc_tools.get_4_by_4_matrix_from_16_bytes(key),
                                             cbc_tools.get_4_by_4_matrix_from_16_bytes(m))
        cipher_text_block = cbc_tools.get_16byte_array_from_4by4(cipher_text_matrix)
        cipher_text += cipher_text_block
        cbc_xor_variable = cipher_text_block

    return cipher_text

if __name__ == '__main__':

    iv = "4ca00ff4c898d61e1edbf1800618fb28"
    key = "144288afaa485658c611b7f2e574756d"

    message = "I am cbc crypto guy!"

    iv = bytearray.fromhex(iv)
    iv = [iv[i] for i in range(0, len(iv))]

    key = bytearray.fromhex(key)
    key = [key[i] for i in range(0, len(key))]

    message = message.encode()
    message = [message[i] for i in range(0, len(message))]

    cipher_text = cbc_encrypt(iv, key, message)

    print(cipher_text)
