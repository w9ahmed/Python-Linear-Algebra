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

    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)

    def __eq__(self, v):
        return self.coordinates == v.coordinates


if __name__ == "__main__":
    my_vector = Vector([1, 2, 3])
    print my_vector

    my_vector2 = Vector([1, 2, 3])
    print my_vector == my_vector2

    my_vector3 = Vector([-1, 2, 3])
    print my_vector == my_vector3