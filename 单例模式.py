# -*- coding: utf-8 -*-
"""
1、使用__new__方法
"""
class Singlon(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            orig = super(Singlon, cls)
            cls._instance = orig.__new__(cls, *args, **kwargs)
        return cls._instance

"""
共享属性
"""
class Brog(object):
    _state = {}
    def __new__(cls, *args, **kwargs):
        ob = super(Brog, cls).__new__(cls, *args, **kwargs)
        ob.__dict__ = cls._state
        return ob


class A(object):
    def __init__(self):
        self.n = 2

    def add(self, m):
        print('self is {0} @A.add'.format(self))
        self.n += m


class B(A):
    def __init__(self):
        self.n = 3

    def add(self, m):
        print('self is {0} @B.add'.format(self))
        super(B, self).add(m)
        print ('newb')
        self.n += 3


class C(A):
    def __init__(self):
        self.n = 4

    def add(self, m):
        print ('self is {0} @C.add'.format(self))
        super(C, self).add(m)
        print ('newc')
        self.n += 4


class D(B, C):
    def __init__(self):
        self.n = 5

    def add(self, m):
        print ('self is {0} @D.add'.format(self))
        super(D, self).add(m)
        self.n += 5


d = D()
d.add(2)
print (d.n)

