import aes_decryption
import aes_encryption
import aes_tools


def aes_encrypt(base_key, text):
    keys = aes_tools.key_expansion(base_key)

    for i in range(0, 10):
        text = aes_tools.xor_4_by_4(keys[i], text)
        text = aes_encryption.bytes_ubstitution(text)
        text = aes_encryption.shift_row(text)

        if i != 9:
            text = aes_encryption.mix_columns(text)

    text = aes_tools.xor_4_by_4(keys[10], text)

    return text


def aes_decrypt(base_key, cipher_text):

    keys = aes_tools.key_expansion(base_key)

    cipher_text = aes_tools.xor_4_by_4(keys[10], cipher_text)

    for i in range(9, -1, -1):

        if i != 9:
            cipher_text = aes_decryption.mix_columns(cipher_text)

        cipher_text = aes_decryption.shift_row(cipher_text)
        cipher_text = aes_decryption.bytes_ubstitution(cipher_text)
        cipher_text = aes_tools.xor_4_by_4(keys[i], cipher_text)

    return cipher_text


if __name__ == '__main__':
    key = [[0x54, 0x68, 0x61, 0x74],
           [0x73, 0x20, 0x6d, 0x79],
           [0x20, 0x4b, 0x75, 0x6e],
           [0x67, 0x20, 0x46, 0x75]]

    plain = [[92, 23, 12, 4],
             [27, 52, 3, 123],
             [93, 5, 0x75, 121],
             [128, 21, 45, 44]]

    print(plain)

    plain = aes_encrypt(key, plain)
    plain = aes_decrypt(key, plain)

    print(plain)
