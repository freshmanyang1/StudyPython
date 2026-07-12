# -*- coding: utf-8 -*-
"""
课程：面向对象高级编程
演示：__slots__、@property、多重继承、定制类
"""

from enum import Enum

# 1. __slots__
print("=== __slots__ ===")
class Student:
    __slots__ = ('name', 'age')

s = Student()
s.name = "Alice"
s.age = 25
print(f"姓名: {s.name}")
print(f"年龄: {s.age}")

# 2. @property
print("\n=== @property ===")
class Student2:
    def __init__(self, score):
        self._score = score

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('分数必须是整数')
        if value < 0 or value > 100:
            raise ValueError('分数必须在 0-100 之间')
        self._score = value

s = Student2(90)
print(f"分数: {s.score}")
s.score = 85
print(f"修改后: {s.score}")

# 3. 多重继承
print("\n=== 多重继承 ===")
class A:
    def foo(self):
        print("A.foo")

class B(A):
    def foo(self):
        print("B.foo")

class C(A):
    def foo(self):
        print("C.foo")

class D(B, C):
    pass

d = D()
d.foo()  # B.foo (MRO)
print(f"MRO: {[c.__name__ for c in D.__mro__]}")

# 4. 定制类
print("\n=== 定制类 ===")
class Student3:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'Student: {self.name}'

    def __repr__(self):
        return f'Student({self.name!r})'

s = Student3("Alice")
print(f"str: {s}")
print(f"repr: {repr(s)}")

# 5. 枚举类
print("\n=== 枚举类 ===")
class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

print(f"Color.RED = {Color.RED}")
print(f"Color.RED.name = {Color.RED.name}")
print(f"Color.RED.value = {Color.RED.value}")

# 6. 元类
print("\n=== 元类 ===")
class HelloMeta(type):
    def __new__(cls, name, bases, attrs):
        attrs['hello'] = lambda self: f"Hello from {name}"
        return type.__new__(cls, name, bases, attrs)

class Hello(metaclass=HelloMeta):
    pass

h = Hello()
print(h.hello())

# 7. 上下文管理器
print("\n=== 上下文管理器 ===")
class Timer:
    def __enter__(self):
        import time
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        import time
        self.end = time.time()
        print(f"执行时间: {self.end - self.start:.4f} 秒")
        return False

with Timer():
    sum(range(1000000))
