# -*- coding: utf-8 -*-
"""
课程：递归函数
演示：递归概念、终止条件、阶乘、斐波那契数列
"""

# 1. 阶乘
print("=== 阶乘 ===")
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(f"factorial(5) = {factorial(5)}")
print(f"factorial(10) = {factorial(10)}")

# 2. 斐波那契数列
print("\n=== 斐波那契数列 ===")
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

for i in range(10):
    print(f"fibonacci({i}) = {fibonacci(i)}")

# 3. 倒计时
print("\n=== 倒计时 ===")
def countdown(n):
    if n <= 0:
        print("Done!")
        return
    print(n)
    countdown(n - 1)

countdown(5)

# 4. 字符串反转
print("\n=== 字符串反转 ===")
def reverse_string(s):
    if len(s) <= 1:
        return s
    return reverse_string(s[1:]) + s[0]

print(f"reverse_string('hello') = {reverse_string('hello')}")
print(f"reverse_string('Python') = {reverse_string('Python')}")

# 5. 列表求和
print("\n=== 列表求和 ===")
def list_sum(lst):
    if not lst:
        return 0
    return lst[0] + list_sum(lst[1:])

numbers = [1, 2, 3, 4, 5]
print(f"list_sum({numbers}) = {list_sum(numbers)}")
