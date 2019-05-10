import numpy as np
from math import gcd as bltin_gcd


# FUNKCJE POMOCNICZE

def coprime2(a, b):
    return bltin_gcd(a, b) == 1


def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)


def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m


# MERKLE-HELLMAN PUZZLE

def gen_keys(n):
    w = []
    s = 0
    for i in range(n):
        w.append(np.random.randint(s + 1, np.ceil(1.2 * (s + 1))))
        s = sum(w)

    q = np.random.randint(s + 1, np.ceil(1.2 * (s + 1)))
    r = q
    while not coprime2(q, r):
        r = np.random.randint(0, q + 1)
    beta = []
    for j in range(n):
        beta.append(r * w[j] % q)
    if if_print:
        print('Public key: ', beta)
        print('Private key: ', (w, q, r))
    return beta, w, q, r


def enc(m, beta):
    c = 0
    for i in range(len(m)):
        c += m[i] * beta[i]
    if if_print:
        print("Ciphertext is {}".format(c))
    return c


def dec(c, w, q, r, n):
    s = modinv(r, q)
    c_p = (c * s) % q
    m_p = [None] * n
    for j in range(n):
        i = n - j - 1
        m_p[i] = int(w[i] <= c_p)
        c_p -= w[i] * m_p[i]
    if if_print:
        print('Odkodowana wiaddomość {}'.format(m_p))
    return m_p


# KOD WŁAŚCIWY
global if_print
if_print = False
n = 10

beta, w, q, r = gen_keys(n)
m = list(np.random.randint(0, 2, n))
c = enc(m, beta)
m_p = dec(c, w, q, r, n)
print(
    'Wiadomość przed zakodowaniem: {m}\n'
    'Wiadomość odszyfrowana:       {m_p}\n'
    'Czy eksperyment się udał?     {result}'.format(m=m,
                                                    m_p=m_p,
                                                    result=m == m_p))
