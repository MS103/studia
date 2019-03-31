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
t = int(round(2 * n * np.log(n)))
length = 10
key = 'Wiki'
keystream_list = rc4_mdrop_d(key, n, t, d, KSARS, length)
binary = num2hexb(keystream_list)
f = open(r"C:\Users\Latitude\Desktop\Studia - Git_repo\studia\Kryptografia\Lista 2\test.txt", 'w')
f.write(binary)
