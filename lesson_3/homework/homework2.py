if __name__ == '__main__':
    class ComplexNumber:
        def __init__(self, a, b):
            self.a = a
            self.b = b

        def __add__(self, other):
            result_a = self.a + other.a
            result_b = self.b + other.b
            return f'{result_a} + {result_b}i'

        def __sub__(self, other):
            result_a = self.a - other.a
            result_b = self.b - other.b
            return f'{result_a} - {result_b}i'

        def __mul__(self, other):
            result_a = self.a * other.a
            result_b = self.a * other.b
            return f'{result_a} * {result_b}i'

        def __truediv__(self, other):
            result_a = self.a / other.a
            result_b = self.a / other.b
            return f'{result_a} / {result_b}i'

    first_number = ComplexNumber(12, 23)
    second_number = ComplexNumber(10, 10)
    print(first_number + second_number)
    print(first_number - second_number)
    print(first_number * second_number)
    print(first_number / second_number)
