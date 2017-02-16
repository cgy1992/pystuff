Decorate function with context manager
--------------------------------------

To do this we just need use context manager before calling the function:

```python
def opener(func):
    def wrapper(*args, **kwargs):
        with open(args[0], 'r') as source:
            func(*((source,) + args[1:]), **kwargs)
    return wrapper


@opener
def read_file_from_file(filename):
    print(filename.readline())


read_file_from_file('test.txt')
```


###Decotrator with arguments

The decorator with arguments should return a function that will take a function and return another function. So it should really return a normal decorator. In fact the outermost function for decorator with arguments is a decorator factory.

```python
def advanced_opener(mode='r'):
    def decorator(func):
        def wrapper(*args, **kwargs):
            with open(args[0], mode) as source:
                func(*((source,) + args[1:]), **kwargs)
        return wrapper
    return decorator
```

###Three ways to return result from wrapper

```python
def dec(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
    return wrapper

def dec(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

def dec(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result
    return wrapper
```

So in first case we don't care about return value at all. There will be `None`.

In second case decorated function will return result, but it will be immediately after `return`. So there is no any postprocessing.

And finally we could dump result to variable and continue with desired processing as we did in third case.

Related links:
```
http://www.artima.com/weblogs/viewpost.jsp?thread=240845
http://stackoverflow.com/questions/5929107/python-decorators-with-parameters
```

####TODO
```
Continue with http://stackoverflow.com/questions/9213600/function-acting-as-both-decorator-and-context-manager-in-python
```