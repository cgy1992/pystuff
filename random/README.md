So, for now I can't properly manage the category for small notes. So I've called that folder `random`. May be in the future I'll move some stuff to proper sections. And there will be some plain text may be split in paragraphs.

It is gonna be here some thoughts about py or about learning.

### Usage of several context managers simultaneously
```python
with open('a.txt', 'w') as a, open('b.txt', 'w') as b:
    for i in (a, b):
        i.write('text')
```

### Object creation with new
```python
#object construction with pseudo-code
def object_maker(the_class, some_arg):
    new_object = the_class.__new__(some_arg)
    if isinstance(new_object, the_class):
        the_class.__init__(new_object, some_arg)
    return new_object
```

The `__new__` method can also return an instance of a different class, and when that happens interpreter does not call `__init__`.

```python
class A():

    def __init__(self, a):
        self.a = a
        return 0

print(A(1).a)

Traceback (most recent call last):
  File "return_from_init.py", line 7, in <module>
    print(A(1).a)
TypeError: __init__() should return None, not 'int'
```
