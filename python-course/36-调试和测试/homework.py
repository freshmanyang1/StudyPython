# -*- coding: utf-8 -*-
"""
课程：调试和测试
作业要求：
1. 编写一个函数 multiply(a, b)，计算两个数的乘积
2. 使用 assert 语句验证函数的正确性
3. 使用 unittest 编写测试用例

完成后输入 `python，提交作业` 提交。
"""

import unittest

# 作业1：定义 multiply 函数
# 请在此处填写代码
def multiply(a, b):
    pass

# 作业2：使用 assert 验证
# 请在此处填写代码
def homework2():
    pass

# 作业3：使用 unittest 编写测试
# 请在此处填写代码
class TestMultiply(unittest.TestCase):
    pass

# 测试代码（不要修改）
if __name__ == "__main__":
    print("测试作业1 - multiply 函数:")
    print(f"multiply(3, 5) = {multiply(3, 5)}")
    print(f"multiply(0, 10) = {multiply(0, 10)}")

    print("\n测试作业2 - assert 验证:")
    homework2()

    print("\n测试作业3 - unittest 测试:")
    unittest.main(argv=[''], exit=False, verbosity=2)
