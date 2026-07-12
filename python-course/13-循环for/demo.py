# -*- coding: utf-8 -*-
"""
课程：循环for
演示：for 循环、range()、enumerate、for-else、嵌套循环
"""

# 1. for 循环 - 遍历列表
print("=== for 循环 - 遍历列表 ===")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# 2. for 循环 - 遍历字符串
print("\n=== for 循环 - 遍历字符串 ===")
for char in "Hello":
    print(char)

# 3. range() 函数
print("\n=== range() 函数 ===")
print("range(5):")
for i in range(5):
    print(i, end=" ")
print()

print("range(1, 6):")
for i in range(1, 6):
    print(i, end=" ")
print()

print("range(0, 10, 2):")
for i in range(0, 10, 2):
    print(i, end=" ")
print()

# 4. enumerate 函数
print("\n=== enumerate 函数 ===")
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

# 5. for-else 语句
print("\n=== for-else 语句 ===")
for i in range(5):
    print(i, end=" ")
else:
    print("\n循环结束")

# 6. 嵌套循环
print("\n=== 嵌套循环 ===")
for i in range(3):
    for j in range(3):
        print(f"({i}, {j})", end=" ")
    print()

# 7. 九九乘法表
print("\n=== 九九乘法表 ===")
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f"{j}x{i}={i*j}", end="\t")
    print()
