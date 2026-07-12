# -*- coding: utf-8 -*-
"""
课程：迭代和enumerate
演示：for 循环迭代、enumerate、zip、map
"""

# 1. for 循环迭代
print("=== for 循环迭代 ===")
# 遍历列表
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# 遍历字符串
print("\n遍历字符串:")
for char in "Hello":
    print(char, end=" ")
print()

# 遍历字典
print("\n遍历字典:")
d = {"a": 1, "b": 2}
for key, value in d.items():
    print(f"{key}: {value}")

# 2. enumerate 函数
print("\n=== enumerate 函数 ===")
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

# 3. zip 函数
print("\n=== zip 函数 ===")
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
for name, age in zip(names, ages):
    print(f"{name}: {age}")

# 4. map 函数
print("\n=== map 函数 ===")
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2, numbers))
print(f"numbers = {numbers}")
print(f"squares = {squares}")
