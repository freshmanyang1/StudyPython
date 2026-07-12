# 装饰器和偏函数

## 学习目标

- 理解装饰器的概念
- 掌握装饰器的编写和使用
- 了解偏函数的概念
- 掌握 functools.partial 的使用

## 知识点

### 1. 装饰器的概念

装饰器是一种高阶函数，用于修改或增强其他函数的功能。

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

### 2. 带参数的装饰器

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

### 3. 保留原函数信息

```python
import functools

def my_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper
```

### 4. 类装饰器

```python
class Timer:
    def __init__(self, func):
        self.func = func
    
    def __call__(self, *args, **kwargs):
        import time
        start = time.time()
        result = self.func(*args, **kwargs)
        end = time.time()
        print(f"执行时间: {end - start} 秒")
        return result

@Timer
def slow_function():
    import time
    time.sleep(1)
```

### 5. 偏函数

偏函数是指固定函数的部分参数，返回一个新的函数。

```python
from functools import partial

def add(x, y):
    return x + y

add5 = partial(add, 5)
print(add5(10))  # 15
```

### 6. partial 的应用

```python
from functools import partial

# 固定参数
int2 = partial(int, base=2)
print(int2('1010'))  # 10

# 固定多个参数
def power(base, exponent):
    return base ** exponent

square = partial(power, exponent=2)
cube = partial(power, exponent=3)

print(square(5))  # 25
print(cube(3))    # 27
```

## 示例说明

`demo.py` 文件包含了本课程的示例代码，展示了：
- 装饰器的概念和编写
- 带参数的装饰器
- 类装饰器
- 偏函数的使用

## 参考资料

- 廖雪峰 Python 教程：https://liaoxuefeng.com/books/python/introduction/index.html
- 菜鸟教程 Python3：https://www.runoob.com/python3/python3-tutorial.html
