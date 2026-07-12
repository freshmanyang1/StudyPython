# -*- coding: utf-8 -*-
"""
课程：偏函数
演示：偏函数概念、functools.partial、使用场景
"""

from functools import partial

# 1. 基本偏函数
print("=== 基本偏函数 ===")
def add(x, y):
    return x + y

add5 = partial(add, 5)
print(f"add5(10) = {add5(10)}")
print(f"add5(20) = {add5(20)}")

# 2. 固定参数
print("\n=== 固定参数 ===")
int2 = partial(int, base=2)
print(f"int2('1010') = {int2('1010')}")

# 3. 固定多个参数
print("\n=== 固定多个参数 ===")
def power(base, exponent):
    return base ** exponent

square = partial(power, exponent=2)
cube = partial(power, exponent=3)

print(f"square(5) = {square(5)}")
print(f"cube(3) = {cube(3)}")
