# 切片和迭代

## 学习目标

- 掌握切片操作符的使用
- 了解迭代器和可迭代对象
- 掌握 for 循环的迭代机制
- 了解 enumerate、zip 等内置函数

## 知识点

### 1. 切片操作符

```python
# 基本切片
lst = [0, 1, 2, 3, 4, 5]
lst[1:4]    # [1, 2, 3]
lst[:3]     # [0, 1, 2]
lst[3:]     # [3, 4, 5]
lst[::2]    # [0, 2, 4]
lst[::-1]   # [5, 4, 3, 2, 1, 0]
```

### 2. 字符串切片

```python
s = "Hello World"
s[0:5]      # "Hello"
s[6:]       # "World"
s[::-1]     # "dlroW olleH"
```

### 3. 元组切片

```python
t = (1, 2, 3, 4, 5)
t[1:3]      # (2, 3)
```

### 4. 可迭代对象

可迭代对象是可以被遍历的对象：
- 列表、元组、字符串
- 字典、集合
- 文件对象
- 生成器

### 5. 迭代器

迭代器是实现了 `__iter__()` 和 `__next__()` 方法的对象。

```python
lst = [1, 2, 3]
it = iter(lst)
print(next(it))  # 1
print(next(it))  # 2
print(next(it))  # 3
```

### 6. enumerate 函数

```python
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
```

### 7. zip 函数

```python
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
for name, age in zip(names, ages):
    print(f"{name}: {age}")
```

### 8. map 函数

```python
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2, numbers))
print(squares)  # [1, 4, 9, 16, 25]
```

### 9. filter 函数

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even = list(filter(lambda x: x % 2 == 0, numbers))
print(even)  # [2, 4, 6, 8, 10]
```

## 示例说明

`demo.py` 文件包含了本课程的示例代码，展示了：
- 切片操作符的使用
- 可迭代对象和迭代器
- enumerate、zip、map、filter 函数

## 参考资料

- 廖雪峰 Python 教程：https://liaoxuefeng.com/books/python/introduction/index.html
- 菜鸟教程 Python3：https://www.runoob.com/python3/python3-tutorial.html
