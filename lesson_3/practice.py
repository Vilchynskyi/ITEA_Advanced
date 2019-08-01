import urllib.request


if __name__ == '__main__':
    def decorator(numbers_of_repeats):
        def actual_decorator(func):
            def wrapper(url):
                for i in range(numbers_of_repeats):
                    result = func(url)
                return result
            return wrapper
        return actual_decorator

    @decorator(5)
    def open_page(url):
        urllib.request.urlopen(url)

    open_page('https://www.google.com')
