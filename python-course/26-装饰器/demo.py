# -*- coding: utf-8 -*-
"""
课程：装饰器
演示：装饰器概念、编写、使用、带参数的装饰器
"""

import functools

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
