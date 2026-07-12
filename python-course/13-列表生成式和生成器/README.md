# 列表生成式和生成器

## 学习目标

- 掌握列表生成式的语法
- 了解生成器的概念和使用
- 掌握 yield 关键字的用法
- 理解惰性计算的概念

## 知识点

### 1. 列表生成式

```python
# 基本语法
squares = [x**2 for x in range(10)]

# 带条件
even = [x for x in range(10) if x % 2 == 0]

# 嵌套
matrix = [[i * j for j in range(5)] for i in range(5)]
```

### 2. 列表生成式的应用

```python
# 字符串处理
words = ["hello", "world", "python"]
upper_words = [word.upper() for word in words]

# 字典生成
squares_dict = {x: x**2 for x in range(10)}

# 集合生成
unique_lengths = {len(word) for word in words}
```

### 3. 生成器

生成器是一种特殊的迭代器，使用 yield 关键字。

```python
def countdown(n):
    while n > 0:
        yield n
        n -= 1

for i in countdown(5):
    print(i)
```

### 4. 生成器表达式

```python
# 列表生成式
squares_list = [x**2 for x in range(10)]

# 生成器表达式
squares_gen = (x**2 for x in range(10))
```

### 5. yield 关键字

```python
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib = fibonacci()
for _ in range(10):
    print(next(fib))
```

### 6. 生成器的优势

- 节省内存：惰性计算，按需生成
- 无限序列：可以表示无限序列
- 管道操作：可以串联多个生成器

### 7. send 方法

```python
def counter():
    n = 0
    while True:
        n += 1
        received = yield n
        if received is not None:
            n = received

c = counter()
print(next(c))      # 1
print(next(c))      # 2
print(c.send(10))   # 11
print(next(c))      # 12
```

## 示例说明

`demo.py` 文件包含了本课程的示例代码，展示了：
- 列表生成式的语法和应用
- 生成器的概念和使用
- yield 关键字的用法
- 生成器的优势

## 参考资料

- 廖雪峰 Python 教程：https://liaoxuefeng.com/books/python/introduction/index.html
- 菜鸟教程 Python3：https://www.runoob.com/python3/python3-tutorial.html
