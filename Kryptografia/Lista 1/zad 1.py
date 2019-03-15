class LCG:  # s[i+1] = (s[i]*a + b) % m

    def __init__(self, seed, a, b, m):
        self.state = seed
        self.a = a
        self.b = b
        self.m = m

    def random(self):
        self.state = (self.state * self.a + self.b) % self.m
        return self.state


class Crack_LCG:
    def __init__(self):
        self.state = None
        self.a = None
        self.b = None
        self.m = None

    @staticmethod
    def crack_lcg(states, m):  # Musimy znać tylko m
        delta = states[1] - states[0]
        a = (states[2] - states[1]) * modinv(delta, m) % m
        b = (states[1] - states[0] * a) % m
        return (states[-1], a, b, m)

    def predict_new_value_lcg(self, states, m):
        if self.state is None:
            state, self.a, self.b, self.m = self.crack_lcg(states, m)
            self.state = (state * self.a + self.b) % self.m
            return self.state
        else:
            self.state = (self.state * self.a + self.b) % self.m
            return self.state

    def clear_cracker(self):
        self.state = None
        self.a = None
        self.b = None
        self.m = None


## FUNKCJE POMOCNICZE - znalezione w internecie
def egcd(a, b):  # Rozszerzony algorytm Euklidesa
    if a == 0:
        return (b, 0, 1)
    else:
        g, x, y = egcd(b % a, a)
        return (g, y - (b // a) * x, x)  # zwraca (g, x, y) takie że a*x + b*y = g = gcd(a, b); gdzie gcd = NWD


def modinv(b, n):  # Odwrócone modulo
    g, x, _ = egcd(b, n)
    if g == 1:
        return x % n
    else:
        raise ValueError('Nie można znaleźć wartiści odwrotnej')


## PROGRAM WLAŚCIWY
seed = 5
a = 1664525
b = 1013904223
m = 2 ** 32  # Musi być można zrobić (x_1 - x_0) * y mod(m) = 1, dla dowolnego y < m .

states = []
lcg = LCG(seed=seed, a=a, b=b, m=m)
cracker = Crack_LCG()
for i in range(1000):
    lcg.random()
for j in range(3):
    states.append(lcg.random())
for k in range(10):
    print('\n')
    print('Przewidujemy nową liczbę: {0}'.format(cracker.predict_new_value_lcg(states, m)))
    print('Nową liczbą rzeczywiście jest: {0}'.format(lcg.random()))
