# -*- coding: utf-8 -*-
"""
课程：目录操作
作业要求：
1. 编写一个函数 create_dir(path)，创建目录
2. 编写一个函数 list_files(path)，列出目录下的所有文件
3. 编写一个函数 find_files(path, extension)，查找指定扩展名的文件

完成后输入 `python，提交作业` 提交。
"""

import os
from pathlib import Path

# 作业1：创建目录
# 请在此处填写代码
def create_dir(path):
    pass

# 作业2：列出文件
# 请在此处填写代码
def list_files(path):
    pass

# 作业3：查找文件
# 请在此处填写代码
def find_files(path, extension):
    pass

# 测试代码（不要修改）
if __name__ == "__main__":
    print("测试作业1 - 创建目录:")
    create_dir('test_homework_dir')
    print("目录创建完成")

    print("\n测试作业2 - 列出文件:")
    files = list_files('.')
    print(f"文件: {files[:3]}...")

    print("\n测试作业3 - 查找文件:")
    py_files = find_files('.', '.py')
    print(f"Python 文件: {py_files[:3]}...")

    # 清理
    os.rmdir('test_homework_dir')
