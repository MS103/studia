from collections import namedtuple

from cyclic_group import Z

Point = namedtuple('Point', ['x', 'y'])


class EdwardsCurves: # Klasa krzywych eliptycznych zadanych przez: x**2 + y**2 = 1 + d * x**2 * y**2 (mod p)

    def __init__(self, d, p):
        self.z = Z(p)
        self.p = p
        self.d = self.process_d(d)
        self.one = self.z(1)
        self.zero = self.z(0)

    def process_d(self, d): #Przygotowanie wartości d, żeby można było wpisać np. '1/3'
        if type(d) == str:
            data = d.split('/')
            return self.z(int(data[0])) / self.z(int(data[1]))
        return self.z(d)

    def add_points(self, p1, p2): #Dodawanie punktów na krzywej - wzory z wykładu
        x1, y1 = p1
        x2, y2 = p2
        x3 = (x1 * y2 + y1 * x2) / (self.one + self.d * x1 * y1 * x2 * y2)
        y3 = (y1 * y2 - x1 * x2) / (self.one - self.d * x1 * y1 * x2 * y2)
        return self.create_point(x3.x, y3.x)

    def scalar_mul(self, scalar, point): #Mnożenie punktu przez skalar
        if scalar == 0:
            return self.create_point(0, 1)
        if scalar == 1:
            return point
        Q = self.scalar_mul(scalar // 2, point)
        Q = self.add_points(Q, Q)
        if scalar % 2:
            Q = self.add_points(Q, point)
        return Q

    def neg(self, p):#Zwraca punkt przeciwny
        return self.create_point(-p.x.x, p.y.x)

    def create_point(self, x, y): #Tworzy punkt z własnościami grupy
        x = self.z(x)
        y = self.z(y)
        return Point(x, y)

    def is_on_curve(self, p): #Sprawdza czy punkt jest na krzywej
        x, y = p
        x, y = x.x, y.x
        return (x ** 2 + y ** 2) % self.p == (1 + self.d.x * x ** 2 * y ** 2) % self.p

    def order(self, g): #Najmniejszy skalar x taki, że x*g = (0, 1) <- punkt bazowy dla krzywej zadanej
        base_point = self.create_point(0, 1)         # x**2 + y**2 = 1 + d * x**2 * y**2 (mod p)
        if not (self.is_on_curve(g) or g != base_point):
            print("Błąd wartości generatora!")
            exit(-1)
        for i in range(2, self.p):
            if self.scalar_mul(i, g) == base_point:
                return i
        return 1
