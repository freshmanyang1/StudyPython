# -*- coding: utf-8 -*-
"""
课程：数据类型转换
演示：类型转换函数、类型检查、隐式转换、显式转换
"""

# 1. 类型转换函数
print("=== 类型转换函数 ===")
# 转换为整数
print(f"int('123') = {int('123')}")
print(f"int(3.14) = {int(3.14)}")
print(f"int(True) = {int(True)}")
print(f"int(False) = {int(False)}")

# 转换为浮点数
print(f"float('3.14') = {float('3.14')}")
print(f"float(10) = {float(10)}")
print(f"float(True) = {float(True)}")

# 转换为字符串
print(f"str(123) = {str(123)}")
print(f"str(3.14) = {str(3.14)}")
print(f"str(True) = {str(True)}")
print(f"str(None) = {str(None)}")

# 转换为布尔值
print(f"bool(0) = {bool(0)}")
print(f"bool('') = {bool('')}")
print(f"bool(None) = {bool(None)}")
print(f"bool(1) = {bool(1)}")
print(f"bool('hello') = {bool('hello')}")

# 2. 类型检查
print("\n=== 类型检查 ===")
x = 10
print(f"type(x) = {type(x)}")
print(f"isinstance(x, int) = {isinstance(x, int)}")

y = "hello"
print(f"type(y) = {type(y)}")
print(f"isinstance(y, str) = {isinstance(y, str)}")

# 3. 隐式转换
print("\n=== 隐式转换 ===")
result = 1 + 2.0
print(f"1 + 2.0 = {result} (类型: {type(result)})")

s = "Hello" + " " + "World"
print(f"'Hello' + ' ' + 'World' = {s}")

# 4. 显式转换
print("\n=== 显式转换 ===")
num = int("123")
print(f"int('123') = {num}")

s = str(123)
print(f"str(123) = {s}")

f = float("3.14")
print(f"float('3.14') = {f}")

# 5. 常见转换场景
print("\n=== 常见转换场景 ===")
# 数字格式化
price = 99.9
print(f"价格: {price:.2f} 元")

# 列表转字符串
words = ["Hello", "World"]
sentence = " ".join(words)
print(f"列表转字符串: {sentence}")

# 字符串转列表
s = "Hello World"
words = s.split()
print(f"字符串转列表: {words}")
