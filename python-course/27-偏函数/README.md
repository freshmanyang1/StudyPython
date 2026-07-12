# 偏函数

## 学习目标

- 理解偏函数的概念
- 掌握 functools.partial 的使用
- 了解偏函数的使用场景

## 知识点

### 1. 偏函数的概念

偏函数是指固定函数的部分参数，返回一个新的函数。

### 2. functools.partial

```python
from functools import partial

def add(x, y):
    return x + y

add5 = partial(add, 5)
print(add5(10))  # 15
```

### 3. 使用场景

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
- 偏函数的概念
- functools.partial 的使用
- 偏函数的使用场景

## 参考资料

- 廖雪峰 Python 教程：https://liaoxuefeng.com/books/python/introduction/index.html
- 菜鸟教程 Python3：https://www.runoob.com/python3/python3-tutorial.html
