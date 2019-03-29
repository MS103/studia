from common import *
import numpy as np


def KSARS(key, n, t):
    bit_key = str2bin(key)
    key_length = len(bit_key)
    s = list(range(n))
    for r in range(t):
        top = []
        bottom = []
        for i in range(n):
            temp = (r * n + i) % key_length
            if bit_key[temp] == '0':
                top.append(s[i])
            else:
                bottom.append(s[i])
        s = top + bottom
    return s


d = 1
n = 256
t = int(round(2*n*np.log(n)))
length = (10**6)*4
key = 'hi i am john and this is a random text with no periods or capitals or commas this is just simply a random ' \
      'text with no hard words that many find challenging to type in due to the unusual order of the letters so i ' \
      'thought id just keep it easy thought thought thought thought thats a easy word to type depending on youre your ' \
      'highest WPM rank'
keystream_list = rc4_mdrop_d(key, n, t, d, KSARS)
f = open(r"C:\Users\Latitude\Desktop\Studia - Git_repo\studia\Kryptografia\Lista 2\diehard\test.txt", 'w')
f.write(keystream_list)
