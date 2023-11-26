from math import sqrt
class Vector:
# TODO: Finish the Vector class.
    def __init__(self, iterable):
        self._v = tuple(x for x in iterable)
        
    def __str__(self):
        return str(self._v).replace(' ', '')
    
    def check(self, other):
        if not len(self._v) == len(other._v):
            raise ValueError('Vectors of different length')

    def add(self, other):
        self.check(other)
        return Vector(s + o for s, o in zip(self._v, other._v))

    def subtract(self, other):
        self.check(other)
        return Vector(s - o for s, o in zip(self._v, other._v))

    def dot(self, other):
        self.check(other)
        return sum(s * o for s, o in zip(self._v, other._v))

    def norm(self):
        return sqrt(sum(x**2 for x in self._v))

    def equals(self, other):
        return self._v == other._v