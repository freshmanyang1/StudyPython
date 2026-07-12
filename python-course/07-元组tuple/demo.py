# -*- coding: utf-8 -*-
"""
课程：元组tuple
演示：元组创建、访问、区别、方法、遍历
"""

# 1. 元组的创建
print("=== 元组的创建 ===")
point = (1, 2)
colors = ("red", "green", "blue")
single = (1,)  # 单元素元组需要逗号

print(f"point = {point}")
print(f"colors = {colors}")
print(f"single = {single}")
print(f"type(single) = {type(single)}")

# 2. 元组的访问
print("\n=== 元组的访问 ===")
point = (1, 2, 3)
print(f"point = {point}")
print(f"point[0] = {point[0]}")
print(f"point[1] = {point[1]}")
print(f"point[-1] = {point[-1]}")
print(f"point[-2] = {point[-2]}")

# 切片
print(f"point[1:] = {point[1:]}")
print(f"point[:2] = {point[:2]}")

# 3. 元组与列表的区别
print("\n=== 元组与列表的区别 ===")
# 列表是可变的
my_list = [1, 2, 3]
my_list[0] = 10
print(f"列表修改后: {my_list}")

# 元组是不可变的
my_tuple = (1, 2, 3)
try:
    my_tuple[0] = 10
except TypeError as e:
    print(f"元组修改失败: {e}")

# 4. 元组的常用方法
print("\n=== 元组的常用方法 ===")
point = (1, 2, 3)
print(f"point = {point}")
print(f"len(point) = {len(point)}")
print(f"point.count(1) = {point.count(1)}")
print(f"point.index(2) = {point.index(2)}")

# 5. 元组的遍历
print("\n=== 元组的遍历 ===")
point = (1, 2, 3)
print("for 循环遍历:")
for x in point:
    print(f"  {x}")

print("带索引遍历:")
for i, x in enumerate(point):
    print(f"  {i}: {x}")
