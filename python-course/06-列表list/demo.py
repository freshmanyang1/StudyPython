# -*- coding: utf-8 -*-
"""
课程：列表list
演示：列表创建、访问、修改、方法、切片
"""

# 1. 列表的创建
print("=== 列表的创建 ===")
fruits = ["apple", "banana", "cherry"] #字符串数组
numbers = [1, 2, 3, 4, 5]  #整数数组
mixed = [1, "hello", 3.14, True] #混合类型数组

print(f"fruits = {fruits}")
print(f"numbers = {numbers}")
print(f"mixed = {mixed}")

# 2. 列表的访问
print("\n=== 列表的访问 ===")
print(f"fruits[0] = {fruits[0]}")
print(f"fruits[1] = {fruits[1]}")
print(f"fruits[-1] = {fruits[-1]}")
print(f"fruits[-2] = {fruits[-2]}")

# 3. 列表的修改
print("\n=== 列表的修改 ===")
fruits[0] = "orange"
print(f"修改后: {fruits}")

# 添加元素
fruits.append("grape")
print(f"append后: {fruits}")
fruits.insert(1, "mango")
print(f"insert后: {fruits}")

# 删除元素
print("\n=== 删除元素 ===")
fruits.remove("banana")
print(f"remove后: {fruits}")
fruits.pop()
print(f"pop后: {fruits}")
del fruits[0]
print(f"del后: {fruits}")

# 4. 列表的常用方法
print("\n=== 列表的常用方法 ===")
fruits = ["apple", "banana", "cherry"]
print(f"fruits = {fruits}")
print(f"len(fruits) = {len(fruits)}")
print(f"fruits.count('apple') = {fruits.count('apple')}")
print(f"fruits.index('banana') = {fruits.index('banana')}")

fruits.sort()
print(f"sort后: {fruits}")
fruits.reverse()
print(f"reverse后: {fruits}")

# 5. 列表的切片
print("\n=== 列表的切片 ===")
numbers = [1, 2, 3, 4, 5]
print(f"numbers = {numbers}")
print(f"numbers[1:3] = {numbers[1:3]}")
print(f"numbers[:3] = {numbers[:3]}")
print(f"numbers[2:] = {numbers[2:]}")
print(f"numbers[::2] = {numbers[::2]}")
print(f"numbers[::-1] = {numbers[::-1]}")
