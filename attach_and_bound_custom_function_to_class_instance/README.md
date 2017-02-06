## Attach and bound custom function to class instance


It is really easy to monkeypatch class method with custom function.
```python
class A(object):

    def f(self):
        print 'I am method f!'


def custom(self):
    print 'I am custom function!'

>>> A.f = custom
>>> A().f()
I am custom function!
>>> A.f
<unbound method A.custom>
```

Nothing interesting here.

But if you need to monkeypatch method of certain existing instance of class:

```python
>>> a = A()
>>> a.f
<bound method A.f of <A object at 0x7fb497b94e10>>
>>> a.f = custom
>>> a.f
<function custom at 0x7fb49d458d70>
>>> a.f()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: custom() takes exactly 1 argument (0 given)
custom() takes exactly 1 argument (0 given)
```

there will be some issues. Since there is no anymore automatical passing of class instance (self).

To bind it, we can use the MethodType function in the types module:

```python
>>> import types
>>> a.f = types.MethodType(custom, a)
>>> a.f()
I am custom function!
>>> a.f
<bound method ?.custom of <A object at 0x7fb497b94e10>>
>>>
```
