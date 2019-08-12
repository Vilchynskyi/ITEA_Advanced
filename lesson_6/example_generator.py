# генератор это функция
def num_generator(numbers):
    for i in range(numbers):
        yield i
        print('After yield')


a = num_generator(10)
print(1, next(a))
print(2, next(a))
print(3, next(a))
print(4, next(a))
print(5, next(a))

for i in num_generator(5):
    pass

c = (x ** 2 for x in range(10))

print(c)
