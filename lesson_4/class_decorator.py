class A:

    @classmethod
    def show_inside(cls):
        for d in cls.__dict__.items():
            print(d)

    @staticmethod
    def say_hello():
        print('Hello!!')


A.show_inside()
A.say_hello()
