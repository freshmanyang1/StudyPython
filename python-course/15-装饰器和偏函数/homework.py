# -*- coding: utf-8 -*-
"""
课程：装饰器和偏函数
作业要求：
1. 编写一个装饰器 log，记录函数的调用时间和执行时间
2. 编写一个装饰器 cache，缓存函数的计算结果
3. 使用 partial 创建一个 int2 函数，将二进制字符串转换为整数
4. 使用 partial 创建一个 double 函数，将数字乘以 2

完成后输入 `python，提交作业` 提交。
"""

import functools
from functools import partial

# 作业1：日志装饰器
# 请在此处填写代码
def log(func):
    pass

# 作业2：缓存装饰器
# 请在此处填写代码
def cache(func):
    pass

# 作业3：二进制转换
# 请在此处填写代码
def homework3():
    pass

# 作业4：double 函数
# 请在此处填写代码
def homework4():
    pass

# 测试代码（不要修改）
if __name__ == "__main__":
    print("测试作业1 - 日志装饰器:")
    @log
    def add(a, b):
        return a + b
    print(f"add(3, 5) = {add(3, 5)}")

    print("\n测试作业2 - 缓存装饰器:")
    @cache
    def fibonacci(n):
        if n <= 1:
            return n
        return fibonacci(n - 1) + fibonacci(n - 2)
    print(f"fibonacci(10) = {fibonacci(10)}")

    print("\n测试作业3 - 二进制转换:")
    homework3()
    print("\n测试作业4 - double 函数:")
    homework4()
