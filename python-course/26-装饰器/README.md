# 装饰器

## 学习目标

- 理解装饰器的概念
- 掌握装饰器的编写
- 了解装饰器的使用
- 掌握带参数的装饰器

## 知识点

### 1. 装饰器的概念

装饰器是一种高阶函数，用于修改或增强其他函数的功能。

### 2. 基本装饰器

```python
def my_decorator(func):
    def wrapper():
        print("函数执行前")
        func()
        print("函数执行后")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
```

### 3. 带参数的装饰器

```python
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    print(f"Hello, {name}!")
```

### 4. 保留原函数信息

```python
import functools

def my_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper
```

## 示例说明

`demo.py` 文件包含了本课程的示例代码，展示了：
- 装饰器的概念
- 装饰器的编写
- 装饰器的使用
- 带参数的装饰器

## 参考资料

- 廖雪峰 Python 教程：https://liaoxuefeng.com/books/python/introduction/index.html
- 菜鸟教程 Python3：https://www.runoob.com/python3/python3-tutorial.html
