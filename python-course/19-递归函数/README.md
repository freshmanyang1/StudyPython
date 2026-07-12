# 递归函数

## 学习目标

- 理解递归的概念
- 掌握递归函数的编写
- 了解递归的终止条件
- 掌握递归的应用

## 知识点

### 1. 递归的概念

递归是指函数调用自身的过程。

### 2. 终止条件

递归必须有终止条件，否则会无限递归。

```python
def factorial(n):
    if n == 0:  # 终止条件
        return 1
    return n * factorial(n - 1)
```

### 3. 阶乘

```python
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # 120
```

### 4. 斐波那契数列

```python
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(10))  # 55
```

### 5. 递归的优缺点

**优点**：
- 代码简洁
- 逻辑清晰

**缺点**：
- 效率较低
- 可能导致栈溢出

## 示例说明

`demo.py` 文件包含了本课程的示例代码，展示了：
- 递归的概念
- 终止条件
- 阶乘和斐波那契数列

## 参考资料

- 廖雪峰 Python 教程：https://liaoxuefeng.com/books/python/introduction/index.html
- 菜鸟教程 Python3：https://www.runoob.com/python3/python3-tutorial.html
