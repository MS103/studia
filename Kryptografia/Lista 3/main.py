import sys

from random import randint
from jks import jks

from command_line_parser import CommandLineParser
from openssl import OpenSSL


def xor_strings(str1, str2):
    return "".join([chr(ord(a) ^ ord(b)) for a, b in zip(str1, str2)])


def increment_iv(iv):
    iv = bin(int(iv, 2) + 1)[2:]
    return '0' * (16 - len(iv)) + iv


def destinguisher(key, iv, msg_list, enc_msg):
    iv2 = increment_iv(iv)
    encryptor = OpenSSL('cbc')
    for i, m in enumerate(msg_list):
        xored = xor_strings(xor_strings(iv, iv2), m)
        enc_m = encryptor.encrypt(xored, key, iv2)
        if enc_m == enc_msg:
            return i, enc_m


command_line_parser = CommandLineParser()
parsed_args = command_line_parser.parse_arguments(sys.argv[1:])

enc_type = 'cbc'
openssl = OpenSSL(enc_type)
iv = '0' * 16
key_store = jks.KeyStore.load(parsed_args['keystore_path'], parsed_args['password'])
key = key_store.private_keys['alias_name'].pkey[:32]

f = open(parsed_args['input_path'], 'r')
input_ms = [x for x in f]
f = open(r'C:\Users\Latitude\Desktop\output.txt', 'w')

if len(input_ms) == 0:
    raise IOError('Za mało danych wejściowych')
elif len(input_ms) == 2 :
    msg_list = [x[:16] for x in input_ms]
    random_msg = msg_list[randint(0, 1)]

    enc_m = openssl.encrypt(random_msg, key, iv)
    f.write(str(enc_m)+'\n')
    print('Szyfruje {a} w {b}'.format(a=random_msg, b=enc_m))

    if enc_type == 'cbc':
        print('\n\nProgram uruchamia destinguisher\n\n')
        dec_m, cipher = destinguisher(key, iv, msg_list, enc_m)
        print('{a} zaszyfrowano w {b}'.format(a=msg_list[dec_m], b=cipher))
else:

    for m in input_ms:
        enc_m = openssl.encrypt(m, key, iv)
        f.write(str(enc_m)+'\n')
        print('Szyfruje {a} w {b}'.format(a=m, b=enc_m))

