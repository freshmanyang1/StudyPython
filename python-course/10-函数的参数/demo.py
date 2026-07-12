# -*- coding: utf-8 -*-
"""
课程：函数的参数
演示：位置参数、关键字参数、可变参数
"""

# 1. 位置参数
print("=== 位置参数 ===")
def greet(name, age):
    print(f"姓名: {name}, 年龄: {age}")

greet("Alice", 25)

# 2. 关键字参数
print("\n=== 关键字参数 ===")
greet(age=25, name="Bob")

# 3. 默认参数
print("\n=== 默认参数 ===")
def greet_default(name, age=18):
    print(f"姓名: {name}, 年龄: {age}")

greet_default("Charlie")
greet_default("David", 30)

# 4. 可变参数 *args
print("\n=== 可变参数 *args ===")
def sum_numbers(*args):
    print(f"args = {args}")
    return sum(args)

print(f"sum_numbers(1, 2, 3) = {sum_numbers(1, 2, 3)}")
print(f"sum_numbers(1, 2, 3, 4, 5) = {sum_numbers(1, 2, 3, 4, 5)}")

# 5. 关键字可变参数 **kwargs
print("\n=== 关键字可变参数 **kwargs ===")
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"  {key}: {value}")

print_info(name="Alice", age=25, city="Beijing")

# 6. 参数组合
print("\n=== 参数组合 ===")
def func(a, b, *args, **kwargs):
    print(f"  a = {a}")
    print(f"  b = {b}")
    print(f"  args = {args}")
    print(f"  kwargs = {kwargs}")

func(1, 2, 3, 4, x=5, y=6)

# 7. 参数解包
print("\n=== 参数解包 ===")
def add(a, b, c):
    return a + b + c

numbers = [1, 2, 3]
print(f"add(*numbers) = {add(*numbers)}")

info = {"name": "Alice", "age": 25}
print_info(**info)

# 8. 强制关键字参数
print("\n=== 强制关键字参数 ===")
def func_keyword(a, b, *, c, d):
    print(f"  a = {a}, b = {b}, c = {c}, d = {d}")

func_keyword(1, 2, c=3, d=4)

# 9. 参数传递
print("\n=== 参数传递 ===")
def modify_list(lst):
    lst.append(4)
    print(f"  函数内: lst = {lst}")

my_list = [1, 2, 3]
print(f"  修改前: my_list = {my_list}")
modify_list(my_list)
print(f"  修改后: my_list = {my_list}")
