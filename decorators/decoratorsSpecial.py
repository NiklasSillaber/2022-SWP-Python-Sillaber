import functools

def do_twice(func):
    @functools.wraps(func)
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    return wrapper_do_twice

def do_n(times):

    def decorator_do_n(func):
        @functools.wraps(func)
        def wrapper_do_n(*args, **kwargs):
            for _ in range(times):
                return func(*args, **kwargs)
        return wrapper_do_n

    return 
    

def print_before(func):
    @functools.wraps(func)
    def wrapper_print_before(*args, **kwargs):
        print('Start der Funktion')
        func(*args, **kwargs)
        print('Ende der Funktion')
    return wrapper_print_before
