# 字符串基础

## 学习目标

- 掌握字符串的创建方法
- 了解字符串的常用方法
- 掌握字符串的格式化
- 了解字符串的索引和切片

## 知识点

### 1. 字符串的创建

```python
# 单引号
s1 = 'Hello'

# 双引号
s2 = "World"

# 三引号（多行字符串）
s3 = """多行
字符串"""

s4 = '''也是
多行字符串'''
```

### 2. 转义字符

```python
\n  # 换行
\t  # 制表符
\\  # 反斜杠
\'  # 单引号
\"  # 双引号
```

### 3. 字符串操作

```python
# 拼接
s = "Hello" + " " + "World"

# 重复
s = "Hello" * 3  # "HelloHelloHello"

# 长度
len("Hello")  # 5
```

### 4. 字符串索引

```python
s = "Hello"
s[0]   # 'H'
s[1]   # 'e'
s[-1]  # 'o'
s[-2]  # 'l'
```

### 5. 字符串切片

```python
s = "Hello World"
s[0:5]    # "Hello"
s[6:]     # "World"
s[:5]     # "Hello"
s[::2]    # "HloWrd"
s[::-1]   # "dlroW olleH"
```

### 6. 常用方法

```python
s = "Hello World"

s.lower()      # "hello world"
s.upper()      # "HELLO WORLD"
s.strip()      # 去除首尾空格
s.split()      # ['Hello', 'World']
s.replace("Hello", "Hi")  # "Hi World"
s.find("World")  # 6
s.startswith("Hello")  # True
s.endswith("World")    # True
```

### 7. 格式化

```python
# f-string (推荐)
name = "Alice"
age = 25
print(f"姓名: {name}, 年龄: {age}")

# format 方法
print("姓名: {}, 年龄: {}".format(name, age))

# % 格式化
print("姓名: %s, 年龄: %d" % (name, age))
```

## 示例说明

`demo.py` 文件包含了本课程的示例代码，展示了：
- 字符串的创建和转义字符
- 字符串的索引和切片
- 字符串的常用方法
- 字符串的格式化

## 参考资料

- 廖雪峰 Python 教程：https://liaoxuefeng.com/books/python/introduction/index.html
- 菜鸟教程 Python3：https://www.runoob.com/python3/python3-tutorial.html
