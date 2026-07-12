# 递归函数

## 学习目标

- 理解递归的概念
- 掌握递归函数的编写
- 了解递归的应用场景
- 掌握递归的终止条件

## 知识点

### 1. 递归的概念

递归是指函数调用自身的过程。

```python
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # 120
```

### 2. 递归的终止条件

递归必须有终止条件，否则会无限递归。

```python
# 错误：没有终止条件
def infinite_recursion():
    infinite_recursion()

# 正确：有终止条件
def countdown(n):
    if n <= 0:
        print("Done!")
        return
    print(n)
    countdown(n - 1)
```

### 3. 递归的应用

**阶乘：**
```python
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)
```

**斐波那契数列：**
```python
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
```

**幂运算：**
```python
def power(base, exponent):
    if exponent == 0:
        return 1
    return base * power(base, exponent - 1)
```

### 4. 递归的优缺点

**优点：**
- 代码简洁
- 逻辑清晰
- 适合解决递归问题

**缺点：**
- 效率较低
- 可能导致栈溢出
- 调试困难

### 5. 尾递归优化

Python 不支持尾递归优化，但可以了解概念。

```python
# 尾递归形式
def factorial_tail(n, accumulator=1):
    if n == 0:
        return accumulator
    return factorial_tail(n - 1, n * accumulator)
```

## 示例说明

`demo.py` 文件包含了本课程的示例代码，展示了：
- 递归的基本概念
- 递归的终止条件
- 递归的应用场景
- 递归的优缺点

## 参考资料

- 廖雪峰 Python 教程：https://liaoxuefeng.com/books/python/introduction/index.html
- 菜鸟教程 Python3：https://www.runoob.com/python3/python3-tutorial.html
