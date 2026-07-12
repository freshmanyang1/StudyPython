# -*- coding: utf-8 -*-
"""
课程：字典dict
演示：字典创建、访问、修改、方法、推导式
"""

# 1. 字典的创建
print("=== 字典的创建 ===")
student = {
    "name": "Alice",
    "age": 25,
    "city": "Beijing"
}
print(f"student = {student}")

# 2. 字典的访问
print("\n=== 字典的访问 ===")
print(f"student['name'] = {student['name']}")
print(f"student.get('age') = {student.get('age')}")
print(f"student.get('email', 'N/A') = {student.get('email', 'N/A')}")

# 3. 字典的修改
print("\n=== 字典的修改 ===")
student["email"] = "alice@example.com"
print(f"添加email后: {student}")
student["age"] = 26
print(f"修改age后: {student}")

# 删除元素
print("\n=== 删除元素 ===")
del student["email"]
print(f"删除email后: {student}")
student.pop("city")
print(f"删除city后: {student}")

# 检查键是否存在
print("\n=== 检查键是否存在 ===")
print(f"'name' in student = {'name' in student}")
print(f"'email' in student = {'email' in student}")

# 4. 字典的常用方法
print("\n=== 字典的常用方法 ===")
student = {"name": "Alice", "age": 25}
print(f"student = {student}")
print(f"student.keys() = {student.keys()}")
print(f"student.values() = {student.values()}")
print(f"student.items() = {student.items()}")

student.update({"city": "Beijing"})
print(f"update后: {student}")

# 5. 字典推导式
print("\n=== 字典推导式 ===")
squares = {x: x**2 for x in range(10)}
print(f"squares = {squares}")

even_squares = {x: x**2 for x in range(10) if x % 2 == 0}
print(f"even_squares = {even_squares}")
