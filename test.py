def do_sth(a, b, c, *args):
    return print(a, b, c, args)
    

#do_sth(2, 5, *[7, 7, 8, 6])



def do_lol(a, b, x, **kwargs):
    return print(a, b, x, kwargs)


dic = {'b':2, 'x':99, 'a': 1, 'i':87, 'j': 187}

#do_lol(**dic)

def super_flex(p1, p2, *args, **kwargs):
    print(p1)
    print(p2)
    print(args)
    print(kwargs)

#super_flex(*[1], **{'p2': 4, 'j': 6})

#Decorators
def outer_function(num):

    def inner_function(n):
        return f'Im wilden Hause {n}'

    return inner_function(num)

#a = outer_function('Högler')
#print(a)

def seas(name):
    return f'Habe die Äre {name}'

def seasFelix(greet):
    return greet('Felix')

#w = seasFelix(seas)
#print(w)

# def my_decorator(func):
#     def wrapper():
#         print("Something is happening before the function is called.")
#         func()
#         print("Something is happening after the function is called.")
#     return wrapper

# def say_whee():
#     print("Whee!")

# say_whee = my_decorator(say_whee)

# say_whee()

# from datetime import datetime

# def not_during_the_night(func):
#     def wrapper():
#         if 7 <= datetime.now().hour < 22:
#             print('ok')
#             func()
#         else:
#             pass  # Hush, the neighbors are asleep
#     return wrapper

# @not_during_the_night
# def say_whee():
#     print("Whee!")

# say_whee()

from decorators import timer

@timer
def waste_some_time(num_times):
    for _ in range(num_times):
        sum([i**2 for i in range(10000)])

waste_some_time(1)