from Crypto.Cipher import AES

import hashlib


class OpenSSL:
    def __init__(self, mode):
        self.modes = {'ofb': AES.MODE_OFB, 'ctr': AES.MODE_CTR, 'cbc': AES.MODE_CBC}
        self.mode = self.modes[mode]

    # CBC - Polega na dodawaniu XOR każdego kolejnego bloku tekstu jawnego do poprzednio otrzymanego bloku szyfrogramu.

    # OFB - Szyfrujemy wektor inicjalizujący i powstaje nam X.
    # X XOR blok tekstu jawnego. Natępnie szyfrujemy X i powstaje X' itd.

    # CTR - Szyfrujemy Number-used-once+licznik i powstaje X.
    # X XOR blok tekstu jawnego.  Zwiększ licznik. Powtórz dla kolejnych bloków.

    def encrypt(self, msg, key, iv):
        iv = bytes(iv.encode())
        msg = bytes(msg.encode())
        if len(key) % 16:
            key = hashlib.sha256(key).digest()
        key = key.encode("utf8")
        msg += b'\x00' * ((16 - len(msg)) % 16)  # Długość wiadomości musi być mod 16 = 0
        if self.mode != self.modes['ctr']:
            encryptor = AES.new(key=key, mode=self.mode, iv=iv)
        else:
            encryptor = AES.new(key=key, mode=self.mode)

        return encryptor.encrypt(msg)

    def decrypt(self, msg, key, iv):
        iv = bytes(iv.encode())
        if len(key) % 16 != 0:
            key = hashlib.sha256(key).digest()
        key = key.encode("utf8")
        if self.mode != self.modes['ctr']:
            decryptor = AES.new(key=key, mode=self.mode, iv=iv)
        else:
            decryptor = AES.new(key=key, mode=self.mode)

        return decryptor.decrypt(msg)
