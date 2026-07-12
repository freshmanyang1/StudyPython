# 循环for

## 学习目标

- 掌握 for 循环的语法
- 了解 range() 函数的使用
- 掌握遍历列表和字符串
- 了解 enumerate 函数

## 知识点

### 1. for 循环

```python
# 遍历列表
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# 遍历字符串
for char in "Hello":
    print(char)
```

### 2. range() 函数

```python
# range(stop)
for i in range(5):      # 0, 1, 2, 3, 4
    print(i)

# range(start, stop)
for i in range(1, 6):   # 1, 2, 3, 4, 5
    print(i)

# range(start, stop, step)
for i in range(0, 10, 2):  # 0, 2, 4, 6, 8
    print(i)
```

### 3. enumerate 函数

```python
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
```

### 4. for-else 语句

```python
for i in range(5):
    print(i)
else:
    print("循环结束")
```

### 5. 嵌套循环

```python
for i in range(3):
    for j in range(3):
        print(f"({i}, {j})", end=" ")
    print()
```

## 示例说明

`demo.py` 文件包含了本课程的示例代码，展示了：
- for 循环
- range() 函数
- enumerate 函数
- for-else 语句
- 嵌套循环

## 参考资料

- 廖雪峰 Python 教程：https://liaoxuefeng.com/books/python/introduction/index.html
- 菜鸟教程 Python3：https://www.runoob.com/python3/python3-tutorial.html
