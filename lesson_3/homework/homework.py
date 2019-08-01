if __name__ == '__main__':
    class Stack:
        def __init__(self):
            self.stack = []

        def append(self, item):
            self.stack.append(item)

        def pop(self):
            self.stack.pop()

        def get_stack(self):
            return self.stack

        def get_len(self):
            return len(self.stack)

    class Queue:
        def __init__(self):
            self.queue = []

        def append(self, item):
            self.queue.append(item)

        def pop(self):
            self.queue.pop(0)

        def get_queue(self):
            return self.queue

        def get_len(self):
            return len(self.queue)

    stack = Stack()
    stack.append(1)
    stack.append('34232')
    stack.append(True)
    print(stack.get_stack())
    stack.pop()
    print(stack.get_stack())
    print(stack.get_len())

    queue = Queue()
    queue.append(90)
    queue.append('56757')
    queue.append(False)
    print(queue.get_queue())
    queue.pop()
    print(queue.get_queue())
    print(queue.get_len())
