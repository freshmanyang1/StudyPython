# -*- coding: utf-8 -*-
"""
课程：条件判断
演示：if 语句、比较运算符、逻辑运算符
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

# 5. 比较运算符
print("\n=== 比较运算符 ===")
a, b = 10, 20
print(f"a = {a}, b = {b}")
print(f"a == b: {a == b}")
print(f"a != b: {a != b}")
print(f"a > b: {a > b}")
print(f"a < b: {a < b}")
print(f"a >= b: {a >= b}")
print(f"a <= b: {a <= b}")

# 6. 逻辑运算符
print("\n=== 逻辑运算符 ===")
x, y = True, False
print(f"x = {x}, y = {y}")
print(f"x and y: {x and y}")
print(f"x or y: {x or y}")
print(f"not x: {not x}")

# 7. 成员运算符
print("\n=== 成员运算符 ===")
fruits = ["apple", "banana", "cherry"]
print(f"fruits = {fruits}")
print(f"'apple' in fruits: {'apple' in fruits}")
print(f"'grape' in fruits: {'grape' in fruits}")
print(f"'grape' not in fruits: {'grape' not in fruits}")

# 8. 身份运算符
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

# 9. 嵌套条件
print("\n=== 嵌套条件 ===")
x = 15
if x > 0:
    if x > 10:
        print("x 是大于10的正数")
    else:
        print("x 是小于等于10的正数")
else:
    print("x 是负数或零")

# 10. 多条件判断
print("\n=== 多条件判断 ===")
age = 25
income = 10000
if age >= 18 and income >= 5000:
    print("符合申请条件")
else:
    print("不符合申请条件")
