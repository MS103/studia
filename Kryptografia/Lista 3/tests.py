import sys
from jks import jks

from command_line_parser import CommandLineParser
from openssl import OpenSSL

command_line_parser = CommandLineParser()
parsed_args = command_line_parser.parse_arguments(sys.argv[1:])

key_store = jks.KeyStore.load(parsed_args['keystore_path'], parsed_args['password'])
key = key_store.private_keys['alias_name'].pkey[:32]

num_of_success = 0
msg_to_enc = 'x'
types_of_enc = ['ofb', 'cbc', 'ctr']
if True:
    for enc_type in types_of_enc:
        print('Sprawdzam szyfrowanie i deszyfrowanie dla ', enc_type.upper())
        openssl = OpenSSL(enc_type)
        iv = '0' * 16
        enc_m = openssl.encrypt(msg_to_enc, key, iv)
        dec_m = openssl.decrypt(enc_m, key, iv).rstrip(b'\x00')
        try:
            dec_m = dec_m.decode()
            if_success = msg_to_enc == dec_m
        except UnicodeDecodeError as e:
            print("Wystąpił błąd!", e)
            if_success = 0
        num_of_success += if_success
        print('Sprawdzam czy {a} == {b}. Rezultat to {c}\n'.format(a=msg_to_enc, b=dec_m, c=if_success))
    print('Stosunek sukcesów do prób to {a}/{b}'.format(a=num_of_success, b=len(types_of_enc)))
