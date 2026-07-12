# -*- coding: utf-8 -*-
"""
课程：Python基础语法
演示：缩进、标识符、关键字、语句
"""

# 1. 缩进示例
print("=== 缩进示例 ===")
if True:
    print("这是缩进的代码块")
    print("属于同一个 if 代码块")
print("这是 if 代码块外面的代码")

# 2. 标识符命名示例
print("\n=== 标识符命名示例 ===")

# 变量命名
my_name = "张三"
my_age = 25
student_count = 50

# 常量命名
MAX_SIZE = 100
PI = 3.14159

# 函数命名
def get_student_name():
    return "李四"

def calculate_sum(a, b):
    return a + b

print(f"名字: {my_name}")
print(f"年龄: {my_age}")
print(f"学生数量: {student_count}")
print(f"最大尺寸: {MAX_SIZE}")
print(f"PI: {PI}")
print(f"学生姓名: {get_student_name()}")
print(f"计算结果: {calculate_sum(10, 20)}")

# 3. 关键字示例
print("\n=== 关键字示例 ===")
import keyword
print(f"Python 关键字: {keyword.kwlist}")
print(f"关键字数量: {len(keyword.kwlist)}")

# 4. 语句示例
print("\n=== 语句示例 ===")

# 单行语句
y = 20
print(f"y = {y}")

# 多行语句（使用反斜杠）
total = 1 + 2 + 3 + \
        4 + 5 + 6
print(f"total = {total}")

# 多行语句（在括号内）
numbers = [
    1, 2, 3,
    4, 5, 6
]
print(f"numbers = {numbers}")
