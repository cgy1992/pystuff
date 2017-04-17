### Python built-in functions and other modules

[Built-in Functions](https://docs.python.org/3.6/library/functions.html)


#### [`vars([object])`](https://docs.python.org/3.6/library/functions.html#vars)
Return the `__dict__` attribute for a module, class, instance, or any other object with a `__dict__` attribute.

Objects such as modules and instances have an updateable `__dict__` attribute; however, other objects may have write restrictions on their `__dict__` attributes (for example, classes use a types.MappingProxyType to prevent direct dictionary updates).

Without an argument, `vars()` acts like `locals()`. Note, the locals dictionary is only useful for reads since updates to the locals dictionary are ignored.

#### [`object.__dict__`](https://docs.python.org/3.6/library/stdtypes.html#object.__dict__)
A dictionary or other mapping object used to store an object’s (writable) attributes.

#### [`locals()`](https://docs.python.org/3.6/library/functions.html#locals)
Update and return a dictionary representing the current local symbol table. Free variables are returned by `locals()` when it is called in function blocks, but not in class blocks.

Note, the contents of this dictionary *should not be modified*; changes may not affect the values of local and free variables used by the interpreter.

```python
from pprint import pprint as pp


class A():
    a = 5
    pp(vars())

    def f(self, x):
        self.x = x


def s(o):
    pp(vars())
    return o

s(2)
pp(vars())
pp(vars(A))  # same as pp(A.__dict__)

{'__module__': '__main__', '__qualname__': 'A', 'a': 5}
{'o': 2}
{'A': <class '__main__.A'>,
 '__builtins__': <module 'builtins' (built-in)>,
 '__cached__': None,
 '__doc__': None,
 '__file__': '/var_scope.py',
 '__loader__': <_frozen_importlib.SourceFileLoader object at 0x7f9c98e88eb8>,
 '__name__': '__main__',
 '__package__': None,
 '__spec__': None,
 'pp': <function pprint at 0x7f9c98e82378>,
 's': <function s at 0x7f9c98eb2bf8>}
mappingproxy({'f': <function A.f at 0x7f9c9139f378>, '__doc__': None, '__dict__': <attribute '__dict__' of 'A' objects>, 'a': 5, '__weakref__': <attribute '__weakref__' of 'A' objects>, '__module__': '__main__'})
```
