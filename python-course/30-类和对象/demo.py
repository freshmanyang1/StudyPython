# -*- coding: utf-8 -*-
"""
课程：类和对象
演示：类定义、实例化、__init__ 方法
"""

# 1. 定义类
print("=== 定义类 ===")
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name}")

# 2. 实例化
print("\n=== 实例化 ===")
p = Person("Alice", 25)
print(f"姓名: {p.name}")
print(f"年龄: {p.age}")
p.greet()

# 3. 多个实例
print("\n=== 多个实例 ===")
p1 = Person("Alice", 25)
p2 = Person("Bob", 30)
print(f"p1: {p1.name}, {p1.age}")
print(f"p2: {p2.name}, {p2.age}")

# 4. 修改属性
print("\n=== 修改属性 ===")
p = Person("Alice", 25)
print(f"修改前: {p.age}")
p.age = 26
print(f"修改后: {p.age}")
