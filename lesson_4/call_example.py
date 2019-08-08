class DecOne:
    def __init__(self, f):
        self._f = f

    def __call__(self, *args, **kwargs):
        print('Start decorating')
        self._f()
        print('End decorating')


@DecOne
def hi():
    print('Say Hello')


hi()
