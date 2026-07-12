# -*- coding: utf-8 -*-
"""
课程：切片和迭代
演示：切片操作、迭代器、enumerate、zip
"""

# 1. 列表切片
print("=== 列表切片 ===")
lst = [0, 1, 2, 3, 4, 5]
print(f"lst = {lst}")
print(f"lst[1:4] = {lst[1:4]}")
print(f"lst[:3] = {lst[:3]}")
print(f"lst[3:] = {lst[3:]}")
print(f"lst[::2] = {lst[::2]}")
print(f"lst[::-1] = {lst[::-1]}")

# 2. 字符串切片
print("\n=== 字符串切片 ===")
s = "Hello World"
print(f"s = {s}")
print(f"s[0:5] = {s[0:5]}")
print(f"s[6:] = {s[6:]}")
print(f"s[::-1] = {s[::-1]}")

# 3. 元组切片
print("\n=== 元组切片 ===")
t = (1, 2, 3, 4, 5)
print(f"t = {t}")
print(f"t[1:3] = {t[1:3]}")

# 4. 可迭代对象
print("\n=== 可迭代对象 ===")
# 列表
for item in [1, 2, 3]:
    print(item, end=" ")
print()

# 字符串
for char in "Hello":
    print(char, end=" ")
print()

# 字典
d = {"a": 1, "b": 2}
for key, value in d.items():
    print(f"{key}: {value}", end=" ")
print()

# 5. 迭代器
print("\n=== 迭代器 ===")
lst = [1, 2, 3]
it = iter(lst)
print(f"next(it) = {next(it)}")
print(f"next(it) = {next(it)}")
print(f"next(it) = {next(it)}")

# 6. enumerate 函数
print("\n=== enumerate 函数 ===")
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

# 7. zip 函数
print("\n=== zip 函数 ===")
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
for name, age in zip(names, ages):
    print(f"{name}: {age}")

# 8. map 函数
print("\n=== map 函数 ===")
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2, numbers))
print(f"numbers = {numbers}")
print(f"squares = {squares}")

# 9. filter 函数
print("\n=== filter 函数 ===")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even = list(filter(lambda x: x % 2 == 0, numbers))
print(f"numbers = {numbers}")
print(f"even = {even}")

# 10. 切片赋值
print("\n=== 切片赋值 ===")
lst = [1, 2, 3, 4, 5]
print(f"原始列表: {lst}")
lst[1:3] = [20, 30]
print(f"切片赋值后: {lst}")
