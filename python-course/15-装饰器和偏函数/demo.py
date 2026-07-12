# -*- coding: utf-8 -*-
"""
课程：装饰器和偏函数
演示：装饰器、偏函数
"""

import functools
from functools import partial

# 1. 基本装饰器
print("=== 基本装饰器 ===")
def my_decorator(func):
    def wrapper():
        print("函数执行前")
        func()
        print("函数执行后")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()

# 2. 带参数的装饰器
print("\n=== 带参数的装饰器 ===")
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")

# 3. 保留原函数信息
print("\n=== 保留原函数信息 ===")
def my_decorator2(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@my_decorator2
def say_hi():
    """打招呼函数"""
    print("Hi!")

print(f"函数名: {say_hi.__name__}")
print(f"文档: {say_hi.__doc__}")

# 4. 类装饰器
print("\n=== 类装饰器 ===")
class Timer:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        import time
        start = time.time()
        result = self.func(*args, **kwargs)
        end = time.time()
        print(f"执行时间: {end - start:.4f} 秒")
        return result

@Timer
def slow_function():
    import time
    time.sleep(0.1)
    print("函数执行完成")

slow_function()

# 5. 偏函数
print("\n=== 偏函数 ===")
def add(x, y):
    return x + y

add5 = partial(add, 5)
print(f"add5(10) = {add5(10)}")
print(f"add5(20) = {add5(20)}")

# 6. partial 的应用
print("\n=== partial 的应用 ===")
int2 = partial(int, base=2)
print(f"int2('1010') = {int2('1010')}")

def power(base, exponent):
    return base ** exponent

square = partial(power, exponent=2)
cube = partial(power, exponent=3)

print(f"square(5) = {square(5)}")
print(f"cube(3) = {cube(3)}")

# 7. 多个装饰器
print("\n=== 多个装饰器 ===")
def bold(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return f"<b>{func(*args, **kwargs)}</b>"
    return wrapper

def italic(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return f"<i>{func(*args, **kwargs)}</i>"
    return wrapper

@bold
@italic
def say_hello():
    return "Hello, World!"

print(say_hello())
