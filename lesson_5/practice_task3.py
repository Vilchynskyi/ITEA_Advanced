import random


class File:

    def __init__(self, name_of_file, method):
        self._name_of_file = name_of_file
        self._method = method

    def __enter__(self):
        self._opened_file = open(self._name_of_file, self._method)
        return self._opened_file

    def __exit__(self, *args):
        if args[0]:
            print(f'Ooops, we have exceptions {args}')
        self._opened_file.close()


with File('ITEA', 'w') as f:
    f.write(str(random.randint(0, 10000)))
