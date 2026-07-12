# 函数的参数

## 学习目标

- 掌握位置参数和关键字参数
- 了解可变参数 *args 和 **kwargs
- 掌握参数解包
- 了解参数的传递方式

## 知识点

### 1. 位置参数

```python
def greet(name, age):
    print(f"姓名: {name}, 年龄: {age}")

greet("Alice", 25)  # 位置参数
```

### 2. 关键字参数

```python
def greet(name, age):
    print(f"姓名: {name}, 年龄: {age}")

greet(age=25, name="Alice")  # 关键字参数
```

### 3. 默认参数

```python
def greet(name, age=18):
    print(f"姓名: {name}, 年龄: {age}")

greet("Alice")        # 使用默认值
greet("Bob", 25)      # 覆盖默认值
```

### 4. 可变参数 *args

```python
def sum_numbers(*args):
    return sum(args)

print(sum_numbers(1, 2, 3))      # 6
print(sum_numbers(1, 2, 3, 4, 5)) # 15
```

### 5. 关键字可变参数 **kwargs

```python
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=25, city="Beijing")
```

### 6. 参数组合

```python
def func(a, b, *args, **kwargs):
    print(f"a = {a}")
    print(f"b = {b}")
    print(f"args = {args}")
    print(f"kwargs = {kwargs}")

func(1, 2, 3, 4, x=5, y=6)
```

### 7. 参数解包

```python
def add(a, b, c):
    return a + b + c

numbers = [1, 2, 3]
print(add(*numbers))  # 6

info = {"name": "Alice", "age": 25}
print_info(**info)
```

### 8. 强制关键字参数

```python
def func(a, b, *, c, d):
    print(a, b, c, d)

func(1, 2, c=3, d=4)  # 正确
# func(1, 2, 3, 4)    # 错误
```

## 示例说明

`demo.py` 文件包含了本课程的示例代码，展示了：
- 位置参数和关键字参数
- 可变参数 *args 和 **kwargs
- 参数解包
- 参数的传递方式

## 参考资料

- 廖雪峰 Python 教程：https://liaoxuefeng.com/books/python/introduction/index.html
- 菜鸟教程 Python3：https://www.runoob.com/python3/python3-tutorial.html
