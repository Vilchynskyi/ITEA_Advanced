# class Test:
#     __slots__ = '_a', '_b'
#
#     def __init__(self):
#         self._a = 10
#         self._b = 20
#
#
# a = Test()
# a.c = 24
# print(vars(a))

temp_list = [1, 2, 3]

# b = temp_list.__iter__()
#
# print(b.__next__())
# print(b.__next__())
# print(b.__next__())
# print(b.__next__())

# our_list = iter(temp_list)
#
# print(next(our_list))
# print(next(our_list))
# print(next(our_list))


class NumberGenerator:
    def __init__(self, start, end):
        self._start = start
        self._end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self._start < self._end:
            self._start += 1
            return self._start

        raise StopIteration('The end of structure')


a = NumberGenerator(0, 2)

print(iter(a))
print(next(a))
print(next(a))

for i in a:
    print(i)
