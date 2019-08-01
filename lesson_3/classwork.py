import urllib.request
import time


if __name__ == '__main__':
    def decorator(numbers_of_repeats):
        def actual_decorator(func):
            def wrapper(url):
                for i in range(numbers_of_repeats):
                    current_time = time.time()
                    result = func(url)
                    print('Processing time was -',
                          str(time.time() - current_time))
                return result
            return wrapper
        return actual_decorator

    @decorator(5)
    def open_page(url):
        urllib.request.urlopen(url)

    open_page('https://www.google.com')
