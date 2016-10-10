import binascii


def get_val(hex_byte):
    return int(hex_byte, 16)


def get_char(hex_byte):
    print(hex_byte + " should be two bytes")
    a = hex_byte[0]
    b = hex_byte[1]

    rest = get_val(a)
    rest = rest * 16 + get_val(b)

    return chr(rest)


def get_m(hex_text):
    rest = ''

    i = 0

    print(hex_text + " should be sliced")

    while i < 10:
        rest += get_char(hex_text[i: i + 2])
        i += 2

    return rest


with open('cipher_texts.txt', 'r') as myfile:
    content = myfile.read()
    data = content.split('\n')

copher_text = data[0]
data.pop(0)

c1 = data[0]
c2 = data[1]

m1_xor_m2 = ''

min_length = min(len(c1), len(c2))

for i in range(0, min_length):
    m1_xor_m2 += '%x' % (int(c1[i], 16) ^ int(c2[i], 16))

print(m1_xor_m2)

dees = binascii.hexlify(b' the ')

for i in range(0, min_length - 11):
    substr = m1_xor_m2[i: i + 10]
    print(substr + " is substr")
    mb = '%x' % (int(dees, 16) ^ int(substr, 16))
    print(mb)
    print(get_m(mb) + " for " + str(i))
