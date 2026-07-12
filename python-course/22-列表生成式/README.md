# 列表生成式

## 学习目标

- 掌握列表生成式的基本语法
- 了解带条件的列表生成式
- 掌握嵌套列表生成式

## 知识点

### 1. 基本语法

```python
# 基本语法
squares = [x**2 for x in range(10)]
print(squares)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

### 2. 带条件

```python
# 带条件
even = [x for x in range(10) if x % 2 == 0]
print(even)  # [0, 2, 4, 6, 8]
```

### 3. 嵌套列表生成式

```python
# 嵌套列表生成式
matrix = [[i * j for j in range(5)] for i in range(5)]
for row in matrix:
    print(row)
```

### 4. 字符串处理

```python
# 字符串处理
words = ["hello", "world", "python"]
upper_words = [word.upper() for word in words]
print(upper_words)  # ['HELLO', 'WORLD', 'PYTHON']
```

## 示例说明

`demo.py` 文件包含了本课程的示例代码，展示了：
- 列表生成式的基本语法
- 带条件的列表生成式
- 嵌套列表生成式

## 参考资料

- 廖雪峰 Python 教程：https://liaoxuefeng.com/books/python/introduction/index.html
- 菜鸟教程 Python3：https://www.runoob.com/python3/python3-tutorial.html
