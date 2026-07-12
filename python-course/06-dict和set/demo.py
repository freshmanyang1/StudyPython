# -*- coding: utf-8 -*-
"""
课程：dict和set
演示：字典和集合的创建、操作和方法
"""

# 1. 字典的创建
print("=== 字典的创建 ===")
student = {
    "name": "Alice",
    "age": 25,
    "city": "Beijing"
}
print(f"student = {student}")

# 2. 字典操作 - 访问元素
print("\n=== 字典操作 - 访问元素 ===")
print(f"student['name'] = {student['name']}")
print(f"student.get('age') = {student.get('age')}")
print(f"student.get('email', 'N/A') = {student.get('email', 'N/A')}")

# 3. 字典操作 - 添加/修改元素
print("\n=== 字典操作 - 添加/修改元素 ===")
student["email"] = "alice@example.com"
print(f"添加email后: {student}")
student["age"] = 26
print(f"修改age后: {student}")

# 4. 字典操作 - 删除元素
print("\n=== 字典操作 - 删除元素 ===")
del student["email"]
print(f"删除email后: {student}")
student.pop("city")
print(f"删除city后: {student}")

# 5. 字典操作 - 检查键是否存在
print("\n=== 字典操作 - 检查键是否存在 ===")
print(f"'name' in student = {'name' in student}")
print(f"'email' in student = {'email' in student}")

# 6. 字典方法
print("\n=== 字典方法 ===")
student = {"name": "Alice", "age": 25}
print(f"student = {student}")
print(f"student.keys() = {student.keys()}")
print(f"student.values() = {student.values()}")
print(f"student.items() = {student.items()}")

student.update({"city": "Beijing"})
print(f"update后: {student}")

# 7. 字典推导式
print("\n=== 字典推导式 ===")
squares = {x: x**2 for x in range(10)}
print(f"squares = {squares}")

# 8. 集合的创建
print("\n=== 集合的创建 ===")
fruits = {"apple", "banana", "cherry"}
numbers = set([1, 2, 3, 4, 5])
print(f"fruits = {fruits}")
print(f"numbers = {numbers}")

# 9. 集合操作 - 添加/删除元素
print("\n=== 集合操作 - 添加/删除元素 ===")
fruits.add("grape")
print(f"添加grape后: {fruits}")
fruits.remove("banana")
print(f"删除banana后: {fruits}")

# 10. 集合运算
print("\n=== 集合运算 ===")
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(f"set1 = {set1}")
print(f"set2 = {set2}")
print(f"set1 | set2 (并集) = {set1 | set2}")
print(f"set1 & set2 (交集) = {set1 & set2}")
print(f"set1 - set2 (差集) = {set1 - set2}")

# 11. 集合方法
print("\n=== 集合方法 ===")
fruits = {"apple", "banana", "cherry"}
print(f"fruits = {fruits}")
print(f"len(fruits) = {len(fruits)}")

fruits.add("grape")
print(f"添加grape后: {fruits}")

fruits.discard("xxx")  # 不报错
print(f"discard('xxx')后: {fruits}")
