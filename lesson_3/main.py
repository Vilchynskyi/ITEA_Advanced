if __name__ == '__main__':
    class Dot:
        def __init__(self, x, y, z):
            self.x = x
            self.y = y
            self.z = z

        def get_x(self):
            return self.x

        def set_x(self, value):
            self.x = value

        def get_y(self):
            return self.y

        def set_y(self, value):
            self.y = value

        def get_z(self):
            return self.z

        def set_z(self, value):
            self.z = value

        def __add__(self, other):
            result_x = self.get_x() + other.x
            result_y = self.get_y() + other.y
            result_z = self.get_z() + other.z
            return result_x, result_y, result_z

        def __sub__(self, other):
            result_x = self.get_x() - other.x
            result_y = self.get_y() - other.y
            result_z = self.get_z() - other.z
            return result_x, result_y, result_z

        def __mul__(self, other):
            result_x = self.get_x() * other.x
            result_y = self.get_y() * other.y
            result_z = self.get_z() * other.z
            return result_x, result_y, result_z

        def __truediv__(self, other):
            result_x = self.get_x() / other.x
            result_y = self.get_y() / other.y
            result_z = self.get_z() / other.z
            return result_x, result_y, result_z

        def __neg__(self):
            result, result1, result2 = -self.get_x(), -self.get_y(), -self.get_z()
            return result, result1, result2

    first_dot = Dot(1, 2, 3)
    second_dot = Dot(2, 4, 6)

    print('+', first_dot + second_dot)
    print('-', first_dot - second_dot)
    print('*', first_dot * second_dot)
    print('/', first_dot / second_dot)
    print(-first_dot)
