# -*- coding: utf-8 -*-
"""
课程：匿名函数lambda
演示：lambda 语法、使用场景、与普通函数的区别
"""

# 1. 基本语法
print("=== 基本语法 ===")
square = lambda x: x ** 2
print(f"square(5) = {square(5)}")

add = lambda x, y: x + y
print(f"add(3, 5) = {add(3, 5)}")

# 2. 作为参数传递
print("\n=== 作为参数传递 ===")
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2, numbers))
print(f"numbers = {numbers}")
print(f"squares = {squares}")

# 3. 排序
print("\n=== 排序 ===")
students = [("Alice", 85), ("Bob", 92), ("Charlie", 78)]
sorted_students = sorted(students, key=lambda x: x[1])
print(f"students = {students}")
print(f"sorted_students = {sorted_students}")

# 4. 与普通函数的区别
print("\n=== 与普通函数的区别 ===")
# 普通函数
def square_func(x):
    return x ** 2

# lambda 函数
square_lambda = lambda x: x ** 2

print(f"square_func(5) = {square_func(5)}")
print(f"square_lambda(5) = {square_lambda(5)}")
