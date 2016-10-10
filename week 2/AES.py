import aes_decryption
import aes_encryption
import tools

key = [[0x54, 0x68, 0x61, 0x74],
       [0x73, 0x20, 0x6d, 0x79],
       [0x20, 0x4b, 0x75, 0x6e],
       [0x67, 0x20, 0x46, 0x75]]

plain = [[0x54, 0x68, 0x61, 0x74],
         [0x73, 0x20, 0x6d, 0x79],
         [0x20, 0x4b, 0x75, 0x6e],
         [0x67, 0x20, 0x46, 0x75]]

keys = aes_encryption.key_expansion(key)


for i in range(0, 10):
    plain = tools.xor_4_by_4(keys[i], plain)
    plain = aes_encryption.bytes_ubstitution(plain)
    plain = aes_encryption.shift_row(plain)

    if i != 9:
        plain = aes_encryption.mix_columns(plain)

    print(str(plain) + " is plaintext")

plain = tools.xor_4_by_4(keys[10], plain)

print(plain)
