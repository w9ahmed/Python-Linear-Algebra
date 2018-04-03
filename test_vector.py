import unittest
from math import sqrt, acos
from decimal import Decimal, getcontext
from vector import Vector


getcontext().prec = 30


class TestVector(unittest.TestCase):
    def test_init(self):
        with self.assertRaises(ValueError) as e:
            Vector([])
        self.assertEquals(e.exception.message, 'The coordinate must be nonempty')

        with self.assertRaises(TypeError) as e:
            Vector(1)
        self.assertEquals(e.exception.message, 'The coordinates must be an iterable')

        v = Vector([1, 2, 3])
        self.assertEqual((1, 2, 3), v.coordinates)
        self.assertEqual(3, v.dimension)

    def test_plus(self):
        v1 = Vector([1, 2, 3])
        v2 = Vector([1, 2, 3])

        result = v1.plus(v2)
        expected = Vector([2, 4, 6])
        self.assertEquals(expected, result)

    def test_minus(self):
        v1 = Vector([1, 2, 3])
        v2 = Vector([1, 2, 3])

        result = v1.minus(v2)
        expected = Vector([0, 0, 0])
        self.assertEquals(expected, result)

    def test_scalar_multiply(self):
        c = 5
        v = Vector([1, 2, 3])

        result = v.scalar_multiply(c)
        expected = Vector([5, 10, 15])
        self.assertEquals(expected, result)

    def test_magnitude(self):
        v = Vector([1, 2, 3])

        result = v.magnitude()
        expected = sqrt(14)
        self.assertEquals(expected, result)

    def test_normalize(self):
        with self.assertRaises(Exception) as e:
            Vector([0, 0, 0]).normalize()
        self.assertEquals(e.exception.message, 'Cannot normalize the zero vector')


        v = Vector([1, 2, 3])

        result = v.normalize()
        expected = Vector([1 / sqrt(14), 2 / sqrt(14), 3 / sqrt(14)])
        print result
        print expected
        self.assertEquals(expected, result)

    def test_dot_product(self):
        v1 = Vector([1, 2, 3])
        v2 = Vector([1, 2, 3])

        result = v1.dot_product(v2)
        self.assertEquals(14, result)

    def test_calculate_angle(self):
        v1 = Vector([1, 2, 3])
        v2 = Vector([1, 2, 3])

        result = v1.calculate_angle(v2)
        expected = acos((1 / 14.) + (4 / 14.) + (9 / 14.))
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()