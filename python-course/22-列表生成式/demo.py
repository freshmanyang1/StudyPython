# -*- coding: utf-8 -*-
"""
课程：列表生成式
演示：基本语法、带条件、嵌套列表生成式
"""

# 1. 基本语法
print("=== 基本语法 ===")
squares = [x**2 for x in range(10)]
print(f"squares = {squares}")

# 2. 带条件
print("\n=== 带条件 ===")
even = [x for x in range(10) if x % 2 == 0]
print(f"even = {even}")

# 3. 嵌套列表生成式
print("\n=== 嵌套列表生成式 ===")
matrix = [[i * j for j in range(5)] for i in range(5)]
for row in matrix:
    print(row)

# 4. 字符串处理
print("\n=== 字符串处理 ===")
words = ["hello", "world", "python"]
upper_words = [word.upper() for word in words]
print(f"upper_words = {upper_words}")

# 5. 字典生成
print("\n=== 字典生成 ===")
squares_dict = {x: x**2 for x in range(10)}
print(f"squares_dict = {squares_dict}")

# 6. 集合生成
print("\n=== 集合生成 ===")
unique_lengths = {len(word) for word in words}
print(f"unique_lengths = {unique_lengths}")
