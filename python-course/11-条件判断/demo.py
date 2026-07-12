# -*- coding: utf-8 -*-
"""
课程：条件判断
演示：if 语句、if-else、if-elif-else、条件表达式
"""

# 1. if 语句
print("=== if 语句 ===")
x = 10
if x > 0:
    print("x 是正数")

# 2. if-else 语句
print("\n=== if-else 语句 ===")
x = -5
if x > 0:
    print("x 是正数")
else:
    print("x 是负数或零")

# 3. if-elif-else 语句
print("\n=== if-elif-else 语句 ===")
x = 0
if x > 0:
    print("x 是正数")
elif x < 0:
    print("x 是负数")
else:
    print("x 是零")

# 4. 条件表达式（三元运算符）
print("\n=== 条件表达式 ===")
x = 10
result = "正数" if x > 0 else "负数或零"
print(f"x = {x}, result = {result}")

# 5. 嵌套条件
print("\n=== 嵌套条件 ===")
x = 15
if x > 0:
    if x > 10:
        print("x 是大于10的正数")
    else:
        print("x 是小于等于10的正数")
else:
    print("x 是负数或零")

# 6. 多条件判断
print("\n=== 多条件判断 ===")
age = 25
income = 10000
if age >= 18 and income >= 5000:
    print("符合申请条件")
else:
    print("不符合申请条件")
