import time

squares = [x ** 2 for x in range(10)]
# print(squares)

odds = [x for x in range(10) if x % 2 != 0]
# print(odds)

list_var = [(1, 2), (3, 4), (5, 6), (7, 8)]

#   Если парное подносим в квадрат, иначе умножаем на -1

new_list = [tuple(x ** 2, y ** 2) if not x % 2 else (x * (-1), y ** 2) for x, y in list_var]

# print(new_list)

current_time = time.time()
first_variant = []
for i in range(1000000):
    first_variant.append(i)
print('Processing time is ', str(time.time() - current_time))

current_time1 = time.time()
second_variant = [x for x in range(1000000)]
print('Processing time is ', str(time.time() - current_time1))
