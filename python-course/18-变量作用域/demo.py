# -*- coding: utf-8 -*-
"""
课程：变量作用域
演示：局部变量、全局变量、global、nonlocal
"""

# 1. 局部变量
print("=== 局部变量 ===")
def foo():
    x = 10  # 局部变量
    print(f"函数内: x = {x}")

foo()
# print(x)  # 错误：x 未定义

# 2. 全局变量
print("\n=== 全局变量 ===")
x = 10  # 全局变量

def bar():
    print(f"函数内: x = {x}")

bar()
print(f"函数外: x = {x}")

# 3. global 关键字
print("\n=== global 关键字 ===")
x = 10

def modify_global():
    global x
    x = 20

print(f"修改前: x = {x}")
modify_global()
print(f"修改后: x = {x}")

# 4. nonlocal 关键字
print("\n=== nonlocal 关键字 ===")
def outer():
    x = 10
    def inner():
        nonlocal x
        x = 20
    print(f"调用前: x = {x}")
    inner()
    print(f"调用后: x = {x}")

outer()
