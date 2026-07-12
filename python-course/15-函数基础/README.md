# 函数基础

## 学习目标

- 理解什么是函数
- 掌握定义函数的方法
- 掌握调用函数的方法
- 了解函数文档字符串

## 知识点

### 1. 什么是函数

函数是一段可重复使用的代码块，用于完成特定任务。

**函数的好处**：
- 代码复用
- 代码组织
- 易于维护

### 2. 定义函数

```python
def greet():
    print("Hello, World!")
```

### 3. 调用函数

```python
greet()  # 输出：Hello, World!
```

### 4. 函数文档字符串

```python
def greet():
    """
    打招呼函数
    输出 Hello, World!
    """
    print("Hello, World!")

# 查看文档
print(greet.__doc__)
```

### 5. 内置函数

Python 提供了许多内置函数：

```python
print("Hello")  # 输出
len("Hello")    # 长度
type(10)        # 类型
int("123")      # 转换为整数
str(123)        # 转换为字符串
```

## 示例说明

`demo.py` 文件包含了本课程的示例代码，展示了：
- 函数的定义和调用
- 函数文档字符串
- 内置函数的使用

## 参考资料

- 廖雪峰 Python 教程：https://liaoxuefeng.com/books/python/introduction/index.html
- 菜鸟教程 Python3：https://www.runoob.com/python3/python3-tutorial.html
