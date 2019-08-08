class Test:
    def __init__(self, x):
        self._x = x

    @property
    def x(self):
        print('getter called')
        return self._x

    @x.setter
    def x(self, x):
        print('setter called')
        self._x = x

    @x.deleter
    def x(self):
        print('deleter called')
        del self._x

obj = Test(100)
obj.x
obj.x = 'new value'
del obj.x
