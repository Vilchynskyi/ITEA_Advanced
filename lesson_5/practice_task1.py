from threading import Thread
import random
import time


def actual_decorator(func):
    def wrapper(*args):
        thread = Thread(target=func, args=args)
        thread.start()
    return wrapper


@actual_decorator
def thread_func(num, name):
    for i in range(num):
        time.sleep(random.randint(0, 1))
        print(f'I am executing from {name}')
    print(f'The end of {name}')


thread_func(3, 'thread')
