# 调试和测试

## 学习目标

- 掌握 print 调试的方法
- 了解 assert 语句的使用
- 掌握 unittest 模块的基本使用

## 知识点

### 1. print 调试

```python
def calculate(x, y):
    print(f"x = {x}, y = {y}")  # 调试输出
    result = x + y
    print(f"result = {result}")  # 调试输出
    return result
```

### 2. assert 语句

```python
def add(a, b):
    return a + b

# 断言
assert add(1, 2) == 3
assert add(0, 0) == 0
```

### 3. unittest 模块

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

### 4. 测试方法

```python
self.assertEqual(a, b)      # a == b
self.assertNotEqual(a, b)   # a != b
self.assertTrue(x)          # x is True
self.assertFalse(x)         # x is False
self.assertIsNone(x)        # x is None
self.assertIn(a, b)         # a in b
self.assertRaises(Error)    # 抛出异常
```

## 示例说明

`demo.py` 文件包含了本课程的示例代码，展示了：
- print 调试
- assert 语句
- unittest 模块

## 参考资料

- 廖雪峰 Python 教程：https://liaoxuefeng.com/books/python/introduction/index.html
- 菜鸟教程 Python3：https://www.runoob.com/python3/python3-tutorial.html
