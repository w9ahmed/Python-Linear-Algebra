import unittest
from vector import Vector

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


if __name__ == '__main__':
    unittest.main()