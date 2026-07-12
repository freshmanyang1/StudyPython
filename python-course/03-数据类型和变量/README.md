# 数据类型和变量

## 学习目标

- 掌握 Python 的基本数据类型
- 理解变量的概念和使用
- 掌握类型转换的方法
- 了解动态类型的特点

## 知识点

### 1. 变量

变量是用来存储数据的容器。

```python
x = 10          # 整数
name = "Alice"  # 字符串
pi = 3.14       # 浮点数
is_true = True  # 布尔值
```

**变量特点：**
- 不需要声明类型
- 赋值即创建
- 可以随时改变类型

### 2. 数据类型

Python 有以下基本数据类型：

| 类型 | 说明 | 示例 |
|---|---|---|
| int | 整数 | 10, -5, 0 |
| float | 浮点数 | 3.14, -0.5 |
| str | 字符串 | "hello", 'world' |
| bool | 布尔值 | True, False |
| NoneType | 空值 | None |

### 3. 整数 (int)

```python
a = 10
b = -5
c = 0
d = 0b1010  # 二进制
e = 0o12    # 八进制
f = 0xa     # 十六进制
```

### 4. 浮点数 (float)

```python
x = 3.14
y = -0.5
z = 1.0
e = 1.5e10  # 科学计数法
```

### 5. 字符串 (str)

```python
s1 = "Hello"
s2 = 'World'
s3 = """多行
字符串"""
```

### 6. 布尔值 (bool)

```python
is_true = True
is_false = False

# 布尔运算
print(True and True)   # True
print(True or False)   # True
print(not True)        # False
```

### 7. 空值 (None)

```python
x = None
print(x)        # None
print(type(x))  # <class 'NoneType'>
```

### 8. 类型检查

```python
x = 10
print(type(x))  # <class 'int'>

y = "hello"
print(type(y))  # <class 'str'>
```

### 9. 类型转换

```python
# 转换为整数
int("123")    # 123
int(3.14)     # 3
int(True)     # 1

# 转换为浮点数
float("3.14") # 3.14
float(10)     # 10.0

# 转换为字符串
str(123)      # "123"
str(3.14)     # "3.14"
str(True)     # "True"

# 转换为布尔值
bool(0)       # False
bool("")      # False
bool(None)    # False
bool(1)       # True
bool("hello") # True
```

## 示例说明

`demo.py` 文件包含了本课程的示例代码，展示了：
- 各种数据类型的定义和使用
- 类型检查和类型转换
- 变量的赋值和使用

## 参考资料

- 廖雪峰 Python 教程：https://liaoxuefeng.com/books/python/introduction/index.html
- 菜鸟教程 Python3：https://www.runoob.com/python3/python3-tutorial.html
