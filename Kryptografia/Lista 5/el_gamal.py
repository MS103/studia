from edvard_curves import EdwardsCurves


class ElGamal:
    def __init__(self, curve: EdwardsCurves, g):
        if not curve.is_on_curve(g):
            print("Generator nie na krzywej!")
            exit(-1)
        self.curve = curve
        self.g = g
        self.n = curve.order(g)

    def generate_public_key(self, private_key):
        return self.curve.scalar_mul(private_key, self.g)  # Iloczyn skalarny generatora i klucza prywatnego

    def encrypt_point(self, p, public_key, rand):
        if not (self.curve.is_on_curve(p) or self.curve.is_on_curve(public_key)):
            print("Punkty nie na krzywej!")
            exit(-1)
        cipher = self.curve.scalar_mul(rand, self.g), self.curve.add_points(p, self.curve.scalar_mul(rand, public_key))
        print(f'Szyfruję punkt {p} za pomocą klucza publicznego {public_key}.\nOtrzymano {cipher}')
        return cipher

    def decrypt_cipher(self, cipher, private_key):
        c1, c2 = cipher
        if not (self.curve.is_on_curve(c1) or self.curve.is_on_curve(c2)):
            print("Punkty nie na krzywej!")
            exit(-1)
        decoded = self.curve.add_points(c2, self.curve.neg(self.curve.scalar_mul(private_key, c1)))
        print(f'Odszyfrowuję punkt {cipher} za pomocą klucza prywatnego {private_key}.\n Otrzymano{decoded}')
        return decoded
