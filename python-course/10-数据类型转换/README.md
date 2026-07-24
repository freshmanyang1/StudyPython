# 数据类型转换

## 学习目标

- 掌握类型转换函数
- 了解类型检查方法
- 理解隐式转换和显式转换
- 掌握常见转换场景

## 知识点

### 1. 类型转换函数

```python
# 转换为整数
int("123")    # 123
int(3.14)     # 3
int(True)     # 1
int(False)    # 0

# 转换为浮点数
float("3.14") # 3.14
float(10)     # 10.0
float(True)   # 1.0

# 转换为字符串
str(123)      # "123"
str(3.14)     # "3.14"
str(True)     # "True"
str(None)     # "None"

# 转换为布尔值
bool(0)       # False
bool("")      # False
bool(None)    # False
bool(1)       # True
bool("hello") # True
```

### 2. 类型检查

```python
x = 10
print(type(x))           # <class 'int'>
print(isinstance(x, int)) # True            #isinstance() 用来判断：一个值是否属于指定的数据类型
                                            #isinstance(值, 数据类型)
y = "hello"
print(type(y))           # <class 'str'>
print(isinstance(y, str)) # True
```

### 3. 隐式转换

Python 会自动进行一些类型转换：

```python
# 整数和浮点数运算
result = 1 + 2.0  # 3.0（浮点数）

# 字符串拼接
s = "Hello" + " " + "World"  # "Hello World"
```

### 4. 显式转换

使用类型转换函数进行转换：

```python
# 字符串转整数
num = int("123")

# 整数转字符串
s = str(123)

# 字符串转浮点数
f = float("3.14")
```

### 5. 常见转换场景

```python
# 用户输入转换
user_input = input("请输入数字: ")
num = int(user_input)

# 数字格式化
price = 99.9
print(f"价格: {price:.2f} 元")

# 列表转字符串
words = ["Hello", "World"]
sentence = " ".join(words)  # "Hello World"

# 字符串转列表
s = "Hello World"
words = s.split()  # ["Hello", "World"]
```

## 示例说明

`demo.py` 文件包含了本课程的示例代码，展示了：
- 类型转换函数
- 类型检查方法
- 隐式转换和显式转换
- 常见转换场景

## 参考资料

- 廖雪峰 Python 教程：https://liaoxuefeng.com/books/python/introduction/index.html
- 菜鸟教程 Python3：https://www.runoob.com/python3/python3-tutorial.html
