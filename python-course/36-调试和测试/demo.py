# -*- coding: utf-8 -*-
"""
课程：调试和测试
演示：print 调试、assert、unittest
"""

import unittest

# 1. print 调试
print("=== print 调试 ===")
def calculate(x, y):
    print(f"x = {x}, y = {y}")
    result = x + y
    print(f"result = {result}")
    return result

calculate(3, 5)

# 2. assert 语句
print("\n=== assert 语句 ===")
def add(a, b):
    return a + b

assert add(1, 2) == 3
assert add(0, 0) == 0
print("所有断言通过")

# 3. unittest 模块
print("\n=== unittest 模块 ===")
class TestMath(unittest.TestCase):
    def test_add(self):
        self.assertEqual(1 + 1, 2)

    def test_subtract(self):
        self.assertEqual(5 - 3, 2)

# 运行测试
if __name__ == '__main__':
    unittest.main(argv=[''], exit=False, verbosity=2)
