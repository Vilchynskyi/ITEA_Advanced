import random

class File:

    def __init__(self, a, b):
        self._a = a
        self._b = b

    def __enter__(self):
        print(f'Entered args are {self._a, self._b}')
        return 'Hello'

    def __exit__(self, *args):
        print('The end of context_manager')


with File(2, 3) as f:
    print(f)
