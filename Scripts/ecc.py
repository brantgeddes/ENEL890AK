
a = 1
b = 1

class Curve:
    a = None
    b = None
    m = None
    def __init__(self, a, b, m):
        self.a = a
        self.b = b
        self.m = m

    def check(self, p):
        y = p[1]
        x = p[0]
        return (y**2 % self.m == (x**3 + self.a*x + self.b) % self.m) and (0 < x < self.m) and (0 < y < self.m)

    def y(self, x):
        return ((x**3 + self.a * x + self.b)**(1/2)) % self.m

    def __add__(self, p1, p2):
        return self.add(p1, p2)

    def add(self, p1, p2):
        s = (p1[1] - p2[1]) / (p1[0] - p2[0])
        px = s**2 - p1[0] - p2[0]
        py = s * (p1[0] - px) - p1[1]
        return (px, py)

    def __exponent__(self, p):
        return self.double(p)

    def double(self, p):
        s = (3 * p[0]**2 + self.a) / (2 * p[1])
        rx = s**2 - 2 * p[0]
        ry = s * (p[0] - rx) - p[1]
        return (int(rx % self.m), int(ry % self.m))

curve = Curve(5, 7, 199)

#"""
print("Generator Points:")
for x in range(1, curve.m):
    y = int(curve.y(x))
    if (curve.check((x, y))):
        y = int(y)
        print("(x, y) = (" + str(x) + ", " + str(y) + ")")
#"""

dn = 2
r = (3, 7)
#"""
for i in range(dn):
    r = curve.double(r)
#"""

print(r, curve.check(r))

print(r[1]**2 % curve.m, (r[0]**3 + curve.a*(r[0]) + curve.b) % curve.m)
