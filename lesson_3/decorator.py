if __name__ == '__main__':
    def decorator(num_of_repeats):
        print(num_of_repeats)

        def actual_decorator(func):
            def wrapper(*args):
                print(args)
                for i in range(num_of_repeats):
                    print("The begin of wrapping")
                    result = func(*args)
                    print("The end of wrapping")
                return result

            return wrapper

        return actual_decorator


    @decorator(10)
    def addition(arg1, arg2):
        return arg1 + arg2

    print(addition(1, 2))
