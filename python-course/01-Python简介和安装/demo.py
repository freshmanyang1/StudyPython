# -*- coding: utf-8 -*-
"""
课程：Python简介和安装
演示：Python 基本输出和执行方式
"""

# 1. 基本输出
print("Hello, World!")
print("你好，Python！")

# 2. 输出多个值
print("姓名:", "张三")
print("年龄:", 25)

# 3. 使用 sep 参数指定分隔符
print("2024", "01", "01", sep="-")

# 4. 使用 end 参数指定结尾
print("Hello", end=" ")
print("World")

# 5. 输出空行
print()

# 6. 输出数字
print(42)
print(3.14)

# 7. 输出表达式结果
print(1 + 2)
print("Hello" + " " + "Python")

# 8. 查看 Python 版本
import sys
print(f"Python 版本: {sys.version}")
