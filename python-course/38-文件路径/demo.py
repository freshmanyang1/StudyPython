# -*- coding: utf-8 -*-
"""
课程：文件路径
演示：os.path 模块、pathlib 模块、路径操作
"""

import os
from pathlib import Path

# 1. os.path 模块
print("=== os.path 模块 ===")
print(f"当前目录: {os.getcwd()}")
print(f"文件存在: {os.path.exists('demo.py')}")
print(f"是否是文件: {os.path.isfile('demo.py')}")
print(f"是否是目录: {os.path.isdir('.')}")

# 2. pathlib 模块
print("\n=== pathlib 模块 ===")
p = Path('demo.py')
print(f"文件名: {p.name}")
print(f"扩展名: {p.suffix}")
print(f"父目录: {p.parent}")
print(f"是否存在: {p.exists()}")
print(f"是否是文件: {p.is_file()}")

# 3. 路径操作
print("\n=== 路径操作 ===")
p = Path('test') / 'dir' / 'file.txt'
print(f"路径: {p}")
print(f"父目录: {p.parent}")
print(f"文件名: {p.name}")
