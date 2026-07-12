# 高阶函数

## 学习目标

- 理解高阶函数的概念
- 掌握 map、reduce、filter 函数
- 了解 sorted 函数的使用
- 掌握匿名函数 lambda

## 知识点

### 1. 高阶函数的概念

高阶函数是指接受函数作为参数或返回函数的函数。

```python
def apply(func, value):
    return func(value)

def square(x):
    return x ** 2

result = apply(square, 5)
print(result)  # 25
```

### 2. map 函数

```python
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2, numbers))
print(squares)  # [1, 4, 9, 16, 25]
```

### 3. reduce 函数

```python
from functools import reduce

numbers = [1, 2, 3, 4, 5]
total = reduce(lambda x, y: x + y, numbers)
print(total)  # 15
```

### 4. filter 函数

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even = list(filter(lambda x: x % 2 == 0, numbers))
print(even)  # [2, 4, 6, 8, 10]
```

### 5. sorted 函数

```python
# 基本排序
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
sorted_numbers = sorted(numbers)
print(sorted_numbers)  # [1, 1, 2, 3, 4, 5, 6, 9]

# 自定义排序
students = [("Alice", 85), ("Bob", 92), ("Charlie", 78)]
sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students)
```

### 6. 匿名函数 lambda

```python
# 基本语法
square = lambda x: x ** 2
print(square(5))  # 25

# 多个参数
add = lambda x, y: x + y
print(add(3, 5))  # 8
```

### 7. 返回函数

```python
def make_adder(n):
    def adder(x):
        return x + n
    return adder

add5 = make_adder(5)
print(add5(10))  # 15
```

### 8. 闭包

```python
def counter():
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    return increment

c = counter()
print(c())  # 1
print(c())  # 2
print(c())  # 3
```

## 示例说明

`demo.py` 文件包含了本课程的示例代码，展示了：
- 高阶函数的概念
- map、reduce、filter 函数
- sorted 函数的使用
- 匿名函数 lambda
- 返回函数和闭包

## 参考资料

- 廖雪峰 Python 教程：https://liaoxuefeng.com/books/python/introduction/index.html
- 菜鸟教程 Python3：https://www.runoob.com/python3/python3-tutorial.html
