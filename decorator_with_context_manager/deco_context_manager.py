import functools


def opener(func):
    def wrapper(*args, **kwargs):
        with open(args[0], 'r') as source:
            func(*((source,) + args[1:]), **kwargs)
    return wrapper


def advanced_opener(mode='r'):
    def decorator(func):
        def wrapper(*args, **kwargs):
            with open(args[0], mode) as source:
                func(*((source,) + args[1:]), **kwargs)
        return wrapper
    return decorator


@advanced_opener('w')
def write_to_file(filename):
    filename.write('content!')


@opener
def read_file_from_file(filename):
    print(filename.readline())


write_to_file('test.txt')
read_file_from_file('test.txt')


def deco_call(func):
    def wrapper(*args, **kwargs):
        print('inside wrapper')
        func(*args, **kwargs)
        print('post call')
    return wrapper


def f(a, b):
    print('inside function')
    print(a, b)
    return a + b

a = deco_call(f)
print(a(1, 2))
print('-' * 80)


def deco_return(func):
    def wrapper(*args, **kwargs):
        print('inside wrapper')
        return func(*args, **kwargs)
        print('post call')
    return wrapper


b = deco_return(f)
print(b(1, 2))
print('-' * 80)


def deco_return_and_post(func):
    def wrapper(*args, **kwargs):
        print('inside wrapper')
        result = func(*args, **kwargs)
        print('post call')
        return result
    return wrapper

c = deco_return_and_post(f)
print(c(1, 2))
print('-' * 80)
