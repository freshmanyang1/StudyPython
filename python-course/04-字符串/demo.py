# -*- coding: utf-8 -*-
"""
课程：字符串
演示：字符串的创建、操作、方法和格式化
"""

# 1. 字符串的创建
print("=== 字符串的创建 ===")
s1 = "Hello"
s2 = 'World'
s3 = """多行
字符串"""
s4 = '''也是
多行字符串'''

print(f"s1 = {s1}")
print(f"s2 = {s2}")
print(f"s3 = {s3}")
print(f"s4 = {s4}")

# 2. 转义字符
print("\n=== 转义字符 ===")
print("换行符：第一行\n第二行")
print("制表符：列1\t列2\t列3")
print("反斜杠：\\")
print("单引号：\'")
print("双引号：\"")

# 3. 字符串操作
print("\n=== 字符串操作 ===")
# 拼接
s = "Hello" + " " + "World"
print(f"拼接: {s}")

# 重复
s = "Hello" * 3
print(f"重复: {s}")

# 长度
print(f"长度: {len('Hello')}")

# 4. 字符串索引
print("\n=== 字符串索引 ===")
s = "Hello"
print(f"s = {s}")
print(f"s[0] = {s[0]}")
print(f"s[1] = {s[1]}")
print(f"s[-1] = {s[-1]}")
print(f"s[-2] = {s[-2]}")

# 5. 字符串切片
print("\n=== 字符串切片 ===")
s = "Hello World"
print(f"s = {s}")
print(f"s[0:5] = {s[0:5]}")
print(f"s[6:] = {s[6:]}")
print(f"s[:5] = {s[:5]}")
print(f"s[::2] = {s[::2]}")
print(f"s[::-1] = {s[::-1]}")

# 6. 常用方法
print("\n=== 常用方法 ===")
s = "  Hello World  "
print(f"s = '{s}'")
print(f"s.lower() = '{s.lower()}'")
print(f"s.upper() = '{s.upper()}'")
print(f"s.strip() = '{s.strip()}'")
print(f"s.split() = {s.split()}")
print(f"s.replace('Hello', 'Hi') = '{s.replace('Hello', 'Hi')}'")
print(f"s.find('World') = {s.find('World')}")
print(f"s.startswith('Hello') = {s.startswith('Hello')}")
print(f"s.endswith('World') = {s.endswith('World')}")

# 7. 格式化
print("\n=== 格式化 ===")
name = "Alice"
age = 25

# f-string (推荐)
print(f"姓名: {name}, 年龄: {age}")

# format 方法
print("姓名: {}, 年龄: {}".format(name, age))

# % 格式化
print("姓名: %s, 年龄: %d" % (name, age))

# 格式化数字
pi = 3.14159
print(f"PI = {pi:.2f}")
print(f"PI = {pi:.4f}")
