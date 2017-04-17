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
