# -*- coding: utf-8 -*-
"""
课程：递归函数
演示：递归概念、终止条件、应用场景
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

# 3. 幂运算
print("\n=== 幂运算 ===")
def power(base, exponent):
    if exponent == 0:
        return 1
    return base * power(base, exponent - 1)

print(f"power(2, 10) = {power(2, 10)}")
print(f"power(3, 4) = {power(3, 4)}")

# 4. 倒计时
print("\n=== 倒计时 ===")
def countdown(n):
    if n <= 0:
        print("Done!")
        return
    print(n)
    countdown(n - 1)

countdown(5)

# 5. 字符串反转
print("\n=== 字符串反转 ===")
def reverse_string(s):
    if len(s) <= 1:
        return s
    return reverse_string(s[1:]) + s[0]

print(f"reverse_string('hello') = {reverse_string('hello')}")
print(f"reverse_string('Python') = {reverse_string('Python')}")

# 6. 列表求和
print("\n=== 列表求和 ===")
def list_sum(lst):
    if not lst:
        return 0
    return lst[0] + list_sum(lst[1:])

numbers = [1, 2, 3, 4, 5]
print(f"list_sum({numbers}) = {list_sum(numbers)}")

# 7. 二分查找
print("\n=== 二分查找 ===")
def binary_search(lst, target, low=0, high=None):
    if high is None:
        high = len(lst) - 1
    if low > high:
        return -1
    mid = (low + high) // 2
    if lst[mid] == target:
        return mid
    elif lst[mid] < target:
        return binary_search(lst, target, mid + 1, high)
    else:
        return binary_search(lst, target, low, mid - 1)

sorted_list = [1, 3, 5, 7, 9, 11, 13, 15]
print(f"binary_search({sorted_list}, 7) = {binary_search(sorted_list, 7)}")
print(f"binary_search({sorted_list}, 10) = {binary_search(sorted_list, 10)}")

# 8. 汉诺塔
print("\n=== 汉诺塔 ===")
def hanoi(n, source, target, auxiliary):
    if n == 1:
        print(f"移动盘子 1 从 {source} 到 {target}")
        return
    hanoi(n - 1, source, auxiliary, target)
    print(f"移动盘子 {n} 从 {source} 到 {target}")
    hanoi(n - 1, auxiliary, target, source)

hanoi(3, 'A', 'C', 'B')
