# -*- coding: utf-8 -*-
"""
课程：list和tuple
演示：列表和元组的创建、操作和方法
"""

# 1. 列表的创建
print("=== 列表的创建 ===")
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]

print(f"fruits = {fruits}")
print(f"numbers = {numbers}")
print(f"mixed = {mixed}")

# 2. 列表操作 - 访问元素
print("\n=== 列表操作 - 访问元素 ===")
print(f"fruits[0] = {fruits[0]}")
print(f"fruits[-1] = {fruits[-1]}")

# 3. 列表操作 - 修改元素
print("\n=== 列表操作 - 修改元素 ===")
fruits[0] = "orange"
print(f"修改后: {fruits}")

# 4. 列表操作 - 添加元素
print("\n=== 列表操作 - 添加元素 ===")
fruits.append("grape")
print(f"append后: {fruits}")
fruits.insert(1, "mango")
print(f"insert后: {fruits}")

# 5. 列表操作 - 删除元素
print("\n=== 列表操作 - 删除元素 ===")
fruits.remove("banana")
print(f"remove后: {fruits}")
fruits.pop()
print(f"pop后: {fruits}")
del fruits[0]
print(f"del后: {fruits}")

# 6. 列表切片
print("\n=== 列表切片 ===")
numbers = [1, 2, 3, 4, 5]
print(f"numbers = {numbers}")
print(f"numbers[1:3] = {numbers[1:3]}")
print(f"numbers[:3] = {numbers[:3]}")
print(f"numbers[2:] = {numbers[2:]}")
print(f"numbers[::2] = {numbers[::2]}")
print(f"numbers[::-1] = {numbers[::-1]}")

# 7. 列表方法
print("\n=== 列表方法 ===")
fruits = ["apple", "banana", "cherry"]
print(f"fruits = {fruits}")
print(f"len(fruits) = {len(fruits)}")
print(f"fruits.count('apple') = {fruits.count('apple')}")
print(f"fruits.index('banana') = {fruits.index('banana')}")

fruits.sort()
print(f"sort后: {fruits}")
fruits.reverse()
print(f"reverse后: {fruits}")

# 8. 列表推导式
print("\n=== 列表推导式 ===")
squares = [x**2 for x in range(10)]
print(f"squares = {squares}")

even = [x for x in range(10) if x % 2 == 0]
print(f"even = {even}")

# 9. 元组的创建
print("\n=== 元组的创建 ===")
point = (1, 2)
colors = ("red", "green", "blue")
single = (1,)

print(f"point = {point}")
print(f"colors = {colors}")
print(f"single = {single}")

# 10. 元组操作
print("\n=== 元组操作 ===")
point = (1, 2, 3)
print(f"point = {point}")
print(f"point[0] = {point[0]}")
print(f"point[-1] = {point[-1]}")
print(f"point[1:] = {point[1:]}")
print(f"len(point) = {len(point)}")

# 遍历元组
print("遍历元组:")
for x in point:
    print(f"  {x}")

# 11. 列表和元组的区别
print("\n=== 列表和元组的区别 ===")
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
