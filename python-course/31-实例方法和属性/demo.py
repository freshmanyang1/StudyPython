# -*- coding: utf-8 -*-
"""
课程：实例方法和属性
演示：self 参数、实例属性、类属性、实例方法
"""

# 1. self 参数
print("=== self 参数 ===")
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, {self.name}")

p = Person("Alice")
p.greet()

# 2. 实例属性
print("\n=== 实例属性 ===")
class Person2:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person2("Alice", 25)
print(f"姓名: {p.name}")
print(f"年龄: {p.age}")

# 3. 类属性
print("\n=== 类属性 ===")
class Person3:
    count = 0  # 类属性

    def __init__(self, name):
        self.name = name
        Person3.count += 1

p1 = Person3("Alice")
p2 = Person3("Bob")
print(f"Person3.count = {Person3.count}")

# 4. 实例方法
print("\n=== 实例方法 ===")
class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

calc = Calculator()
print(f"add(3, 5) = {calc.add(3, 5)}")
print(f"subtract(10, 3) = {calc.subtract(10, 3)}")
