from math import sqrt


class GeoLocation:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def distance(self, g):
        calc = sqrt((self.x - g.x) ** 2 + (self.y - g.y) ** 2 + (self.z - g.z) ** 2)
        return calc

