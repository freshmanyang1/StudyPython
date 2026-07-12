# -*- coding: utf-8 -*-
"""
课程：IO编程
演示：文件读写、路径处理、目录操作
"""

import os
from pathlib import Path

# 1. 文件写入
print("=== 文件写入 ===")
with open('test.txt', 'w') as f:
    f.write('Hello, World!\n')
    f.write('Python IO 编程\n')
print("文件写入完成")

# 2. 文件读取
print("\n=== 文件读取 ===")
with open('test.txt', 'r') as f:
    content = f.read()
    print(content)

# 3. 逐行读取
print("\n=== 逐行读取 ===")
with open('test.txt', 'r') as f:
    for line in f:
        print(f"行: {line.strip()}")

# 4. 追加写入
print("\n=== 追加写入 ===")
with open('test.txt', 'a') as f:
    f.write('追加的内容\n')

with open('test.txt', 'r') as f:
    print(f.read())

# 5. 文件路径 - pathlib
print("\n=== 文件路径 - pathlib ===")
p = Path('test.txt')
print(f"文件名: {p.name}")
print(f"扩展名: {p.suffix}")
print(f"父目录: {p.parent}")
print(f"是否存在: {p.exists()}")
print(f"是否是文件: {p.is_file()}")
print(f"是否是目录: {p.is_dir()}")

# 6. 目录操作
print("\n=== 目录操作 ===")
# 创建目录
os.makedirs('test_dir', exist_ok=True)
print("目录创建完成")

# 列出目录
files = os.listdir('.')
print(f"当前目录文件: {files[:5]}...")

# 7. pathlib 目录操作
print("\n=== pathlib 目录操作 ===")
# 创建目录
Path('test_dir2').mkdir(exist_ok=True)

# 遍历目录
print("当前目录文件:")
for p in Path('.').iterdir():
    if p.is_file():
        print(f"  {p.name}")

# 8. 查找文件
print("\n=== 查找文件 ===")
print("Python 文件:")
for p in Path('.').glob('*.py'):
    print(f"  {p.name}")

# 9. 文件信息
print("\n=== 文件信息 ===")
size = os.path.getsize('test.txt')
print(f"文件大小: {size} 字节")

abs_path = os.path.abspath('test.txt')
print(f"绝对路径: {abs_path}")

# 10. 清理
print("\n=== 清理 ===")
os.remove('test.txt')
os.rmdir('test_dir')
os.rmdir('test_dir2')
print("清理完成")
