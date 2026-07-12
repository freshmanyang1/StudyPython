# 迭代和enumerate

## 学习目标

- 掌握 for 循环迭代
- 了解 enumerate 函数的使用
- 掌握 zip 函数的使用
- 了解 map 函数的使用

## 知识点

### 1. for 循环迭代

```python
# 遍历列表
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# 遍历字符串
for char in "Hello":
    print(char)

# 遍历字典
d = {"a": 1, "b": 2}
for key, value in d.items():
    print(f"{key}: {value}")
```

### 2. enumerate 函数

```python
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
```

### 3. zip 函数

```python
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
for name, age in zip(names, ages):
    print(f"{name}: {age}")
```

### 4. map 函数

```python
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2, numbers))
print(squares)  # [1, 4, 9, 16, 25]
```

## 示例说明

`demo.py` 文件包含了本课程的示例代码，展示了：
- for 循环迭代
- enumerate 函数
- zip 函数
- map 函数

## 参考资料

- 廖雪峰 Python 教程：https://liaoxuefeng.com/books/python/introduction/index.html
- 菜鸟教程 Python3：https://www.runoob.com/python3/python3-tutorial.html
