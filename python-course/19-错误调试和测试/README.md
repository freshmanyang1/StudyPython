# 错误调试和测试

## 学习目标

- 掌握异常处理
- 了解调试技巧
- 掌握单元测试
- 了解测试框架

## 知识点

### 1. 异常处理

```python
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
```

### 2. 自定义异常

```python
class MyError(Exception):
    pass

def foo():
    raise MyError("自定义错误")

try:
    foo()
except MyError as e:
    print(e)
```

### 3. 调试技巧

```python
# 使用 print
print(f"变量值: {x}")

# 使用断言
assert x > 0, "x 必须是正数"

# 使用 logging
import logging
logging.debug("调试信息")
logging.info("信息")
logging.warning("警告")
logging.error("错误")
```

### 4. 单元测试

```python
import unittest

class TestMath(unittest.TestCase):
    def test_add(self):
        self.assertEqual(1 + 1, 2)
    
    def test_subtract(self):
        self.assertEqual(5 - 3, 2)

if __name__ == '__main__':
    unittest.main()
```

### 5. 测试方法

```python
self.assertEqual(a, b)      # a == b
self.assertNotEqual(a, b)   # a != b
self.assertTrue(x)          # x is True
self.assertFalse(x)         # x is False
self.assertIsNone(x)        # x is None
self.assertIn(a, b)         # a in b
self.assertRaises(Error)    # 抛出异常
```

### 6. setUp 和 tearDown

```python
class TestMath(unittest.TestCase):
    def setUp(self):
        # 测试前执行
        self.data = [1, 2, 3]
    
    def tearDown(self):
        # 测试后执行
        pass
    
    def test_sum(self):
        self.assertEqual(sum(self.data), 6)
```

### 7. pytest 框架

```python
# test_math.py
def test_add():
    assert 1 + 1 == 2

def test_subtract():
    assert 5 - 3 == 2
```

## 示例说明

`demo.py` 文件包含了本课程的示例代码，展示了：
- 异常处理
- 自定义异常
- 调试技巧
- 单元测试

## 参考资料

- 廖雪峰 Python 教程：https://liaoxuefeng.com/books/python/introduction/index.html
- 菜鸟教程 Python3：https://www.runoob.com/python3/python3-tutorial.html
