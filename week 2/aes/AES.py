import aes_decryption
import aes_encryption
import aes_tools
import binascii
import array


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
    hex = "140b41b22a29beb4061bda66b6747e14"

    binary_string = binascii.unhexlify(hex)

    key = bytearray(binary_string)
    key = [[key[4 * i + j] for i in range(0, 4)] for j in range(0, 4)]

    plain_text = "mamuka sakhelash"
    plain_text = [[ord(plain_text[4 * i + j]) for i in range(0, 4)] for j in range(0, 4)]

    cipher_text = aes_encrypt(key, plain_text)

    c = ""
    for i in range(0, 4):
        for j in range(0, 4):
            c += format(cipher_text[j][i], 'x')

    print(c)
