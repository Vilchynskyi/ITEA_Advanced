from threading import Thread
import random
import time


def random_generator(num, thread_name):
    for i in range(num):
        time.sleep(random.randint(0, 5))
        print(f'I am executing from {thread_name}')
    print(f'the end of {thread_name}')


thread1 = Thread(target=random_generator, args=(5, 'thread1'))
thread2 = Thread(target=random_generator, args=(5, 'thread2'))

thread1.start()
thread2.start()

random_generator(5, 'main thread')


def file_writer(file_name, num_of_lines):

    with open(file_name, 'w') as f:
        for line in range(num_of_lines):
            f.write(str(random.randint(0, 5000)) + '\n')


list_of_threads = []

for i in range(3):
    t = Thread(target=file_writer,
               args=(str(random.randint(0, 1000)) + '.txt',
                     random.randint(0, 100)))

    list_of_threads.append(t)
    t.start()
print(list_of_threads)


class RandomGeneratorThread(Thread):
    def __init__(self, num, name):
        self._num = num
        self._name = name
        Thread.__init__(self, name=self._name)

    def run(self):
        for i in range(self._num):
            time.sleep(random.randint(0, 5))
            print(f'I am executing from {self._name}')
        print(f'the end of {self._name}')


a = RandomGeneratorThread(3, 'Thread a')
b = RandomGeneratorThread(3, 'Thread b')
a.daemon = True
b.daemon = True
a.start()
b.start()
