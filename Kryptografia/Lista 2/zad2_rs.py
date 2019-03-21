def KSARS(key, n, t):
    k = []
    for ke in key:
        k += list("{0:b}".format(ke))
    key_length = len(k)
    S = list(range(n))
    for r in range(t + 1):
        top = []
        bottom = []
        for i in range(n + 1):
            temp = (r * n + i) % key_length
            if k[temp] == '0':
                top.append(i)
            else:
                bottom.append(i)
        S = top + bottom
    return S


def PRGA(S, n):
    i = 0
    j = 0
    while True:
        i = (i + 1) % n
        j = (j + S[i]) % n

        S[i], S[j] = S[j], S[i]
        K = S[(S[i] + S[j]) % n]
        yield K


def get_keystream(key, n, t):
    ''' Takes the encryption key to get the keystream using PRGA
        return object is a generator
    '''
    S = KSARS(key, n, t)
    return PRGA(S, n)


# def encrypt_logic(key, text, n, t):
#     key = [ord(c) for c in key]
#     keystream = get_keystream(key, n, t)
#
#     output = []
#     for c in text:
#         output.append(("%02X" % (c ^ next(keystream))))
#     return ''.join(output)
#
#
# def encrypt(key, plaintext, n, t):
#     plaintext = [ord(c) for c in plaintext]  # z liter robi kod ASCII
#     return encrypt_logic(key, plaintext, n, t)

def create_keystream(key, n, t):
    key = [ord(c) for c in key]
    keystream = get_keystream(key, n, t)

    output = []
    for _ in range(100):
        output.append(("%02X" % (next(keystream))))
    return ''.join(output)


def main():
    n = 256
    t = 256
    key = 'Wiki'
    keystream = create_keystream(key=key, n=n, t=t)
    print('keystream: ', keystream)


if __name__ == '__main__':
    main()
