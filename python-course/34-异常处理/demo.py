# -*- coding: utf-8 -*-
"""
课程：异常处理
演示：try-except、常见异常类型、finally
"""

# 1. try-except 语句
print("=== try-except 语句 ===")
try:
    result = 10 / 0
except ZeroDivisionError:
    print("除数不能为零")

# 2. 常见异常类型
print("\n=== 常见异常类型 ===")
# ValueError
try:
    int("abc")
except ValueError as e:
    print(f"ValueError: {e}")

# TypeError
try:
    "hello" + 123
except TypeError as e:
    print(f"TypeError: {e}")

# IndexError
try:
    lst = [1, 2, 3]
    print(lst[10])
except IndexError as e:
    print(f"IndexError: {e}")

# KeyError
try:
    d = {"a": 1}
    print(d["b"])
except KeyError as e:
    print(f"KeyError: {e}")

# 3. 捕获多个异常
print("\n=== 捕获多个异常 ===")
try:
    int("abc")
except (ValueError, TypeError) as e:
    print(f"错误: {e}")

# 4. finally 语句
print("\n=== finally 语句 ===")
try:
    result = 10 / 0
except ZeroDivisionError:
    print("除数不能为零")
finally:
    print("总是执行")
