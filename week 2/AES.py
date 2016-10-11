import aes_decryption
import aes_encryption
import tools


def aes_encrypt(base_key, text):
    keys = tools.key_expansion(base_key)

    for i in range(0, 10):
        text = tools.xor_4_by_4(keys[i], text)
        text = aes_encryption.bytes_ubstitution(text)
        text = aes_encryption.shift_row(text)

        if i != 9:
            text = aes_encryption.mix_columns(text)

    text = tools.xor_4_by_4(keys[10], text)

    return text


def aes_decrypt(base_key, cipher_text):
    keys = tools.key_expansion(base_key)

    cipher_text = tools.xor_4_by_4(keys[10], cipher_text)

    for i in range(9, -1, -1):
        if i != 9:
            cipher_text = aes_decryption.mix_columns(cipher_text)

        cipher_text = aes_encryption.shift_row(cipher_text)
        cipher_text = aes_decryption.bytes_ubstitution(cipher_text)
        cipher_text = tools.xor_4_by_4(keys[i], cipher_text)

    return cipher_text


if __name__ == '__main__':
    key = [[0x54, 0x68, 0x61, 0x74],
           [0x73, 0x20, 0x6d, 0x79],
           [0x20, 0x4b, 0x75, 0x6e],
           [0x67, 0x20, 0x46, 0x75]]

    # substitution matrix before
    plain = [[0x00, 0x3c, 0x6e, 0x47],
             [0x1f, 0x4e, 0x22, 0x74],
             [0x0e, 0x08, 0x1b, 0x31],
             [0x54, 0x59, 0x0b, 0x1a]]

    plain = aes_encryption.bytes_ubstitution(plain)
    plain = aes_encryption.shift_row(plain)
    plain = aes_encryption.mix_columns(plain)

    for mt in plain:
        print(mt)
