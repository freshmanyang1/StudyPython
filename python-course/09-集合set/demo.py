# -*- coding: utf-8 -*-
"""
课程：集合set
演示：集合创建、操作、运算、方法
"""

# 1. 集合的创建
print("=== 集合的创建 ===")
fruits = {"apple", "banana", "cherry"}
numbers = set([1, 2, 3, 4, 5])
print(f"fruits = {fruits}")
print(f"numbers = {numbers}")

# 2. 集合的常用操作
print("\n=== 集合的常用操作 ===")
fruits.add("grape")
print(f"添加grape后: {fruits}")
fruits.remove("banana")
print(f"删除banana后: {fruits}")

# 3. 集合的运算
print("\n=== 集合的运算 ===")
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(f"set1 = {set1}")
print(f"set2 = {set2}")
print(f"set1 | set2 (并集) = {set1 | set2}")
print(f"set1 & set2 (交集) = {set1 & set2}")
print(f"set1 - set2 (差集) = {set1 - set2}")
print(f"set1 ^ set2 (对称差集) = {set1 ^ set2}")

# 4. 集合的常用方法
print("\n=== 集合的常用方法 ===")
fruits = {"apple", "banana", "cherry"}
print(f"fruits = {fruits}")
print(f"len(fruits) = {len(fruits)}")

fruits.add("grape")
print(f"添加grape后: {fruits}")

fruits.discard("xxx")  # 不报错
print(f"discard('xxx')后: {fruits}")
