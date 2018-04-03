from math import sqrt, pi, acos
from decimal import Decimal, getcontext

getcontext().prec = 30

def rad_to_deg(r):
    return r * 180 / pi

def deg_to_rad(d):
    return d * pi / 180

class Vector(object):

    CANNOT_NORMALIZE_ZERO_VECTOR_MSG = 'Cannot normalize the zero vector'

    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple([Decimal(x) for x in coordinates])
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
        new_coordinates = [Decimal(c)*x for x in self.coordinates]
        return Vector(new_coordinates)

    def magnitude(self):
        return Decimal(sqrt(sum([x**2 for x in self.coordinates])))

    def normalize(self):
        try:
            return self.scalar_multiply(Decimal(1.0) / self.magnitude())
        except ZeroDivisionError:
            raise Exception(self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG)

    def dot_product(self, v):
        return sum([x*y for x,y in zip(self.coordinates, v.coordinates)])

    def calculate_angle(self, v, in_degrees=False):
        try:
            u1 = self.normalize()
            u2 = v.normalize()

            angle_in_radians = acos(u1.dot_product(u2))

            if in_degrees:
                return rad_to_deg(angle_in_radians)
            else:
                return angle_in_radians
        except Exception as e:
            if str(e) == self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG:
                raise Exception('Cannot compute angle with the zero vector')
            else:
                raise e

    def is_orthogonal_to(self, v, tolerance=1e-10):
        return abs(self.dot_product(v)) < tolerance

    def is_parallel_to(self, v):
        return (self.is_zero() or v.is_zero() or self.calculate_angle(v) == 0 or self.calculate_angle(v) == pi)

    def is_zero(self, tolerance=1e-10):
        return self.magnitude() < tolerance

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

    print
    print '=> Exercises - Dot Product and Angle'
    v10 = Vector([7.887, 4.138])
    v11 = Vector([-8.802, 6.776])
    print v10.dot_product(v11)

    v12 = Vector([-5.955, -4.904, -1.874])
    v13 = Vector([-4.496, -8.755, 7.103])
    print v12.dot_product(v13)

    v14 = Vector([3.183, -7.627])
    v15 = Vector([-2.668, 5.319])
    print v14.calculate_angle(v15)

    v16 = Vector([7.35, 0.221, 5.188])
    v17 = Vector([2.751, 8.259, 3.985])
    print rad_to_deg(v16.calculate_angle(v17))

    print
    print '=> Exercises - Parallel and Orthogonal Vectors'
    v18 = Vector([-7.579, -7.88])
    v19 = Vector([22.737, 23.64])
    print 'orthogonal:', v18.is_orthogonal_to(v19)
    print 'parallel:', v18.is_parallel_to(v19)

    v20 = Vector([-2.029, 9.97, 4.172])
    v21 = Vector([-9.231, -6.639, -7.245])
    print 'orthogonal:', v20.is_orthogonal_to(v21)
    print 'parallel:', v20.is_parallel_to(v21)

    v22 = Vector([-2.328, 7.284, -1.214])
    v23 = Vector([-1.821, 1.072, -2.94])
    print 'orthogonal:', v22.is_orthogonal_to(v23)
    print 'parallel:', v22.is_parallel_to(v23)

    v24 = Vector([2.118, 4.827])
    v25 = Vector([0, 0])
    print 'orthogonal:', v24.is_orthogonal_to(v25)
    print 'parallel:', v24.is_parallel_to(v25)