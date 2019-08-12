from threading import Thread
import urllib.request


def actual_decorator(func):
    def wrapper(url, filename, thread_name):
        thread = Thread(target=func, args=(url, filename))
        print(f'Start of work {thread_name}, url {url}')
        thread.start()
        print(f'End of work {thread_name}, url {url}')
    return wrapper


@actual_decorator
def download_page(url, filename):
    opener = urllib.request.urlopen(url)
    with open(str(filename), 'w') as file:
        file.write(str(opener.read()))


url_list = ['https://www.tripadvisor.ru',
            'https://github.com',
            'https://www.google.com',
            'https://www.tripadvisor.ru',
            'https://github.com',
            'https://www.google.com',
            'https://www.tripadvisor.ru',
            'https://github.com',
            'https://www.google.com']

index = 1
for i in url_list:
    download_page(i, f'File {index}', f'Thread {index}')
    index += 1
