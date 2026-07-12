# -*- coding: utf-8 -*-
"""
课程：高阶函数
演示：map、reduce、filter、sorted
"""

from functools import reduce

# 1. map 函数
print("=== map 函数 ===")
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2, numbers))
print(f"numbers = {numbers}")
print(f"squares = {squares}")

# 2. reduce 函数
print("\n=== reduce 函数 ===")
numbers = [1, 2, 3, 4, 5]
total = reduce(lambda x, y: x + y, numbers)
print(f"numbers = {numbers}")
print(f"total = {total}")

# 3. filter 函数
print("\n=== filter 函数 ===")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even = list(filter(lambda x: x % 2 == 0, numbers))
print(f"numbers = {numbers}")
print(f"even = {even}")

# 4. sorted 函数
print("\n=== sorted 函数 ===")
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
sorted_numbers = sorted(numbers)
print(f"numbers = {numbers}")
print(f"sorted_numbers = {sorted_numbers}")

# 5. 自定义排序
print("\n=== 自定义排序 ===")
students = [("Alice", 85), ("Bob", 92), ("Charlie", 78)]
sorted_students = sorted(students, key=lambda x: x[1])
print(f"students = {students}")
print(f"sorted_students = {sorted_students}")
