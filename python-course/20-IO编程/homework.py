# -*- coding: utf-8 -*-
"""
课程：IO编程
作业要求：
1. 编写一个函数 write_file(filename, content)，将内容写入文件
2. 编写一个函数 read_file(filename)，读取文件内容
3. 编写一个函数 count_lines(filename)，统计文件行数
4. 编写一个函数 find_files(directory, extension)，查找指定扩展名的文件

完成后输入 `python，提交作业` 提交。
"""

import os
from pathlib import Path

# 作业1：写入文件
# 请在此处填写代码
def write_file(filename, content):
    pass

# 作业2：读取文件
# 请在此处填写代码
def read_file(filename):
    pass

# 作业3：统计行数
# 请在此处填写代码
def count_lines(filename):
    pass

# 作业4：查找文件
# 请在此处填写代码
def find_files(directory, extension):
    pass

# 测试代码（不要修改）
if __name__ == "__main__":
    print("测试作业1 - 写入文件:")
    write_file('test_homework.txt', 'Hello, Python!')
    print("文件写入完成")

    print("\n测试作业2 - 读取文件:")
    content = read_file('test_homework.txt')
    print(f"内容: {content}")

    print("\n测试作业3 - 统计行数:")
    lines = count_lines('test_homework.txt')
    print(f"行数: {lines}")

    print("\n测试作业4 - 查找文件:")
    py_files = find_files('.', '.py')
    print(f"Python 文件: {py_files[:3]}...")

    # 清理
    os.remove('test_homework.txt')
