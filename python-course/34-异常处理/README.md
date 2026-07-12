# 异常处理

## 学习目标

- 掌握 try-except 语句的使用
- 了解常见异常类型
- 掌握 finally 语句的使用

## 知识点

### 1. try-except 语句

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("除数不能为零")
```

### 2. 常见异常类型

```python
# ZeroDivisionError - 除零错误
# ValueError - 值错误
# TypeError - 类型错误
# IndexError - 索引错误
# KeyError - 键错误
# FileNotFoundError - 文件未找到
```

### 3. 捕获多个异常

```python
try:
    # 代码
except (ValueError, TypeError) as e:
    print(f"错误: {e}")
```

### 4. finally 语句

```python
try:
    # 代码
except Exception as e:
    print(f"错误: {e}")
finally:
    print("总是执行")
```

## 示例说明

`demo.py` 文件包含了本课程的示例代码，展示了：
- try-except 语句
- 常见异常类型
- 捕获多个异常
- finally 语句

## 参考资料

- 廖雪峰 Python 教程：https://liaoxuefeng.com/books/python/introduction/index.html
- 菜鸟教程 Python3：https://www.runoob.com/python3/python3-tutorial.html
