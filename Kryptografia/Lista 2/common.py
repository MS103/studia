import numpy as np


def PRGA(S, n):
    i = 0
    j = 0
    while True:
        i = (i + 1) % n
        j = (j + S[i]) % n

        S[i], S[j] = S[j], S[i]
        K = S[(S[i] + S[j]) % n]
        yield K


def rc4(key, n, t, ksa, length):
    s = ksa(key, n, t)
    keystream = PRGA(s, n)
    return [next(keystream) for i in range(length)]


def rc4_drop_d(key, n, t, d, ksa_alg, length):
    stream = num2hex(rc4(key, n, t, ksa_alg, length))
    return stream[d:]


def rc4_mdrop_d(key, n, t, d, ksa_alg, length):
    stream = rc4(key, n, t, ksa_alg, length)
    return stream[slice(0, len(stream) + 1, d + 1)]


def swap(l, i, j):
    l[i], l[j] = l[j], l[i]


def str2num(l):
    return [ord(x) for x in l]


def str2bin(key):
    return ''.join(format(ord(x), '08b') for x in key)


def num2bin(l):
    return ''.join(format(x, '08b') for x in l)


def num2hex(l):
    return ''.join([format(x, '02X') for x in l])


def num2hexb(l):
    return ''.join([format(x, '08X') + '\n' for x in l])
