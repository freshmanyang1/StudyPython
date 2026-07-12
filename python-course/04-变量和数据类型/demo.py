# -*- coding: utf-8 -*-
"""
课程：变量和数据类型
演示：变量定义、数据类型、类型检查、类型转换
"""

# 1. 变量定义
print("=== 变量定义 ===")
x = 10
name = "Alice"
pi = 3.14
is_true = True

print(f"x = {x}")
print(f"name = {name}")
print(f"pi = {pi}")
print(f"is_true = {is_true}")

# 2. 整数 (int)
print("\n=== 整数 (int) ===")
a = 10
b = -5
c = 0
d = 0b1010  # 二进制
e = 0o12    # 八进制
f = 0xa     # 十六进制

print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")
print(f"二进制 0b1010 = {d}")
print(f"八进制 0o12 = {e}")
print(f"十六进制 0xa = {f}")

# 3. 浮点数 (float)
print("\n=== 浮点数 (float) ===")
x = 3.14
y = -0.5
z = 1.0
e = 1.5e10  # 科学计数法

print(f"x = {x}")
print(f"y = {y}")
print(f"z = {z}")
print(f"科学计数法 1.5e10 = {e}")

# 4. 字符串 (str)
print("\n=== 字符串 (str) ===")
s1 = "Hello"
s2 = 'World'
s3 = """多行
字符串"""

print(f"s1 = {s1}")
print(f"s2 = {s2}")
print(f"s3 = {s3}")

# 5. 布尔值 (bool)
print("\n=== 布尔值 (bool) ===")
is_true = True
is_false = False

print(f"is_true = {is_true}")
print(f"is_false = {is_false}")
print(f"True and True = {True and True}")
print(f"True or False = {True or False}")
print(f"not True = {not True}")

# 6. 空值 (None)
print("\n=== 空值 (None) ===")
x = None
print(f"x = {x}")
print(f"type(x) = {type(x)}")

# 7. 类型检查
print("\n=== 类型检查 ===")
print(f"type(10) = {type(10)}")
print(f"type(3.14) = {type(3.14)}")
print(f"type('hello') = {type('hello')}")
print(f"type(True) = {type(True)}")
print(f"type(None) = {type(None)}")

# 8. 类型转换
print("\n=== 类型转换 ===")
# 转换为整数
print(f"int('123') = {int('123')}")
print(f"int(3.14) = {int(3.14)}")
print(f"int(True) = {int(True)}")

# 转换为浮点数
print(f"float('3.14') = {float('3.14')}")
print(f"float(10) = {float(10)}")

# 转换为字符串
print(f"str(123) = {str(123)}")
print(f"str(3.14) = {str(3.14)}")
print(f"str(True) = {str(True)}")

# 转换为布尔值
print(f"bool(0) = {bool(0)}")
print(f"bool('') = {bool('')}")
print(f"bool(None) = {bool(None)}")
print(f"bool(1) = {bool(1)}")
print(f"bool('hello') = {bool('hello')}")
