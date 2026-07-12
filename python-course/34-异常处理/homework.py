# -*- coding: utf-8 -*-
"""
课程：异常处理
作业要求：
1. 编写一个函数 divide(a, b)，处理除数为零的异常
2. 编写一个函数 convert_int(s)，处理字符串转整数的异常
3. 编写一个函数 get_value(d, key)，处理字典键不存在的异常

完成后输入 `python，提交作业` 提交。
"""

# 作业1：处理除零异常
# 请在此处填写代码
def divide(a, b):
    pass

# 作业2：处理转换异常
# 请在此处填写代码
def convert_int(s):
    pass

# 作业3：处理键不存在异常
# 请在此处填写代码
def get_value(d, key):
    pass

# 测试代码（不要修改）
if __name__ == "__main__":
    print("测试作业1 - 处理除零异常:")
    print(f"divide(10, 2) = {divide(10, 2)}")
    print(f"divide(10, 0) = {divide(10, 0)}")

    print("\n测试作业2 - 处理转换异常:")
    print(f"convert_int('123') = {convert_int('123')}")
    print(f"convert_int('abc') = {convert_int('abc')}")

    print("\n测试作业3 - 处理键不存在异常:")
    d = {"a": 1, "b": 2}
    print(f"get_value(d, 'a') = {get_value(d, 'a')}")
    print(f"get_value(d, 'c') = {get_value(d, 'c')}")
