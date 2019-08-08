from threading import Thread
import random
import time


def decorator(thread_name, number_of_threads=1):
    def actual_decorator(func):
        def wrapper():
            temp_var = 1
            for thread in range(number_of_threads):
                thread = Thread(target=func,
                               args=(2, thread_name + str(temp_var)))
                thread.start()
                temp_var += 1
        return wrapper
    return actual_decorator


@decorator('MyThreadName', number_of_threads=3)
def thread_func(num, thread_name):
    for i in range(num):
        time.sleep(random.randint(0, 1))
        print(f'I am executing from {thread_name}')
    print(f'The end of {thread_name}')


thread_func()
