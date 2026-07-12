# -*- coding: utf-8 -*-
"""
课程：错误调试和测试
演示：异常处理、调试、单元测试
"""

import unittest
import logging

# 1. 异常处理
print("=== 异常处理 ===")
try:
    result = 10 / 0
except ZeroDivisionError:
    print("除数不能为零")
except Exception as e:
    print(f"发生错误: {e}")
else:
    print("没有错误")
finally:
    print("总是执行")

# 2. 自定义异常
print("\n=== 自定义异常 ===")
class MyError(Exception):
    pass

def foo():
    raise MyError("自定义错误")

try:
    foo()
except MyError as e:
    print(f"捕获到: {e}")

# 3. 调试技巧
print("\n=== 调试技巧 ===")
x = 10
print(f"变量值: {x}")

# 断言
assert x > 0, "x 必须是正数"
print("断言通过")

# 4. logging
print("\n=== logging ===")
logging.basicConfig(level=logging.DEBUG)
logging.debug("调试信息")
logging.info("信息")
logging.warning("警告")
logging.error("错误")

# 5. 单元测试
print("\n=== 单元测试 ===")
class TestMath(unittest.TestCase):
    def test_add(self):
        self.assertEqual(1 + 1, 2)

    def test_subtract(self):
        self.assertEqual(5 - 3, 2)

    def test_multiply(self):
        self.assertEqual(2 * 3, 6)

    def test_divide(self):
        self.assertEqual(10 / 2, 5)

# 运行测试
if __name__ == '__main__':
    unittest.main(argv=[''], exit=False, verbosity=2)

# 6. 测试方法
print("\n=== 测试方法 ===")
class TestMethods(unittest.TestCase):
    def test_assertions(self):
        self.assertEqual(1 + 1, 2)
        self.assertNotEqual(1 + 1, 3)
        self.assertTrue(True)
        self.assertFalse(False)
        self.assertIsNone(None)
        self.assertIn(1, [1, 2, 3])

if __name__ == '__main__':
    unittest.main(argv=[''], exit=False, verbosity=2)

# 7. setUp 和 tearDown
print("\n=== setUp 和 tearDown ===")
class TestSetup(unittest.TestCase):
    def setUp(self):
        self.data = [1, 2, 3]
        print("setUp 执行")

    def tearDown(self):
        print("tearDown 执行")

    def test_sum(self):
        self.assertEqual(sum(self.data), 6)

    def test_len(self):
        self.assertEqual(len(self.data), 3)

if __name__ == '__main__':
    unittest.main(argv=[''], exit=False, verbosity=2)
