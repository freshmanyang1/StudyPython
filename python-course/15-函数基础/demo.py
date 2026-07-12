# -*- coding: utf-8 -*-
"""
课程：函数基础
演示：函数定义、调用、文档字符串、内置函数
"""

# 1. 定义函数
print("=== 定义函数 ===")
def greet():
    print("Hello, World!")

# 2. 调用函数
print("\n=== 调用函数 ===")
greet()

# 3. 函数文档字符串
print("\n=== 函数文档字符串 ===")
def greet_with_doc():
    """
    打招呼函数
    输出 Hello, World!
    """
    print("Hello, World!")

greet_with_doc()
print(f"文档: {greet_with_doc.__doc__}")

# 4. 多个函数
print("\n=== 多个函数 ===")
def say_hello():
    print("Hello!")

def say_goodbye():
    print("Goodbye!")

say_hello()
say_goodbye()

# 5. 内置函数
print("\n=== 内置函数 ===")
print(f"print('Hello') - 输出函数")
print(f"len('Hello') = {len('Hello')} - 长度函数")
print(f"type(10) = {type(10)} - 类型函数")
print(f"int('123') = {int('123')} - 转换为整数")
print(f"str(123) = {str(123)} - 转换为字符串")
