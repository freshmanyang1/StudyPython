# -*- coding: utf-8 -*-
"""
课程：高阶函数
演示：map、reduce、filter、sorted、lambda
"""

from functools import reduce

# 1. 高阶函数的概念
print("=== 高阶函数的概念 ===")
def apply(func, value):
    return func(value)

def square(x):
    return x ** 2

result = apply(square, 5)
print(f"apply(square, 5) = {result}")

# 2. map 函数
print("\n=== map 函数 ===")
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2, numbers))
print(f"numbers = {numbers}")
print(f"squares = {squares}")

# 3. reduce 函数
print("\n=== reduce 函数 ===")
numbers = [1, 2, 3, 4, 5]
total = reduce(lambda x, y: x + y, numbers)
print(f"numbers = {numbers}")
print(f"total = {total}")

# 4. filter 函数
print("\n=== filter 函数 ===")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even = list(filter(lambda x: x % 2 == 0, numbers))
print(f"numbers = {numbers}")
print(f"even = {even}")

# 5. sorted 函数
print("\n=== sorted 函数 ===")
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
sorted_numbers = sorted(numbers)
print(f"numbers = {numbers}")
print(f"sorted_numbers = {sorted_numbers}")

# 自定义排序
students = [("Alice", 85), ("Bob", 92), ("Charlie", 78)]
sorted_students = sorted(students, key=lambda x: x[1])
print(f"students = {students}")
print(f"sorted_students = {sorted_students}")

# 6. 匿名函数 lambda
print("\n=== 匿名函数 lambda ===")
square = lambda x: x ** 2
print(f"square(5) = {square(5)}")

add = lambda x, y: x + y
print(f"add(3, 5) = {add(3, 5)}")

# 7. 返回函数
print("\n=== 返回函数 ===")
def make_adder(n):
    def adder(x):
        return x + n
    return adder

add5 = make_adder(5)
add10 = make_adder(10)
print(f"add5(10) = {add5(10)}")
print(f"add10(20) = {add10(20)}")

# 8. 闭包
print("\n=== 闭包 ===")
def counter():
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    return increment

c = counter()
print(f"c() = {c()}")
print(f"c() = {c()}")
print(f"c() = {c()}")

# 9. 函数组合
print("\n=== 函数组合 ===")
def compose(f, g):
    return lambda x: f(g(x))

def double(x):
    return x * 2

def increment(x):
    return x + 1

double_then_increment = compose(increment, double)
increment_then_double = compose(double, increment)

print(f"double_then_increment(5) = {double_then_increment(5)}")
print(f"increment_then_double(5) = {increment_then_double(5)}")
