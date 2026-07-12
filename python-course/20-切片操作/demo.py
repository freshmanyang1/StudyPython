# -*- coding: utf-8 -*-
"""
课程：切片操作
演示：列表切片、字符串切片、元组切片、切片赋值
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

# 4. 切片赋值
print("\n=== 切片赋值 ===")
lst = [1, 2, 3, 4, 5]
print(f"原始列表: {lst}")
lst[1:3] = [20, 30]
print(f"切片赋值后: {lst}")
