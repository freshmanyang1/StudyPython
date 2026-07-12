# -*- coding: utf-8 -*-
"""
课程：函数返回值
演示：return 语句、返回多个值、返回 None、提前返回
"""

# 1. return 语句
print("=== return 语句 ===")
def add(a, b):
    return a + b

result = add(3, 5)
print(f"add(3, 5) = {result}")

# 2. 返回多个值
print("\n=== 返回多个值 ===")
def get_info():
    return "Alice", 25

name, age = get_info()
print(f"姓名: {name}, 年龄: {age}")

# 3. 返回 None
print("\n=== 返回 None ===")
def greet(name):
    print(f"Hello, {name}!")

result = greet("Alice")
print(f"返回值: {result}")

# 4. 提前返回
print("\n=== 提前返回 ===")
def check_age(age):
    if age < 0:
        return "年龄无效"
    if age < 18:
        return "未成年"
    return "成年"

print(f"check_age(25) = {check_age(25)}")
print(f"check_age(15) = {check_age(15)}")
print(f"check_age(-5) = {check_age(-5)}")

# 5. 返回列表
print("\n=== 返回列表 ===")
def get_numbers(n):
    return [i for i in range(n)]

numbers = get_numbers(5)
print(f"get_numbers(5) = {numbers}")
