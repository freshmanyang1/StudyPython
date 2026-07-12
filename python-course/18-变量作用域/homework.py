# -*- coding: utf-8 -*-
"""
课程：变量作用域
作业要求：
1. 定义一个全局变量 count，值为 0
2. 定义一个函数 increment()，使用 global 关键字将 count 加 1
3. 定义一个函数 counter()，使用 nonlocal 关键字实现计数器

完成后输入 `python，提交作业` 提交。
"""

# 作业1：定义全局变量
count = 0

# 作业2：使用 global 关键字
# 请在此处填写代码
def increment():
    pass

# 作业3：使用 nonlocal 关键字
# 请在此处填写代码
def counter():
    pass

# 测试代码（不要修改）
if __name__ == "__main__":
    print("测试作业1 - 全局变量:")
    print(f"count = {count}")

    print("\n测试作业2 - 使用 global 关键字:")
    increment()
    print(f"increment() 后: count = {count}")
    increment()
    print(f"increment() 后: count = {count}")

    print("\n测试作业3 - 使用 nonlocal 关键字:")
    c = counter()
    print(f"counter() = {c}")
