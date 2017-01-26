from functools import wraps
from inspect import signature


def dumb_deco(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('args', args)
        print('kwargs', kwargs)
        return func(*args, **kwargs)
    return wrapper


@dumb_deco
def f(a, b, c='test'):
    print('func_itself', a, b, c)


f('a', 'b')


def smart_deco(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('args', args)
        print('kwargs', kwargs)
        func_params = signature(func).parameters
        print(func_params)
        print(func_params.get('c').default)
        return func(*args, **kwargs)
    return wrapper


@smart_deco
def f(a, b, c='test'):
    print('func_itself', a, b, c)

f('a', 'b')
f('a', 'b', 'positional')
f('a', 'b', c='keyworded')
