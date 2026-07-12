# -*- coding: utf-8 -*-
"""
课程：文件读写
演示：open() 函数、read()、write()、with 语句
"""

import os

# 1. 写入文件
print("=== 写入文件 ===")
with open('test.txt', 'w') as f:
    f.write('Hello, World!\n')
    f.write('Python 文件读写\n')
print("文件写入完成")

# 2. 读取文件
print("\n=== 读取文件 ===")
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

# 5. 清理
os.remove('test.txt')
print("文件已删除")
