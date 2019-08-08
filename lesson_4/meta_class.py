class MyMetaClass(type):
    def __new__(cls, name, bases, attributes):
        # name = name + 'MyMetaClass'
        # print(cls, name, bases, attrs)
        if 'attr' not in attributes:
            attributes['attr'] = True
        return super().__new__(cls, name, bases, attributes)


class TestingMeta(metaclass=MyMetaClass):

    _field = 'Field'

    def __init__(self):
        self._var = 10
        self._new_var = 20


print(TestingMeta.__dict__)
