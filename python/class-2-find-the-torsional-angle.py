import math

class Points(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __sub__(self, no):
        return Points(self.x - no.x, self.y - no.y, self.z - no.z)

    def dot(self, no):
        # Let a   =   ( a1, a2, a3 )T
        # Let b   =   ( b1, b2, b3 )T
        # Then the dot product is:
        # a · b   =   a1b1 + a2b2 + a3b3
        return sum([self.x * no.x, self.y * no.y, self.z * no.z])

    def cross(self, no):
        # If vector u is represented by     u   =   (ui , uj , uk )T
        # and if vector v is represented by     v   =   (vi , vj , vk )T.
        # Then   u × v   =   ( uj vk - uk vj ,   uk vi - ui vk ,   ui vj - uj vi )T.
        first_term = (self.y * no.z) - (self.z * no.y)
        second_term = (self.z * no.x) - (self.x * no.z)
        third_term = (self.x * no.y) - (self.y * no.x)
        return Points(first_term, second_term, third_term)

    def absolute(self):
        return pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5)

if __name__ == '__main__':
    points = list()
    for i in range(4):
        a = list(map(float, input().split()))
        points.append(a)

    a, b, c, d = Points(*points[0]), Points(*points[1]), Points(*points[2]), Points(*points[3])
    x = (b - a).cross(c - b)
    y = (c - b).cross(d - c)
    angle = math.acos(x.dot(y) / (x.absolute() * y.absolute()))

    print("%.2f" % math.degrees(angle))
