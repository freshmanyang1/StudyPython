# -*- coding: utf-8 -*-
"""
课程：自定义异常
演示：创建异常类、raise 语句、异常链
"""

# 1. 创建异常类
print("=== 创建异常类 ===")
class MyError(Exception):
    pass

def foo():
    raise MyError("自定义错误")

try:
    foo()
except MyError as e:
    print(f"捕获到: {e}")

# 2. raise 语句
print("\n=== raise 语句 ===")
def validate_age(age):
    if age < 0:
        raise ValueError("年龄不能为负数")
    if age > 150:
        raise ValueError("年龄不能大于150")
    return age

try:
    validate_age(-5)
except ValueError as e:
    print(f"错误: {e}")

try:
    validate_age(200)
except ValueError as e:
    print(f"错误: {e}")

# 3. 异常链
print("\n=== 异常链 ===")
try:
    try:
        int("abc")
    except ValueError as e:
        raise TypeError("类型错误") from e
except TypeError as e:
    print(f"捕获到: {e}")
    print(f"原始错误: {e.__cause__}")
