
def KSA(key, n):
    key_length = len(key)
    S = list(range(n))
    j = 0
    for i in range(n):
        j = (j + S[i] + key[i % key_length]) % n
        S[i], S[j] = S[j], S[i]

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


def get_keystream(key, n):
    S = KSA(key, n)
    return PRGA(S, n)


def encrypt_logic(key, text, n):
    key = [ord(c) for c in key]
    keystream = get_keystream(key, n)

    output = []
    for c in text:
        output.append(("%02X" % (c ^ next(keystream))))
    return ''.join(output)


def encrypt(key, plaintext, n):
    plaintext = [ord(c) for c in plaintext]  # z liter robi kod ASCII
    return encrypt_logic(key, plaintext, n)


def main():
    n = 256
    key = 'Secret'  # plaintext 'Key', 'Wiki', 'Secret'
    plaintext = 'Attack at dawn'  # plaintext 'Plaintext', 'pedia', 'Attack at dawn'
    ciphertext = encrypt(key, plaintext, n)  # 'BBF316E8D940AF0AD3', '1021BF0420', '45A01F645FC35B383552544B9BF5'
    print('plaintext:', plaintext)
    print('ciphertext:', ciphertext)

    if ciphertext == '45A01F645FC35B383552544B9BF5':
        print('\nSuccess')
    else:
        print('\nLost')


if __name__ == '__main__':
    main()
