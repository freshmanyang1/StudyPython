# -*- coding: utf-8 -*-
"""
课程：比较和逻辑运算符
演示：比较运算符、逻辑运算符、成员运算符、身份运算符
"""

# 1. 比较运算符
print("=== 比较运算符 ===")
a, b = 10, 20
print(f"a = {a}, b = {b}")
print(f"a == b: {a == b}")
print(f"a != b: {a != b}")
print(f"a > b: {a > b}")
print(f"a < b: {a < b}")
print(f"a >= b: {a >= b}")
print(f"a <= b: {a <= b}")

# 2. 逻辑运算符
print("\n=== 逻辑运算符 ===")
x, y = True, False
print(f"x = {x}, y = {y}")
print(f"x and y: {x and y}")
print(f"x or y: {x or y}")
print(f"not x: {not x}")

# 3. 成员运算符
print("\n=== 成员运算符 ===")
fruits = ["apple", "banana", "cherry"]
print(f"fruits = {fruits}")
print(f"'apple' in fruits: {'apple' in fruits}")
print(f"'grape' in fruits: {'grape' in fruits}")
print(f"'grape' not in fruits: {'grape' not in fruits}")

# 4. 身份运算符
print("\n=== 身份运算符 ===")
a = [1, 2, 3]
b = [1, 2, 3]
c = a
print(f"a = {a}")
print(f"b = {b}")
print(f"c = a")
print(f"a is b: {a is b}")
print(f"a is c: {a is c}")
print(f"a == b: {a == b}")

# 5. 复合条件
print("\n=== 复合条件 ===")
age = 25
income = 10000
if age >= 18 and income >= 5000:
    print("符合申请条件")
else:
    print("不符合申请条件")
