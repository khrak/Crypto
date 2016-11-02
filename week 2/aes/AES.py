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
    key_st = "54 68 61 74 73 20 6D 79 20 4B 75 6E 67 20 46 75".split(" ")

    key = [int(st, 16) for st in key_st]

    keys = aes_tools.key_expansion(key)

    for k in keys:
        st = ""
        for ks in k:
            for bt in ks:
                st += " " + hex(bt)[2:]
        print(st)
