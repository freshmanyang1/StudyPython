# -*- coding: utf-8 -*-
"""
课程：循环
演示：for 循环、while 循环、break、continue
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

# 3. for 循环 - 使用 range()
print("\n=== for 循环 - 使用 range() ===")
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

# 4. while 循环
print("\n=== while 循环 ===")
count = 0
while count < 5:
    print(count, end=" ")
    count += 1
print()

# 5. break 语句
print("\n=== break 语句 ===")
for i in range(10):
    if i == 5:
        break
    print(i, end=" ")
print()

# 6. continue 语句
print("\n=== continue 语句 ===")
for i in range(10):
    if i % 2 == 0:
        continue
    print(i, end=" ")
print()

# 7. else 子句
print("\n=== else 子句 ===")
for i in range(5):
    print(i, end=" ")
else:
    print("\n循环结束")

# 8. 循环嵌套
print("\n=== 循环嵌套 - 九九乘法表 ===")
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f"{j}x{i}={i*j}", end="\t")
    print()

# 9. 列表推导式
print("\n=== 列表推导式 ===")
squares = [x**2 for x in range(10)]
print(f"squares = {squares}")

even = [x for x in range(10) if x % 2 == 0]
print(f"even = {even}")

# 10. 嵌套列表推导式
print("\n=== 嵌套列表推导式 ===")
matrix = [[i * j for j in range(5)] for i in range(5)]
for row in matrix:
    print(row)
