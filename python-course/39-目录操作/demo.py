# -*- coding: utf-8 -*-
"""
课程：目录操作
演示：创建目录、列出目录、遍历目录、查找文件
"""

import os
from pathlib import Path

# 1. 创建目录
print("=== 创建目录 ===")
os.makedirs('test_dir', exist_ok=True)
print("目录创建完成")

# 2. 列出目录
print("\n=== 列出目录 ===")
files = os.listdir('.')
print(f"当前目录文件: {files[:5]}...")

# 3. 遍历目录
print("\n=== 遍历目录 ===")
print("当前目录文件:")
for p in Path('.').iterdir():
    if p.is_file():
        print(f"  {p.name}")

# 4. 查找文件
print("\n=== 查找文件 ===")
print("Python 文件:")
for p in Path('.').glob('*.py'):
    print(f"  {p.name}")

# 5. 清理
os.rmdir('test_dir')
print("\n目录已删除")
