import datetime
import functools

def decorator_time(func):
    @functools.wraps(func)
    def wrapper_time(*args, **kwargs):
        t1 = datetime.datetime.now()
        value = func(*args, **kwargs)
        t2 = datetime.datetime.now()
        t3 = t2 - t1
        print(f'Zeitstempel {t3 * 1000} ms')
        return value
    return wrapper_time


def decorator_url(func):

    forbidden_urls = ['lost.com', 'dolm.de', '']

    @functools.wraps(func)
    def wrapper_url(*args, **kwargs):

        for url in forbidden_urls:

            if url in args or url in kwargs.values():
                print(f'hey {url} is a forbidden url')
                return

        return func(*args, **kwargs)

    return wrapper_url

