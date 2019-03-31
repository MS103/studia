from common import *


def KSA(key, n, t):
    num_key = str2num(key)
    key_length = len(num_key)
    s = list(range(n))
    j = 0
    for i in range(t):
        j = (j + s[i] + num_key[i % key_length]) % n
        swap(s, i, j)
    return s


d = 0
t = n = 256
length = 10
key = 'Wiki'
keystream_list = rc4_mdrop_d(key, n, t, d, KSA, length)
binary = num2hexb(keystream_list)
f = open(r"C:\Users\Latitude\Desktop\Studia - Git_repo\studia\Kryptografia\Lista 2\test.txt", 'w')
f.write(binary)
