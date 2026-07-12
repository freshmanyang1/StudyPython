# -*- coding: utf-8 -*-
"""
课程：错误调试和测试
作业要求：
1. 编写一个函数 divide(a, b)，处理除数为零的异常
2. 编写一个自定义异常 InvalidAgeError，用于验证年龄
3. 编写一个函数 validate_age(age)，使用自定义异常
4. 为 validate_age 函数编写单元测试

完成后输入 `python，提交作业` 提交。
"""

import unittest

# 作业1：除法函数
# 请在此处填写代码
def divide(a, b):
    pass

# 作业2：自定义异常
# 请在此处填写代码
class InvalidAgeError(Exception):
    pass

# 作业3：验证年龄函数
# 请在此处填写代码
def validate_age(age):
    pass

# 作业4：单元测试
# 请在此处填写代码
class TestValidateAge(unittest.TestCase):
    pass

# 测试代码（不要修改）
if __name__ == "__main__":
    print("测试作业1 - 除法函数:")
    print(f"divide(10, 2) = {divide(10, 2)}")
    print(f"divide(10, 0) = {divide(10, 0)}")

    print("\n测试作业2 - 自定义异常:")
    try:
        validate_age(-5)
    except InvalidAgeError as e:
        print(f"捕获到: {e}")

    print("\n测试作业3 - 验证年龄:")
    try:
        validate_age(25)
        print("年龄有效")
    except InvalidAgeError as e:
        print(f"错误: {e}")

    print("\n测试作业4 - 单元测试:")
    unittest.main(argv=[''], exit=False, verbosity=2)
