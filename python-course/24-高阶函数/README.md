# 高阶函数

## 学习目标

- 理解高阶函数的概念
- 掌握 map、reduce、filter 函数
- 了解 sorted 函数的使用

## 知识点

### 1. 高阶函数的概念

高阶函数是指接受函数作为参数或返回函数的函数。

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
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
sorted_numbers = sorted(numbers)
print(sorted_numbers)  # [1, 1, 2, 3, 4, 5, 6, 9]
```

## 示例说明

`demo.py` 文件包含了本课程的示例代码，展示了：
- 高阶函数的概念
- map、reduce、filter 函数
- sorted 函数

## 参考资料

- 廖雪峰 Python 教程：https://liaoxuefeng.com/books/python/introduction/index.html
- 菜鸟教程 Python3：https://www.runoob.com/python3/python3-tutorial.html
