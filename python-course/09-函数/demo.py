# -*- coding: utf-8 -*-
"""
课程：函数
演示：函数定义、参数、返回值、作用域
"""

# 1. 函数定义
print("=== 函数定义 ===")
def greet():
    print("Hello, World!")

greet()

# 2. 函数参数
print("\n=== 函数参数 ===")
def greet_name(name):
    print(f"Hello, {name}!")

greet_name("Alice")

# 3. 默认参数
print("\n=== 默认参数 ===")
def greet_default(name="World"):
    print(f"Hello, {name}!")

greet_default()
greet_default("Bob")

# 4. 返回值
print("\n=== 返回值 ===")
def add(a, b):
    return a + b

result = add(3, 5)
print(f"3 + 5 = {result}")

# 5. 多个返回值
print("\n=== 多个返回值 ===")
def get_info():
    return "Alice", 25

name, age = get_info()
print(f"姓名: {name}, 年龄: {age}")

# 6. 函数作用域
print("\n=== 函数作用域 ===")
x = 10

def foo():
    y = 20
    print(f"函数内: x = {x}, y = {y}")

foo()
print(f"函数外: x = {x}")
# print(y)  # 错误：y 未定义

# 7. global 关键字
print("\n=== global 关键字 ===")
x = 10

def modify_global():
    global x
    x = 20

print(f"修改前: x = {x}")
modify_global()
print(f"修改后: x = {x}")

# 8. 文档字符串
print("\n=== 文档字符串 ===")
def greet_doc(name):
    """
    向用户打招呼

    参数:
        name: 用户名字

    返回:
        无
    """
    print(f"Hello, {name}!")

greet_doc("Charlie")
print(f"文档: {greet_doc.__doc__}")

# 9. 函数作为参数
print("\n=== 函数作为参数 ===")
def apply(func, value):
    return func(value)

def square(x):
    return x ** 2

def cube(x):
    return x ** 3

print(f"apply(square, 5) = {apply(square, 5)}")
print(f"apply(cube, 3) = {apply(cube, 3)}")

# 10. 内置函数
print("\n=== 内置函数 ===")
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"numbers = {numbers}")
print(f"len(numbers) = {len(numbers)}")
print(f"max(numbers) = {max(numbers)}")
print(f"min(numbers) = {min(numbers)}")
print(f"sum(numbers) = {sum(numbers)}")
print(f"sorted(numbers) = {sorted(numbers)}")
