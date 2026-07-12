# 函数

## 学习目标

- 掌握函数的定义和调用
- 了解函数的参数和返回值
- 掌握函数的作用域
- 了解函数的文档字符串

## 知识点

### 1. 函数定义

```python
def greet():
    print("Hello, World!")

# 调用函数
greet()
```

### 2. 函数参数

```python
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")  # Hello, Alice!
```

### 3. 默认参数

```python
def greet(name="World"):
    print(f"Hello, {name}!")

greet()         # Hello, World!
greet("Alice")  # Hello, Alice!
```

### 4. 返回值

```python
def add(a, b):
    return a + b

result = add(3, 5)
print(result)  # 8
```

### 5. 多个返回值

```python
def get_info():
    return "Alice", 25

name, age = get_info()
print(f"姓名: {name}, 年龄: {age}")
```

### 6. 函数作用域

```python
# 全局变量
x = 10

def foo():
    # 局部变量
    y = 20
    print(f"x = {x}")
    print(f"y = {y}")

foo()
print(f"x = {x}")
# print(y)  # 错误：y 未定义
```

### 7. global 关键字

```python
x = 10

def foo():
    global x
    x = 20

foo()
print(x)  # 20
```

### 8. 文档字符串

```python
def greet(name):
    """
    向用户打招呼
    
    参数:
        name: 用户名字
    
    返回:
        无
    """
    print(f"Hello, {name}!")

print(greet.__doc__)
```

### 9. 函数作为参数

```python
def apply(func, value):
    return func(value)

def square(x):
    return x ** 2

result = apply(square, 5)
print(result)  # 25
```

## 示例说明

`demo.py` 文件包含了本课程的示例代码，展示了：
- 函数的定义和调用
- 函数的参数和返回值
- 函数的作用域
- 函数的文档字符串

## 参考资料

- 廖雪峰 Python 教程：https://liaoxuefeng.com/books/python/introduction/index.html
- 菜鸟教程 Python3：https://www.runoob.com/python3/python3-tutorial.html
