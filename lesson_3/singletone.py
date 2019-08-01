if __name__ == '__main__':
    class Singletone:
        _instance = None

        def __new__(cls, *args, **kwargs):
            if not cls._instance:
                cls._instance = super().__new__(cls)
                return cls._instance
            else:
                raise Exception('Instance already exist')


    class A(Singletone):
        def __init__(self, name):
            self.name = name

        def get_name(self):
            return self.name


    a1 = A('1')
    a2 = A('2')

    print(a1.get_name())

    print(a1 is a2)

    # var_list = [1, 2, 3]
    # print(type(var_list))
    # print(type(A))
