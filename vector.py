from math import sqrt

class Vector(object):

    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)
        except ValueError:
            raise ValueError('The coordinate must be nonempty')
        except TypeError:
            raise TypeError('The coordinates must be an iterable')

    def plus(self, v):
        new_coordinates = [x+y for x, y in zip(self.coordinates, v.coordinates)]
        return Vector(new_coordinates)

    def minus(self, v):
        new_coordinates = [x-y for x,y in zip(self.coordinates, v.coordinates)]
        return Vector(new_coordinates)

    def scalar_multiply(self, c):
        new_coordinates = [c*x for x in self.coordinates]
        return Vector(new_coordinates)

    def magnitude(self):
        return sqrt(sum([x**2 for x in self.coordinates]))

    def normalize(self):
        try:
            return self.scalar_multiply(1. / self.magnitude())
        except ZeroDivisionError:
            raise Exception('Cannot normalize the zero vector')

    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)

    def __eq__(self, v):
        return self.coordinates == v.coordinates


if __name__ == "__main__":
    # Exercises
    print '=> Exercises - Arethmetic Operations'
    v1 = Vector([8.218, -9.341])
    v2 = Vector([-1.129, 2.111])
    print v1.plus(v2)

    v3 = Vector([7.119, 8.125])
    v4 = Vector([-8.223, 0.878])
    print v3.minus(v4)

    s = 7.41
    v5 = Vector([1.671, -1.012, -0.318])
    print v5.scalar_multiply(s)

    print
    print '=> Exercises - Magnitude and Direction'
    v6 = Vector([-0.221, 7.437])
    print v6.magnitude()

    v7 = Vector([8.813, -1.331, -6.247])
    print v7.magnitude()

    v8 = Vector([5.581, -2.136])
    print v8.normalize()

    v9  = Vector([1.996, 3.108, -4.554])
    print v9.normalize()